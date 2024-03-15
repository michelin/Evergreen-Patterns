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

#model_name='llama2:13b'
model_name='qwen:14b'
#model_name='gemma:7b'

# reads all tags from the all_tags.txt file
tags = []
with open('all_tags.txt', 'r') as file:
  tags = file.readlines()
  tags = [tag.strip() for tag in tags]

def generate_content(patterns, prefix, suffix, model_name):
  for pattern in patterns:
    full_prompt = prefix + "\n" + pattern['prompt'] + "\n"
    full_prompt += "Please select the 3 tags that best describe this pattern from the list below, you must not specify any tags which are not in this list:\n"
    full_prompt += "\n".join(tags) + "\nPlease only include the pattern name and the 3 tags separated by commas in your response."
    full_prompt = generator.render_template_from_string(full_prompt, pattern)
    text = generator.generate_text_ollama(model_name, full_prompt)
    print(text)

generate_content(data.patterns, data.pattern_prefix, data.pattern_suffix, model_name)
generate_content(data.anti_patterns, data.anti_pattern_prefix, data.anti_pattern_suffix, model_name)