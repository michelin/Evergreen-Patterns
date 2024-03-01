# prompt = "Generate a single color green logo for an operability best practice called "{{pattern_name}}", that is defined as "{{short_description}}""
import os
import yaml
import re
from PIL import Image, ImageDraw, ImageColor

card_size = (650, 1004)

x_center = card_size[0] / 2
y_center = card_size[1] / 2

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
        cards = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for card in cards:
            if card['category'] == 'prefix' or card['category'] == 'suffix':
                continue

            pattern_slug = card['pattern_name'].lower().replace(' ', '-')
            pattern_slug = re.sub(rf'[!]', '', pattern_slug)
            icon_file = f"static/images/icons/{pattern_slug}.png"

            # check if icon already exists
            if os.path.exists(icon_file):
                print(f"Icon for {card['pattern_name']} already exists")
                # load image
                img = Image.open(icon_file)
                # check if image needs to be cropped
                bounds = get_image_bounds(img)
                if img.size != (bounds[2], bounds[3]):
                    print(f"Cropping icon for {card['pattern_name']}")
                    img = img.crop(bounds)
                    img.save(icon_file)
                else:
                    print(f"Icon for {card['pattern_name']} is already cropped")

            else:
                print(f"Creating icon for {card['pattern_name']}")

                # TODO
                pass

generate_icons('patterns.yaml')
generate_icons('anti_patterns.yaml')