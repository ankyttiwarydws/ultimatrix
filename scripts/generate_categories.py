import os
import re

blogs_dir = r"c:\Users\ankit\Documents\GitHub\ultimatrix\blogs"
content_file = r"c:\Users\ankit\Documents\GitHub\ultimatrix\ultimatrix-category-content.md"

categories = {
    "trading-basics": {
        "title": "Trading Basics",
        "files": ["what-is-trading.html", "trading-vs-investing.html", "types-of-trading-intro.html", "what-is-swing-trading.html", "intraday_trading_beginner_guide.html", "trading_tools_guide_india.html"]
    },
    "market-dynamics": {
        "title": "Market Dynamics",
        "files": ["market-series-part1-why-markets-move.html", "market-series-part2-global-markets.html", "market-series-part4-gift-nifty.html", "market-series-part5-evening-checklist.html", "market-series-part6-morning-routine.html"]
    },
    "options-trading": {
        "title": "Options Trading",
        "files": ["options-basics-part1.html", "options-basics-part2.html", "options_trading_oi_pcr_iv_vix_maxpain_explained.html"]
    },
    "risk-psychology": {
        "title": "Risk & Psychology",
        "files": ["risk-management.html", "C1-risk-management-beginners.html", "C2-risk-management-intermediate.html", "C3-risk-management-experienced.html", "risk-section-A1-what-risk-means.html", "risk-section-A3-position-sizing.html", "risk-section-A4-stop-losses.html", "risk-section-B1-options-blowup.html", "risk-section-B2-averaging-down.html", "risk-section-B3-revenge-trading.html", "risk-section-B4-telegram-tip.html", "trading-psychology.html"]
    },
    "age-strategies": {
        "title": "Age-Based Strategies",
        "files": ["D1-starting-first-job-investing-20s.html", "D2-starting-mid-30s-trading-investing.html", "D3-starting-40s-building-wealth.html", "D4-starting-50s-time-is-scarce.html", "D5-starting-after-retirement.html"]
    }
}

