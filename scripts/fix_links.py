import os
import re

blogs_dir = r"c:\Users\ankit\Documents\GitHub\ultimatrix\blogs"

def fix_links():
    for root, dirs, files in os.walk(blogs_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Fix .md extensions to .html in href attributes
                    new_content = re.sub(r'href=["\']([^"\']+)\.md["\']', r'href="\1.html"', content)
                    
                    # Fix image links (../../assets -> /assets)
                    new_content = re.sub(r'src=["\']\.\./\.\./assets/([^"\']+)["\']', r'src="/assets/\1"', new_content)

                    # Specific link name fixes
                    new_content = new_content.replace('risk-section-C1-beginners.html', 'C1-risk-management-beginners.html')
                    new_content = new_content.replace('risk-management-2-percent-rule.html', 'C1-risk-management-beginners.html')

                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed links in {file}")
                        
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    fix_links()
