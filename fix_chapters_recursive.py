import json

def promote_units_to_chapters(data):
    if isinstance(data, dict):
        if data.get('type') == 'heading':
            text = data.get('text', '').upper().strip()
            # Catch UNIT 1, UNIT I, UNIT-I, etc.
            if 'UNIT' in text and any(num in text for num in ['1', '2', '3', '4', '5', 'I', 'V']):
                print(f"Promoting to Chapter (Level 1): {text}")
                data['level'] = 1
        
        for key, value in data.items():
            promote_units_to_chapters(value)
            
    elif isinstance(data, list):
        for item in data:
            promote_units_to_chapters(item)

if __name__ == "__main__":
    filepath = 'data/output/book_structure.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        structure = json.load(f)
        
    print("Scanning structure for UNIT headings...")
    promote_units_to_chapters(structure)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(structure, f, indent=2)
        
    print("Done. All units promoted to Chapters.")
