import json

def fix_hierarchy():
    with open('data/output/book_structure.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for chapter in data.get('sections', []):
        if chapter.get('type') == 'chapter':
            for sec in chapter.get('sections', []):
                if sec.get('type') == 'heading':
                    text = sec.get('text', '').upper()
                    # Promote UNIT headings to level 1 if they aren't already
                    if 'UNIT-I' in text or 'UNIT-II' in text or 'UNIT-III' in text or 'UNIT - I' in text or 'UNIT - II' in text or 'UNIT - III' in text or 'UNIT I' in text or 'UNIT II' in text or 'UNIT III' in text:
                        print(f"Promoting: {text}")
                        sec['level'] = 1

    with open('data/output/book_structure.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Hierarchy fixed!")

if __name__ == "__main__":
    fix_hierarchy()
