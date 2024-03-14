import yaml

def load_yaml(file_name):
  
  # load the yaml file
  prompts = []
  with open(file_name, newline='') as yamlfile:
    prompts = yaml.load(yamlfile, Loader=yaml.FullLoader)

  # loop through the prompts and get the responses
  prefix = "\n".join([prompt['prompt'] for prompt in prompts if prompt['family'] == 'prefix'])
  suffix = "\n".join([prompt['prompt'] for prompt in prompts if prompt['family'] == 'suffix'])

  # filter out the prompts that are not patterns
  return prefix, suffix, [prompt for prompt in prompts if prompt['family'] != 'prefix' and prompt['family'] != 'suffix']

pattern_prefix, pattern_suffix, patterns = load_yaml('patterns.yaml')
anti_pattern_prefix, anti_pattern_suffix, anti_patterns = load_yaml('anti_patterns.yaml')

