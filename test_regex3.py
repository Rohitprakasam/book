import json
import re

json_path = "data/output/book_structure.json"
data = json.loads(open(json_path, encoding="utf-8").read())

matches = 0
def process_node(node):
    global matches
    if isinstance(node, dict):
        if "text" in node and isinstance(node["text"], str):
            original = node["text"]
            if "NEW_DIAGRAM" in original:
                print("LITERAL STRING:", repr(original))
                matches += 1
                if matches >= 3:
                    exit(0)
        for v in node.values():
            process_node(v)
    elif isinstance(node, list):
        for item in node:
            process_node(item)

process_node(data)
