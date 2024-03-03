# prompt = "Generate a single color green logo for an operability best practice called "{{pattern_name}}", that is defined as "{{short_description}}""
import os
import yaml
import re
from PIL import Image, ImageOps, ImageColor
import logging

logging.basicConfig(level=logging.INFO)

icon_largest_dimension = 768

colors ={'architecting':ImageColor.getrgb('#00866e'),
    'running':ImageColor.getrgb('#00b06f'),
    'building':ImageColor.getrgb('#00cc9b'),
    'releasing':ImageColor.getrgb('#3c7e5a'),
    'anti-pattern':ImageColor.getrgb('#ff7346')}

white = (255, 255, 255, 255)

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
            if pattern['category'] == 'prefix' or pattern['category'] == 'suffix':
                continue

            pattern_slug = pattern['pattern_name'].lower().replace(' ', '-')
            pattern_slug = re.sub(rf'[!]', '', pattern_slug)
            icon_file = f"static/images/icons/{pattern_slug}.png"

            # check if icon already exists
            if os.path.exists(icon_file):
                # load image
                img = Image.open(icon_file)

                # check if image needs to be cropped
                bounds = get_image_bounds(img)
                if img.size != (bounds[2], bounds[3]):
                    print(f"Cropping icon for {pattern['pattern_name']}")
                    img = img.crop(bounds)
                else:
                    print(f"Icon for {pattern['pattern_name']} is already cropped")
                
                # create 1bpp icon
                img =img.convert('L')
                img = img.point(lambda p: p > 252 and 255)
                img = img.convert('1')
                img.save(icon_file)

            else:
                print(f"Creating icon for {pattern['pattern_name']}")

                # TODO
                pass

generate_icons('patterns.yaml')
generate_icons('anti_patterns.yaml')