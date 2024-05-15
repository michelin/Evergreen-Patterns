import generator
import data

#model_name='llama2:13b'
#model_name='qwen:14b'
#model_name='gemma:7b'
model_name="llama3"

# reads all tags from the all_tags.txt file
tags = []
with open('all_tags.txt', 'r') as file:
  tags = file.readlines()
  tags = [tag.strip() for tag in tags]

def generate_content(patterns, template_name, model_name):
  for pattern in patterns:
    full_prompt = generator.render_template_from_file(template_name, pattern)
    full_prompt += "Please select the 3 tags that best describe this pattern from the list below, you must not specify any tags which are not in this list:\n"
    full_prompt += "\n".join(tags) + "\nPlease only include the pattern name and the 3 tags separated by commas in your response."
    text, _ = generator.generate_text_ollama(model_name, full_prompt)
    print(text)

generate_content(data.patterns, 'prompt-pattern.j2', model_name)
generate_content(data.anti_patterns, 'prompt-anti-pattern.j2', model_name)