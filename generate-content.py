import os
import re
import ollama
import logging
import json
import yaml
from datetime import datetime
from openai import OpenAI
import frontmatter
import generator
import data

model_name='llama2:13b'
#model_name='qwen:14b'
#model_name='gemma:7b'

if 'OPENAI_API_KEY' in os.environ:
  client = OpenAI()

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
    creation_date = datetime.fromtimestamp(response.created).astimezone().isoformat()

    # save the response to a json file
    # create the directory if it doesn't exist
    os.makedirs('openai', exist_ok=True)
    with open(f'openai/openai-response-{creation_date}.json', 'w', newline='') as jsonfile:
        # write the json response to the file
        jsonfile.write(json.dumps(response, indent=4))

    # extract last line from the content
    #last_line = content.trim().split('\n')[-1]

    return content, creation_date

def generate_pattern(prompt, prefix, suffix, model_name):

  # add trailing dot to the short description if it is missing
  if prompt['short_description'][-1] != '.': prompt['short_description'] += '.'

  full_prompt = prefix + "\n" + prompt['prompt'] + "\n" + suffix
  # replace the pattern_name in the prompt with the actual pattern name
  full_prompt = generator.render_template_from_string(full_prompt, prompt)

  pattern_slug = data.generate_slug(prompt['pattern_name'])
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
    if prompt['image_prompt']:
      # generate the image
      generator.generate_image_comfy(prompt['image_prompt'], 'text, watermark', image_path)
    else:
      logging.error(f"Image not found for {prompt['pattern_name']} and image_prompt was not set.")
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

  filecontents = generator.render_template_from_file('page-template.md', prompt)

  # create the directory if it doesn't exist
  os.makedirs(os.path.dirname(output_file_name), exist_ok=True)

  # write the response to a markdown file
  with open(output_file_name, 'w', newline='') as mdfile:
    mdfile.write(filecontents)

def generate_content(patterns, prefix, suffix, model_name):
  for prompt in patterns:
    generate_pattern(prompt, prefix, suffix, model_name)

generate_content(data.patterns, data.pattern_prefix, data.pattern_suffix, model_name)
generate_content(data.anti_patterns, data.anti_pattern_prefix, data.anti_pattern_suffix, model_name)

json_data = {'patterns' : data.patterns, 'anti_patterns' : data.anti_patterns}
with open('./json/data.json', 'w', newline='') as jsonfile:
  # write the json response to the file
  jsonfile.write(json.dumps(json_data))