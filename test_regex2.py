import json
import re

json_path = "data/output/book_structure.json"
data = json.loads(open(json_path, encoding="utf-8").read())

pattern_tag = r'\[NEW_DIAGRAM:\s*(\{.*?\})\s*\]'
matches = 0

def process_node(node):
    global matches
    if isinstance(node, dict):
        if "text" in node:
            text = node["text"]
            found = list(re.finditer(pattern_tag, text, re.DOTALL))
            matches += len(found)
        for v in node.values():
            process_node(v)
    elif isinstance(node, list):
        for item in node:
            process_node(item)

process_node(data)
print("Regex matches found:", matches)
