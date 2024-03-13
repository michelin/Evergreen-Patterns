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
I need you to associate each anti-pattern with one or several patterns that can be used to mitigate it.
You output should be a list of associations, one for each anti-pattern.
You can only use patterns that are defined in our list.
Also for each association, please explain briefly why this pattern can be used to mitigate the anti-pattern.
'''

template = env.from_string(full_prompt)
full_prompt = template.render(patterns=patterns, antipatterns=antipatterns)

logging.info(full_prompt)