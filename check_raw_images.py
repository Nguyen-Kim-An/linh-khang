import re

with open('raw_site.html', 'r', encoding='utf-8') as f:
    content = f.read()

image_ids = [
    'IMAGE130', 'IMAGE210', 'IMAGE211', 'IMAGE78', 'IMAGE80', 'IMAGE77',
    'IMAGE187', 'IMAGE241', 'IMAGE242', 'IMAGE243', 'IMAGE244', 'IMAGE245',
    'IMAGE85', 'IMAGE230', 'IMAGE231', 'IMAGE233', 'IMAGE234', 'IMAGE235', 'IMAGE96'
]

for img_id in image_ids:
    m = re.findall(rf'#{img_id}[^}}]*background-image:\s*url\(([^)]+)\)', content)
    print(f'{img_id}: {m}')
