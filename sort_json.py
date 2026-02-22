import json
import re

def sort_book_structure():
    filepath = 'data/output/book_structure.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Identify which top-level chapter block belongs to which Unit
    # We will search the nested text of each top-level chapter for "UNIT X"
    
    sections = data.get('sections', [])
    ordered_sections = []
    
    # Store tuples of (Unit Number (or 99 if unknown), Section Data)
    categorized_sections = []
    
    for sec in sections:
        sec_str = json.dumps(sec).upper()
        
        # Simple heuristic to find unit numbers in the chunk
        unit_num = 99
        if 'UNIT-I' in sec_str or 'UNIT 1' in sec_str or 'UNIT - I' in sec_str or 'UNIT I ' in sec_str:
            unit_num = 1
        elif 'UNIT-II' in sec_str or 'UNIT 2' in sec_str or 'UNIT - II' in sec_str or 'UNIT II ' in sec_str:
            unit_num = 2
        elif 'UNIT-III' in sec_str or 'UNIT 3' in sec_str or 'UNIT - III' in sec_str or 'UNIT III ' in sec_str:
            unit_num = 3
        elif 'UNIT-IV' in sec_str or 'UNIT 4' in sec_str or 'UNIT - IV' in sec_str or 'UNIT IV ' in sec_str:
            unit_num = 4
        elif 'UNIT-V' in sec_str or 'UNIT 5' in sec_str or 'UNIT - V' in sec_str or 'UNIT V ' in sec_str:
            unit_num = 5
            
        categorized_sections.append((unit_num, sec))
    
    # 2. Sort the sections based on their identified Unit Number
    # Note: Chunks with no unit number (like intro/objectives) get 99 (pushed to end), 
    # but we should probably keep them at the start (Unit 0) if they are introductory.
    # Let's refine: if it's before Unit I, make it Unit 0.
    
    current_unit = 0
    final_sorted_sections = []
    
    for original_idx, (detected_unit, sec_data) in enumerate(categorized_sections):
        if detected_unit != 99:
            current_unit = detected_unit
        
        # If it didn't specifically say a unit, inherit the last seen unit so it stays grouped!
        # Introductory material before ANY unit is seen becomes Unit 0.
        assigned_unit = detected_unit if detected_unit != 99 else current_unit
        final_sorted_sections.append((assigned_unit, original_idx, sec_data))
        
    # Sort primarily by Unit Number (0, 1, 2, 3, 4, 5) and secondarily by original appearance order
    final_sorted_sections.sort(key=lambda x: (x[0], x[1]))
    
    # 3. Write back the perfectly sorted chapters
    data['sections'] = [item[2] for item in final_sorted_sections]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Sorted {len(data['sections'])} chunks sequentialy by Unit 1-5.")

if __name__ == "__main__":
    sort_book_structure()
