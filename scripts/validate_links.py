import os
import re
import urllib.parse

def check_links():
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Find all links in the format [Text](Path)
    links = re.findall(r'\[.*?\]\(([^)]+)\)', content)
    
    broken_links = []
    for link in links:
        if link.startswith('http'):
            continue
        
        # Unquote the link to get the actual path
        unquoted_path = urllib.parse.unquote(link)
        
        # Remove leading ./
        clean_path = unquoted_path.lstrip('./')
        
        if not os.path.exists(clean_path):
            broken_links.append((link, unquoted_path))
            
    return broken_links

if __name__ == "__main__":
    broken = check_links()
    if broken:
        print(f"Found {len(broken)} broken links:")
        for raw, clean in broken:
            print(f"Broken: {raw} -> {clean}")
    else:
        print("No broken links found!")
