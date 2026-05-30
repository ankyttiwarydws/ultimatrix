import os
import markdown

template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Ultimatrix</title>
  <link rel="icon" type="image/png" href="/assets/img/favicon.png" />
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="stylesheet" href="/css/blogs.css" />
  <link rel="stylesheet" href="/css/header-footer.css" />
  <script src="/js/script.js" defer></script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9364127030923496" crossorigin="anonymous"></script>
  <style>
    .markdown-content h2 {{ margin-top: 1.5em; margin-bottom: 0.8em; font-size: 1.5em; }}
    .markdown-content h3 {{ margin-top: 1.2em; margin-bottom: 0.5em; font-size: 1.2em; }}
    .markdown-content p {{ line-height: 1.7; margin-bottom: 1.2em; }}
    .markdown-content ul, .markdown-content ol {{ margin-left: 2em; margin-bottom: 1.2em; line-height: 1.7; }}
    .markdown-content li {{ margin-bottom: 0.5em; }}
    .markdown-content a {{ color: #4DA8DA; text-decoration: none; }}
    .markdown-content a:hover {{ text-decoration: underline; }}
    .markdown-content strong {{ font-weight: bold; }}
    .markdown-content hr {{ border: 0; border-top: 1px solid #ccc; margin: 2em 0; }}
  </style>
</head>
<body>
  <div id="header"></div>
  <main>
    <section class="blogs-main-category">
      <h3>{title}</h3>
    </section>
    <section>
      <div class="howto-tab-content markdown-content" style="display:block; padding: 2em; max-width: 900px; margin: 0 auto; text-align: left;">
        {content}
      </div>
    </section>
  </main>
  <div id="footer"></div>
</body>
</html>'''

md_dir = 'c:/Users/ankit/Documents/GitHub/ultimatrix/blogs/a'
html_dir = os.path.join(md_dir, 'html')
os.makedirs(html_dir, exist_ok=True)

for file in os.listdir(md_dir):
    if file.endswith('.md'):
        with open(os.path.join(md_dir, file), 'r', encoding='utf-8') as f:
            text = f.read()
        
        # parse title
        title = file.replace('.md', '').replace('-', ' ').title()
        if text.startswith('# '):
            first_line = text.split('\n')[0]
            title = first_line.replace('# ', '').strip()
            # remove title from body to avoid duplication
            text = text[len(first_line):]

        html_content = markdown.markdown(text)
        
        final_html = template.format(title=title, content=html_content)
        
        out_name = file.replace('.md', '.html')
        with open(os.path.join(html_dir, out_name), 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f'Converted {file} to {out_name}')
