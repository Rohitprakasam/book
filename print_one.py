import json
import re

json_path = "data/output/book_structure.json"
data = json.loads(open(json_path, encoding="utf-8").read())
with open("test.txt", "w", encoding="utf-8") as f:
    def process_node(node):
        if isinstance(node, dict):
            if "text" in node and isinstance(node["text"], str):
                if "NEW_DIAGRAM" in node["text"]:
                    f.write(repr(node["text"]) + "\n\n")
            for v in node.values():
                process_node(v)
        elif isinstance(node, list):
            for item in node:
                process_node(item)

    process_node(data)
