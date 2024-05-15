import os
import logging
import json
from datetime import datetime
import generator
import data

model_name='llama3'

context = generator.render_template_from_file('context.j2', {'patterns': data.patterns, 'antipatterns': data.anti_patterns})
context += 'For every letter of the alphabet, choose a single word that begins with this letter and that is strongly related to the IT Quality of service and frugality context and is insired from our patterns and anti-patterns. After each word, include a description to explain why this word is adequate.'

print(context)

print(generator.generate_text_ollama(model_name, context))