# Parse markdown
with open(content_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

cat_blocks = md_content.split('## CATEGORY')

category_data = {}
disclaimer_text = "Everything on Ultimatrix is for educational purposes only. Nothing here is financial advice, investment advice, or a recommendation to buy or sell any security. Trading and investing involve real risk — including the loss of capital. Please consult a registered financial advisor before making any investment decisions. Ultimatrix is not SEBI registered and does not manage money on anyone's behalf."

for block in cat_blocks[1:]:
    url_match = re.search(r'\*\*URL:\*\* (.*?\.html)', block)
    if url_match:
        url = url_match.group(1).strip()
        slug = url.replace('category-', '').replace('.html', '').strip()
        
        heading_match = re.search(r'### Heading:\n(.*?)\n', block)
        subheading_match = re.search(r'### Subheading.*?:\n(.*?)\n', block)
        body_match = re.search(r'### Body Content:\n(.*?)### Closing line:', block, re.DOTALL)
        closing_match = re.search(r'### Closing line:\n(.*?)\n', block)
        
        heading = heading_match.group(1).strip() if heading_match else ""
        subheading = subheading_match.group(1).strip() if subheading_match else ""
        closing_line = closing_match.group(1).strip() if closing_match else ""
        
        body_content = body_match.group(1).strip() if body_match else ""
        
        html_body = []
        for p in body_content.split(r'\n\n'):
            # Also handle simple splits
            for sub_p in p.split('\n\n'):
                sub_p = sub_p.strip()
                if not sub_p: continue
                if sub_p.startswith('### What you will find in this section:'):
                    html_body.append(f'<h3 style="color: var(--color-text-primary); margin-top: 2rem; margin-bottom: 1rem;">What you will find in this section:</h3>')
                elif sub_p.startswith('- '):
                    items = sub_p.split('\n')
                    html_body.append('<ul style="margin-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.8;">')
                    for item in items:
                        if item.startswith('- '):
                            html_body.append(f'<li style="margin-bottom: 0.5rem;">{item[2:]}</li>')
                    html_body.append('</ul>')
                else:
                    html_body.append(f'<p style="margin-bottom: 1.25rem;">{sub_p}</p>')
        
        body_content_html = '\n'.join(html_body)
        
        category_data[slug] = {
            'heading': heading,
            'subheading': subheading,
            'body_content_html': body_content_html,
            'closing_line': closing_line
        }

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{heading} | Ultimatrix</title>
  <link rel="icon" type="image/png" href="/assets/img/favicon.png" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="stylesheet" href="/css/header-footer.css" />
  <link rel="stylesheet" href="/css/blogs.css" />
  <link rel="stylesheet" href="/css/home.css" />
  <script src="/js/script.js" defer></script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9364127030923496" crossorigin="anonymous"></script>
</head>
<body>
  <div id="header"></div>
  <main>
    <div class="section" style="padding-top: 4rem;">
      <div class="section-label">Category</div>
      <h1 class="section-title">{heading}</h1>
      <div class="section-sub">{subheading}</div>
      
      <div style="font-size: 1.05rem; color: var(--color-text-secondary); line-height: 1.7; margin-bottom: 3rem;">
        {body_content_html}
      </div>

      <h3 style="margin-bottom: 1rem; color: var(--color-text-primary);">Articles in this category:</h3>
      <div class="article-list">
        {cards_html}
      </div>
      
      <div style="margin-top: 3rem; font-weight: 500; color: #1D9E75; font-size: 1.1rem; text-align: center; padding: 2rem; background: rgba(29, 158, 117, 0.1); border-radius: 12px;">
        {closing_line}
      </div>
    </div>

    <!-- Bottom navigation prompt -->
    <div class="start-bar">
       <div class="start-icon"><i class="ti ti-map" style="color:#1D9E75; font-size:28px;" aria-hidden="true"></i></div>
       <div style="flex:1; min-width: 250px;">
         <h3 style="color: var(--color-text-primary); margin-bottom: 4px;">Not in the right place?</h3>
         <p style="color: var(--color-text-secondary); margin-bottom: 0;">Browse all categories or go back to the homepage to find what you are looking for.</p>
       </div>
       <div style="display:flex; gap: 10px; flex-wrap: wrap;">
         <a href="/index.html#categories-section" class="btn-primary" style="text-decoration:none;">All Categories</a>
         <a href="/index.html" class="btn-secondary" style="text-decoration:none;">Homepage</a>
       </div>
    </div>

    <!-- Disclaimer -->
    <div class="disclaimer">
       <div class="disclaimer-title"><i class="ti ti-info-circle" aria-hidden="true" style="font-size:13px; margin-right:4px;"></i>Disclaimer</div>
       <p>{disclaimer_text}</p>
    </div>
  </main>
  <div id="footer"></div>
</body>
</html>
"""

card_template = """
        <div class="article-item" onclick="window.location.href='/blogs/{filename}'">
          <div class="article-meta">
            <h4>{blog_title}</h4>
          </div>
          <div class="article-arrow"><i class="ti ti-arrow-right" aria-hidden="true"></i></div>
        </div>"""

def get_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if match:
                title = match.group(1).replace(' | Ultimatrix', '').strip()
                return title
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return "Untitled Document"


for cat_slug, cat_info in categories.items():
    if cat_slug not in category_data:
        print(f"No content found for {cat_slug}")
        continue
        
    cards = []
    for file in cat_info["files"]:
        filepath = os.path.join(blogs_dir, file)
        blog_title = get_title(filepath)
        cards.append(card_template.format(filename=file, blog_title=blog_title))
    
    data = category_data[cat_slug]
    html_content = template.format(
        heading=data['heading'],
        subheading=data['subheading'],
        body_content_html=data['body_content_html'],
        closing_line=data['closing_line'],
        cards_html="".join(cards),
        disclaimer_text=disclaimer_text
    )
    
    out_path = os.path.join(blogs_dir, f"category-{cat_slug}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Created {out_path}")
