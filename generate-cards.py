import os
import yaml
from PIL import Image, ImageFont, ImageDraw, ImageColor

card_size = (650, 1004)

x_center = card_size[0] / 2
y_center = card_size[1] / 2

font_size = 36

michelin_font = ImageFont.truetype("themes/evergreen/assets/evergreen/fonts/MichelinUnitTitling-Regular.ttf", size=40)
font = ImageFont.truetype("themes/evergreen/assets/evergreen/fonts/Swansea-q3pd.ttf", size=40)

colors ={'architecting':ImageColor.getrgb('#00866e'),
    'running':ImageColor.getrgb('#00b06f'),
    'building':ImageColor.getrgb('#00cc9b'),
    'releasing':ImageColor.getrgb('#3c7e5a'),
    'anti-pattern':ImageColor.getrgb('#ff7346')}

family_names = {'architecting':'Architecting\nSystems',
    'running':'Running\nSystems',
    'building':'Building\nSystems',
    'releasing':'Releasing\nSystems',
    'anti-pattern':'Anti-Patterns'}

white = (255, 255, 255, 255)

def draw_text(draw, text, color, x, y, font, align):
    mask = font.getmask(text, "L")
    bbox = mask.getbbox()
    words = text.split(' ')
    if len(words) > 0 and bbox[2] > card_size[0]:
        removed = 0
        while removed < len(words) and bbox[2] > card_size[0]:
            removed+=1
            text = " ".join(words[:-removed])
            mask = font.getmask(text, "L")
            bbox = mask.getbbox()
        remaining_text = " ".join(words[-removed:])
        if len(remaining_text) > 0:
            draw_text(draw, remaining_text, color, x, y+font_size, font, align)

    draw.text((x, y), text, color, font=font, align=align, anchor="mm")

def generate_cards(yml_file):
    with open(yml_file, newline='') as yamlfile:
        cards = yaml.load(yamlfile, Loader=yaml.FullLoader)
        for card in cards:
            if card['category'] == 'prefix' or card['category'] == 'suffix':
                continue

            print(card)

            card_file = f"static/cards/{card['pattern_name']}.png"

            # check if card already exists
            if os.path.exists(card_file):
                print(f"Card {card['pattern_name']} already exists")
                continue

            color = colors[card['category']]

            img = Image.new('RGBA', card_size, white)

            # create a rectangle with the color
            draw = ImageDraw.Draw(img)
            draw.rectangle([0, 650, card_size[0], card_size[1]], fill=color)

            # draw text on card
            draw_text(draw, family_names[card['category']], color, x_center, 50, michelin_font, "left")
            draw_text(draw, card['short_description'], white, x_center, 800, font,"center")
            draw_text(draw, card['pattern_name'], white, x_center, 700, michelin_font, "center")

            # draw a white line to separate the title from the description
            draw.line([200, 750, 450, 750], fill=white, width=8)

            # save card
            img.save(card_file)



generate_cards('patterns.yaml')
generate_cards('anti_patterns.yaml')