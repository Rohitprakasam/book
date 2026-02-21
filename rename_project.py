import os
import re

dirs_to_process = [
    r"c:\Users\rohit\OneDrive\Desktop\Book_Creator\bookeducate_local",
    r"C:\Users\rohit\.gemini\antigravity\brain\2d65560b-b107-4bb7-8164-2a740dcad568"
]

allowed_exts = {'.py', '.md', '.json', '.latex', '.txt', '.cls', '.env', '.example', '', '.resolved'}

ignore_dirs = {'.git', '__pycache__', 'venv', 'chroma_db', 'assets', '.pytest_cache'}

def replace_in_string(text):
    text = re.sub(r'BookEducate', 'BookEducate', text)
    text = re.sub(r'bookeducate', 'bookeducate', text)
    text = re.sub(r'BOOKEDUCATE', 'BOOKEDUCATE', text)
    return text

for dir_path in dirs_to_process:
    for root, dirs, files in os.walk(dir_path, topdown=False):
        path_parts = root.replace('\\', '/').split('/')
        if any(ignored in path_parts for ignored in ignore_dirs):
            continue
            
        for name in files:
            file_path = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()
            if ext in allowed_exts or name.startswith('.env') or name == 'README.md':
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = replace_in_string(content)
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                except Exception as e:
                    pass
            
            # Rename file
            new_name = replace_in_string(name)
            if new_name != name:
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(file_path, new_path)
                except:
                    pass
                
        for name in dirs:
            dir_path_iter = os.path.join(root, name)
            new_name = replace_in_string(name)
            if new_name != name:
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(dir_path_iter, new_path)
                except:
                    pass

print("Done resetting project name.")
