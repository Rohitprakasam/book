import re

text1 = '[NEW_DIAGRAM: {"caption": "c1", "subject": "s1"}]'
text2 = 'NEW_DIAGRAM: {"caption": "c2", "subject": "s2"}'
text3 = '[NEW_DIAGRAM: plain text sub]'

pattern_json_tag = r'\[?NEW_DIAGRAM:\s*(\{.*?\})\]?'
pattern_text_tag = r'\[NEW_DIAGRAM:\s*([^{].*?)\]'

print("Test 1 JSON:", bool(re.search(pattern_json_tag, text1, re.DOTALL)))
print("Test 2 JSON:", bool(re.search(pattern_json_tag, text2, re.DOTALL)))
print("Test 3 TEXT:", bool(re.search(pattern_text_tag, text3, re.DOTALL)))
