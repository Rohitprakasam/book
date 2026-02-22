import json

data = json.load(open('data/output/book_structure.json', encoding='utf-8'))
levels = []
for i, c in enumerate(data.get('sections', [])):
    if c.get('type') == 'chapter':
        for s in c.get('sections', []):
            if s.get('type') == 'heading':
                levels.append(f"Section {i}: L{s['level']} {s.get('text', '')[:50]}")

with open('temp_headings.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(levels))
