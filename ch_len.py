import json
data = json.load(open('data/output/book_structure.json', encoding='utf-8', errors='ignore'))
chapters = data.get('sections', [])
for i, ch in enumerate(chapters[:10]):
    length = len(json.dumps(ch))
    print(f"Chapter {i+1}: {length} chars")
