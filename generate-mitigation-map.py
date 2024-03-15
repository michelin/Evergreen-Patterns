import os
import csv
import ollama
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import yaml
import data
import generator

# set the logging level
logging.basicConfig(level=logging.INFO)

# create a jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

#model_name='llama2:13b'
model_name='qwen:14b'

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
full_prompt = template.render(patterns=data.patterns, antipatterns=data.anti_patterns)

logging.info(full_prompt)

response_content, creation_date = generator.generate_text_ollama(model_name, full_prompt)
logging.info(response_content)