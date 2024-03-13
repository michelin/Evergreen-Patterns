import ollama 
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape

# set the logging level
logging.basicConfig(level=logging.INFO)

# create a jinja2 environment that loads templates from the current directory
env = Environment(loader=FileSystemLoader('.'))

def generate_text_ollama(model_name, full_prompt):
  messages=[
    {
      'role': 'user',
      'content': full_prompt,
    },
  ]
  response = ollama.chat(model=model_name, messages=messages)
  return response['message']['content'], response['created_at']