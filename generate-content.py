import os
import re
import ollama
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import yaml
from datetime import datetime
from openai import OpenAI
import frontmatter
import generator


client = OpenAI()

model_name='llama2:13b'
#model_name='qwen:14b'
#model_name='gemma:7b'

def generate_text_openai(full_prompt):
    model_name = 'gpt-4-turbo-preview'
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are an expert in IT systems quality of service."},
            {"role": "user", "content": full_prompt}
        ]
    )

    content = response.choices[0].message.content

    # extract last line from the content
    #last_line = content.trim().split('\n')[-1]

    return response.choices[0].message.content, datetime.fromtimestamp(response.created).astimezone().isoformat() 

def generate_pattern(prompt, prefix, suffix, model_name, responses):

  # add trailing dot to the short description if it is missing
  if prompt['short_description'][-1] != '.': prompt['short_description'] += '.'

  full_prompt = prefix + "\n" + prompt['prompt'] + "\n" + suffix
  # replace the pattern_name in the prompt with the actual pattern name
  template = env.from_string(full_prompt)
  full_prompt = template.render(prompt)

  pattern_slug = prompt['pattern_name'].lower().replace(' ', '-')
  pattern_slug = re.sub(rf'[!]', '', pattern_slug)

  prompt['pattern_slug'] = pattern_slug
  output_file_name = os.path.join('content', prompt['family'], pattern_slug + '.md')

  icon_path = f"static/images/icons/{pattern_slug}.png"
  # create the directory if it doesn't exist
  os.makedirs(os.path.dirname(icon_path), exist_ok=True)

  if not os.path.exists(icon_path):
    logging.error(f"Icon not found for {prompt['pattern_name']}.")
  else:
    prompt['icon'] = f"images/icons/{pattern_slug}.png"

  image_path = f"static/images/{pattern_slug}.webp"
  if not os.path.exists(image_path):
    logging.error(f"Image not found for {prompt['pattern_name']}.")
  else:
    prompt['image'] = f"images/{pattern_slug}.png"

  # check if the file already exists and if it does, read the status
  file_status = None
  if os.path.exists(output_file_name):
    fm = frontmatter.Frontmatter().read_file(output_file_name)
    tags = fm['attributes']['tags']
    file_status = fm['attributes']['status']

  if file_status == 'reviewed':
    logging.debug(f"Skipping {prompt['pattern_name']} as it is already reviewed.")
    return

  logging.info(f"Generating content for : {prompt['pattern_name']} to {output_file_name}")

  response_content, creation_date = generator.generate_text_ollama(model_name, full_prompt)
  # response_content, creation_date = generate_text_openai(full_prompt)

  prompt['page_contents'] = response_content
  # inject generation date in prompt
  prompt['creation_date'] = creation_date
  prompt['status'] = 'draft'
  prompt['model'] = model_name

  # TODO : extracts tags values from the response
  # raw_tags = tags_response['message']['content'].split(',')
  # raw_tags = [tag.strip() for tag in raw_tags]
  # prompt['tags'] = prompt['tags'] + "," + ",".join(raw_tags)

  file_template = env.get_template('page-template.md')
  filecontents = file_template.render(prompt)

  responses.append({'family': prompt['family'], 'model':model_name, 'prompt': full_prompt, 'contents': filecontents})

  # create the directory if it doesn't exist
  os.makedirs(os.path.dirname(output_file_name), exist_ok=True)

  # write the response to a markdown file
  with open(output_file_name, 'w', newline='') as mdfile:
    # write the markdown response to the file
    mdfile.write(filecontents)

def generate_content(file_name, model_name):
  # load the yaml file
  prompts = []
  with open(file_name, newline='') as yamlfile:
    prompts = yaml.load(yamlfile, Loader=yaml.FullLoader)

  # loop through the prompts and get the responses
  prefix = "\n".join([prompt['prompt'] for prompt in prompts if prompt['family'] == 'prefix'])
  suffix = "\n".join([prompt['prompt'] for prompt in prompts if prompt['family'] == 'suffix'])

  responses = []
  for prompt in prompts:
    if prompt['family'] == 'prefix' or prompt['family'] == 'suffix':
      continue

    generate_pattern(prompt, prefix, suffix, model_name, responses)

  # write the responses to a json file
  with open(f"{model_name}-{file_name}.json", 'w', newline='') as jsonfile:
    # write the json response to the file
    jsonfile.write(json.dumps(responses))

generate_content('patterns.yaml', model_name)
generate_content('anti_patterns.yaml', model_name)