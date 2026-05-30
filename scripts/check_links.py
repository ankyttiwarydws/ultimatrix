import os
import re

base_dir = r"c:\Users\ankit\Documents\GitHub\ultimatrix"

broken_links = []
valid_links = 0

def resolve_path(current_file_path, href):
    if href.startswith('http://') or href.startswith('https://') or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'):
        return None # Skip external and special links
    
    # Strip query params or hash from href just in case
    href = href.split('#')[0].split('?')[0]
    
    if not href:
        return None

    if href.startswith('/'):
        # Absolute from root
        target_path = os.path.join(base_dir, href.lstrip('/'))
    else:
        # Relative
        current_dir = os.path.dirname(current_file_path)
        target_path = os.path.normpath(os.path.join(current_dir, href))
        
    return target_path

for root, dirs, files in os.walk(base_dir):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
                    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
                    
                    for link in hrefs + srcs:
                        target = resolve_path(filepath, link)
                        if target:
                            if not os.path.exists(target):
                                broken_links.append((filepath, link, target))
                            else:
                                valid_links += 1
            except Exception as e:
                print(f"Could not read {filepath}: {e}")

print(f"Checked {valid_links} valid internal links.")
if broken_links:
    print(f"Found {len(broken_links)} broken links:")
    for f, link, target in broken_links:
        print(f"File: {os.path.relpath(f, base_dir)} -> Broken Link: {link}")
else:
    print("No broken internal links found!")
