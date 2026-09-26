import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'([^{}\n]+)\{([^}]*background-image:[^}]*)\}', content)
print(f'Total rules with background-image: {len(matches)}')
for sel, body in matches:
    url_m = re.search(r'background-image:\s*url\(([^)]+)\)', body)
    if url_m:
        url = url_m.group(1).strip('\"\'')
        print(f'{sel.strip()[:60]} => {url}')
