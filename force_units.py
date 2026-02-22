import json

def force_all_units(data):
    if isinstance(data, dict):
        if data.get('type') == 'heading':
            text = data.get('text', '').upper().strip()
            # If the heading text CONTAINS the word UNIT or CHAPTER anywhere, force it to Level 1
            if 'UNIT' in text or 'CHAPTER' in text:
                print(f"Force Promoted: {text}")
                data['level'] = 1
        
        for key, value in data.items():
            force_all_units(value)
            
    elif isinstance(data, list):
        for item in data:
            force_all_units(item)

if __name__ == "__main__":
    filepath = 'data/output/book_structure.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        structure = json.load(f)
        
    print("Scanning structure to force Level 1 for ALL Units/Chapters...")
    force_all_units(structure)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(structure, f, indent=2)
        
    print("Done. Forced Level 1.")
