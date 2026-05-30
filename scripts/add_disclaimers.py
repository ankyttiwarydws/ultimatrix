import os
import re

blogs_dir = r"c:\Users\ankit\Documents\GitHub\ultimatrix\blogs"
disclaimer_html = """
        <div style="margin-bottom: 2rem; padding: 1rem 1.25rem; background: var(--color-background-secondary, #f9fafb); border-radius: 8px; border-left: 3px solid #888780;">
           <div style="display: flex; align-items: center; font-size: 12px; font-weight: 600; color: var(--color-text-secondary, #4b5563); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">
             <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
             Disclaimer
           </div>
           <p style="font-size: 12px; color: var(--color-text-tertiary, #6b7280); line-height: 1.6; margin-bottom: 0;">Everything on Ultimatrix is for educational purposes only. Nothing here is financial advice, investment advice, or a recommendation to buy or sell any security. Trading and investing involve real risk — including the loss of capital. Please consult a registered financial advisor before making any investment decisions. Ultimatrix is not SEBI registered and does not manage money on anyone's behalf.</p>
        </div>
"""

for file in os.listdir(blogs_dir):
    if file.endswith('.html') and not file.startswith('category-'):
        filepath = os.path.join(blogs_dir, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if "Everything on Ultimatrix is for educational purposes only" in content and "Disclaimer" in content:
                print(f"Skipping {file} (disclaimer already exists)")
                continue
                
            div_match = re.search(r'(<div class="howto-tab-content markdown-content"[^>]*>)', content)
            if div_match:
                div_tag = div_match.group(1)
                new_content = content.replace(div_tag, div_tag + disclaimer_html)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Added disclaimer to {file}")
            else:
                print(f"Could not find markdown-content div in {file}")
                
        except Exception as e:
            print(f"Error processing {file}: {e}")
