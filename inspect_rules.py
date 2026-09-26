import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

image_ids = [
    'IMAGE130', 'IMAGE210', 'IMAGE211', 'IMAGE78', 'IMAGE80', 'IMAGE77',
    'IMAGE187', 'IMAGE241', 'IMAGE242', 'IMAGE243', 'IMAGE244', 'IMAGE245',
    'IMAGE85', 'IMAGE230', 'IMAGE231', 'IMAGE233', 'IMAGE234', 'IMAGE235', 'IMAGE96'
]

for img_id in image_ids:
    # find size rule: #IMAGE...{...}
    m = re.findall(rf'(#{img_id}[^{{]*\{{[^}}]+\}})', content)
    bg_m = re.findall(rf'(#{img_id}[^}}]*background-image:[^}}]+)', content)
    print(f"=== {img_id} ===")
    for rule in m:
        if 'width' in rule or 'height' in rule:
            print("  SIZE:", rule[:100])
    for bg in bg_m:
        print("  BG:", bg[:120])
