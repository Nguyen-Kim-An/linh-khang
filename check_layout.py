import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

sections = soup.find_all(class_='ladi-section')
print("Sections in DOM order:")
for s in sections:
    sid = s.get('id', '')
    imgs = [img.get('id') for img in s.find_all(class_='ladi-image') if img.get('id')]
    headlines = [h.get_text(strip=True) for h in s.find_all(class_='ladi-headline')[:3]]
    print(f"Section {sid}: images={imgs}, text sample={headlines[:2]}")

# Also check lightbox or gallery scripts/attributes
print("\nChecking ladi-image data or click actions:")
image_ids = [
    'IMAGE130', 'IMAGE210', 'IMAGE211', 'IMAGE78', 'IMAGE80', 'IMAGE77',
    'IMAGE187', 'IMAGE241', 'IMAGE242', 'IMAGE243', 'IMAGE244', 'IMAGE245',
    'IMAGE85', 'IMAGE230', 'IMAGE231', 'IMAGE233', 'IMAGE234', 'IMAGE235', 'IMAGE96'
]
for img_id in image_ids:
    tag = soup.find(id=img_id)
    if tag:
        # find dimensions in style
        print(f"{img_id}: tag={tag.name}, parent={tag.parent.get('id', '')}")
