import os
import csv
import ollama
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import yaml

# set the logging level
logging.basicConfig(level=logging.INFO)

# create a jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

#model_name='llama2:13b'
model_name='qwen:14b'

# load the patterns file
patterns = []
with open('patterns.yaml', newline='') as yamlfile:
  patterns = yaml.load(yamlfile, Loader=yaml.FullLoader)
  # remove patterns with a category of prefix or suffix
  patterns = [pattern for pattern in patterns if pattern['category'] != 'prefix' and pattern['category'] != 'suffix']

# load the antipatterns file
antipatterns = []
with open('anti_patterns.yaml', newline='') as yamlfile:
  antipatterns = yaml.load(yamlfile, Loader=yaml.FullLoader)
  # remove antipatterns with a category of prefix or suffix
  antipatterns = [pattern for pattern in antipatterns if pattern['category'] != 'prefix' and pattern['category'] != 'suffix']

# generate the prompt
full_prompt = '''
We are the Evergreen team. Our job is to improve the Quality of Service of the IT systems in our company.
In order to help the organisation transform and better address the subject,
we have described a set of patterns and anti-patterns that represent respectivelty the best and worst practices in the field.
The patterns that we have described are the following:
{% for pattern in patterns %}
- {{ pattern['pattern_name'] }} : "{{ pattern['short_description'] }}"
{% endfor %}
The anti-patterns that we have described are the following:
{% for antipattern in antipatterns %}
- {{ antipattern['pattern_name'] }} : "{{ antipattern['short_description'] }}"
{% endfor %}
I need you to create a quizz with 8 questions. Each question of the quizz should describe a fictive situation where one of the anti-pattern is represented.
The situation should be described with at least 3 sentences.
3 possible choices of Evergreen Patterns should be proposed as a possible solution to this situation but only one should be actually applicable to the situation described.
For each question, please explain briefly why the winning pattern is the best solution.
'''

template = env.from_string(full_prompt)
full_prompt = template.render(patterns=patterns, antipatterns=antipatterns)

logging.info(full_prompt)