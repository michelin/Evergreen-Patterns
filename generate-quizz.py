import logging
import generator
import data

# set the logging level
logging.basicConfig(level=logging.INFO)

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

full_prompt = generator.render_template_from_string(full_prompt, {"patterns":data.patterns, "antipatterns":data.anti_patterns})

logging.info(full_prompt)