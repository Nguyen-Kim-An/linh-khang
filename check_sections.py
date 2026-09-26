import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

image_ids = [
    'IMAGE130', 'IMAGE210', 'IMAGE211', 'IMAGE78', 'IMAGE80', 'IMAGE77',
    'IMAGE187', 'IMAGE241', 'IMAGE242', 'IMAGE243', 'IMAGE244', 'IMAGE245',
    'IMAGE85', 'IMAGE230', 'IMAGE231', 'IMAGE233', 'IMAGE234', 'IMAGE235', 'IMAGE96'
]

# Find section of each image
for img_id in image_ids:
    tag = soup.find(id=img_id)
    if tag:
        parent_section = tag.find_parent(class_='ladi-section')
        sec_id = parent_section.get('id', 'unknown') if parent_section else 'none'
        classes = tag.get('class', [])
        print(f'{img_id}: section={sec_id}, classes={classes}')
    else:
        print(f'{img_id}: NOT FOUND')
