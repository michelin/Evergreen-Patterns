# prompt = "Generate a single color green logo for an operability best practice called "{{pattern_name}}", that is defined as "{{short_description}}""
import os
import yaml
import re
from PIL import Image
import logging
import generator

logging.basicConfig(level=logging.INFO)

white = (255, 255, 255, 255)

def generate_icon(text, icon_file):
    full_prompt = f"""
        Generate a monochrome line art icon with thick lines and a minimalist and modern aesthetic, black on a white background. No shading.
        It represents a {text}.
    """
    generator.generate_image_stablediff(full_prompt, "shading complex", icon_file)  

def get_image_bounds(img):
    img = img.convert('L')
    img = img.point(lambda p: p > 190 and 255)
    img = img.convert('1')
    img = img.point(lambda p: p == 0)
    bbox = img.getbbox()
    return bbox

def generate_icons(yml_file):
    with open(yml_file, newline='') as yamlfile:
        patterns = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for pattern in patterns:
            if pattern['family'] == 'prefix' or pattern['family'] == 'suffix':
                continue

            pattern_slug = pattern['pattern_name'].lower().replace(' ', '-')
            pattern_slug = re.sub(rf'[!]', '', pattern_slug)
            icon_file = f"static/images/icons/{pattern_slug}.png"

            # check if icon already exists
            if not os.path.exists(icon_file):
                print(f"Creating icon for {pattern['pattern_name']}")
                generate_icon(pattern['icon_prompt'], icon_file)

            
            # load image
            img = Image.open(icon_file)

            # check if image needs to be cropped
            bounds = get_image_bounds(img)
            if img.size != (bounds[2], bounds[3]):
                print(f"Cropping icon for {pattern['pattern_name']}")
                img = img.crop(bounds)
            else:
                print(f"Icon for {pattern['pattern_name']} is already cropped")

            if not img.has_transparency_data:
                # convert white to transparent
                img = img.convert('RGBA')
                datas = img.getdata()
                newData = []
                for item in datas:
                    if item[0] > 220 and item[1] > 220 and item[2] > 220:
                        newData.append((255, 255, 255, 0))
                    else:
                        newData.append(item)
                img.putdata(newData)   
                
                # create 1bpp icon
                img = img.point(lambda p: p > 254 and 255)
                img.save(icon_file)

generate_icons('patterns.yaml')
generate_icons('anti_patterns.yaml')