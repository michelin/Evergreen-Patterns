import ollama 
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape
import stablediff

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

def generate_image(prompt, negative_prompt, icon_file):

    payload = {
        "prompt": prompt,  # extra networks also in prompts
        "negative_prompt": negative_prompt,
#        "seed": 1,
        "steps": 20,
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "sampler_name": "DPM++ 2M Karras",
        "n_iter": 1,
        "batch_size": 1,

        # example args for x/y/z plot
        # "script_name": "x/y/z plot",
        # "script_args": [
        #     1,
        #     "10,20",
        #     [],
        #     0,
        #     "",
        #     [],
        #     0,
        #     "",
        #     [],
        #     True,
        #     True,
        #     False,
        #     False,
        #     0,
        #     False
        # ],

        # example args for Refiner and ControlNet
        # "alwayson_scripts": {
        #     "ControlNet": {
        #         "args": [
        #             {
        #                 "batch_images": "",
        #                 "control_mode": "Balanced",
        #                 "enabled": True,
        #                 "guidance_end": 1,
        #                 "guidance_start": 0,
        #                 "image": {
        #                     "image": encode_file_to_base64(r"B:\path\to\control\img.png"),
        #                     "mask": None  # base64, None when not need
        #                 },
        #                 "input_mode": "simple",
        #                 "is_ui": True,
        #                 "loopback": False,
        #                 "low_vram": False,
        #                 "model": "control_v11p_sd15_canny [d14c016b]",
        #                 "module": "canny",
        #                 "output_dir": "",
        #                 "pixel_perfect": False,
        #                 "processor_res": 512,
        #                 "resize_mode": "Crop and Resize",
        #                 "threshold_a": 100,
        #                 "threshold_b": 200,
        #                 "weight": 1
        #             }
        #         ]
        #     },
        #     "Refiner": {
        #         "args": [
        #             True,
        #             "sd_xl_refiner_1.0",
        #             0.5
        #         ]
        #     }
        # },
        # "enable_hr": True,
        # "hr_upscaler": "R-ESRGAN 4x+ Anime6B",
        # "hr_scale": 2,
        # "denoising_strength": 0.5,
        # "styles": ['style 1', 'style 2'],
        # "override_settings": {
        #     'sd_model_checkpoint': "sd_xl_base_1.0",  # this can use to switch sd model
        # },
    }
    stablediff.call_txt2img_api(icon_file, **payload)    

def render_template_from_string(template_str, context):
  template = env.from_string(template_str)
  return template.render(context)

def render_template_from_file(template_file, context):
  template = env.get_template(template_file)
  return template.render(context)  