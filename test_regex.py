import json
import re

txt = '[NEW_DIAGRAM: {"caption": "test", "subject": "test", "type": "test"}]'
pattern_tag = r'\[NEW_DIAGRAM:\s*(\{.*?\})\s*\]'

matches = list(re.finditer(pattern_tag, txt, re.DOTALL))
print("Matches found:", len(matches))
if matches:
    print(matches[0].groups())
