import json
import re
from src.resolver import resolve_art_tags

json_path = "data/output/book_structure.json"
print("Loading structure...")
try:
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    print("Failed to load JSON:", e)
    exit(1)

matches = 0
def process_node(node):
    global matches
    if isinstance(node, dict):
        if "text" in node and isinstance(node["text"], str):
            original = node["text"]
            if "NEW_DIAGRAM" in original:
                new_text = resolve_art_tags(original)
                if new_text != original:
                    node["text"] = new_text
                    matches += 1
        for v in node.values():
            process_node(v)
    elif isinstance(node, list):
        for item in node:
            process_node(item)

print("Starting recursive Art Department replacement across all AI chunks...")
process_node(data)
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("\nDONE: Patched JSON. Images replaced:", matches)
