import os
import yaml
import re
from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageOps

card_size = (650, 1000)

x_center = card_size[0] / 2
y_center = card_size[1] / 2

michelin_font = ImageFont.truetype("themes/evergreen/assets/evergreen/fonts/MichelinUnitTitling-SemiBold.ttf", size=44)
font = ImageFont.truetype("themes/evergreen/assets/evergreen/fonts/Swansea-q3pd.ttf", size=36)
font_spacing_y = 6

colors ={'architecting':ImageColor.getrgb('#00866eff'),
    'running':ImageColor.getrgb('#00b06fff'),
    'building':ImageColor.getrgb('#00cc9bff'),
    'releasing':ImageColor.getrgb('#3c7e5aff'),
    'anti-pattern':ImageColor.getrgb('#ff7346ff')}

family_names = {'architecting':'Architecting\nSystems',
    'running':'Running\nSystems',
    'building':'Building\nSystems',
    'releasing':'Releasing\nSystems',
    'anti-pattern':'Anti-Patterns'}

white = (255, 255, 255, 255)

def draw_text_left_align(draw, text, color, x, y, font):
    draw.text((x, y), text, color, font=font, align="left", anchor="lm")


def draw_text(draw, text, color, x, y, font, align):
    bbox = font.getmask(text, "L").getbbox()
    height = bbox[3] - bbox[1]
    max_y = y + height + font_spacing_y
    words = text.split(' ')
    if len(words) > 1 and bbox[2] > card_size[0]:
        removed = 0
        while removed < len(words) and bbox[2] > card_size[0]:
            removed+=1
            text = " ".join(words[:-removed])
            bbox = font.getmask(text, "L").getbbox()
        remaining_text = " ".join(words[-removed:])
        if len(remaining_text) > 0:
            max_y = draw_text(draw, remaining_text, color, x, y+height + font_spacing_y, font, align)

    draw.text((x, y), text, color, font=font, align=align, anchor="mm")
    return max_y

def generate_cards(yml_file):
    with open(yml_file, newline='') as yamlfile:
        cards = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for card in cards:
            if card['category'] == 'prefix' or card['category'] == 'suffix':
                continue

            pattern_slug = card['pattern_name'].lower().replace(' ', '-')
            pattern_slug = re.sub(rf'[!]', '', pattern_slug)

            card_file = f"static/cards/{pattern_slug}.png"
            # create folder if needed
            os.makedirs(os.path.dirname(card_file), exist_ok=True)

            color = colors[card['category']]

            icon_file = f"static/images/icons/{pattern_slug}.png"
            if not os.path.exists(icon_file):
                print(f"Icon for {card['pattern_name']} does not exist")
                continue
            icon = Image.open(icon_file)
            icon = icon.convert('L')
            icon =  ImageOps.colorize(icon, color, white)

            icon_width = 370
            
            # resize icon to icon_width width, maintaining aspect ratio
            ratio = icon.height / icon.width 
            icon = icon.resize((icon_width, int(icon_width*ratio)), resample=Image.LANCZOS)

            card_image = Image.new('RGBA', card_size, white)
            card_image.paste(icon, (int((card_size[0] - icon_width) / 2), 400 - int(icon.height / 2)))

            # generate a smaller version of the icon
            small_icon = Image.open(icon_file)
            small_icon = small_icon.convert('L')
            # invert the colors of the smaller icon
            small_icon =  ImageOps.colorize(small_icon, white, color)            
            small_icon = small_icon.resize((80, int(80*ratio)), resample=Image.LANCZOS)
            # make it square
            small_icon = ImageOps.pad(small_icon, (80, 80), color=color)
            card_image.paste(small_icon, (60, 30))

            # create a rectangle with the color
            draw = ImageDraw.Draw(card_image)
            draw.rectangle([0, 650, card_size[0], card_size[1]], fill=color)

            # draw text on card
            draw_text_left_align(draw, family_names[card['category']], color, 170, 70, michelin_font)
            y = draw_text(draw, card['pattern_name'], white, x_center, 700, michelin_font, "center")

            # draw a white line to separate the title from the description
            draw.line([200, y, 450, y], fill=white, width=8)

            # write the image description
            draw_text(draw, card['short_description'], white, x_center, y + 80, font,"center")

            # save card
            card_image.save(card_file)



generate_cards('patterns.yaml')
generate_cards('anti_patterns.yaml')