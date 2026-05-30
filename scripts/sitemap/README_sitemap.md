# Sitemap Generator for Ultimatrix.co.in

This collection of scripts automatically generates `sitemap.xml` for your website by scanning the directory structure and finding all HTML files.

## Quick Start (Easiest Method)

### Windows Users:
1. Double-click `update_sitemap.bat`
2. The script will generate `sitemap.xml` automatically

### All Users:
```bash
python generate_sitemap_simple.py
```

## Files Included

### 1. `generate_sitemap_simple.py` ⭐ (Recommended)
- **Simple, one-click solution**
- No configuration needed
- Just run and get your sitemap.xml
- Perfect for regular updates

### 2. `generate_sitemap.py` (Advanced)
- Full-featured version with command-line options
- Customizable priorities and change frequencies
- Can scan different directories
- Supports custom domains

### 3. `sitemap_config.py`
- Configuration file for the advanced version
- Customize priorities, change frequencies, and exclusions
- Easy to modify for your needs

### 4. `update_sitemap.bat`
- Windows batch file for one-click generation
- Double-click to run

## Usage Examples

### Basic Usage (Simple Version)
```bash
python generate_sitemap_simple.py
```

### Advanced Usage
```bash
# Generate with default settings
python generate_sitemap.py

# Custom domain and output file
python generate_sitemap.py --domain https://yourdomain.com --output my_sitemap.xml

# Scan different directory
python generate_sitemap.py --directory /path/to/website

# Show summary without generating file
python generate_sitemap.py --summary
```

## What Gets Included

### ✅ Included Files:
- All `.html` files in your directory structure
- Proper priority based on page importance
- Change frequency based on content type
- Last modification date (current date)

### ❌ Excluded Files:
- CSS, JS, and other non-HTML files
- System files (.DS_Store, etc.)
- Development directories (_next/, node_modules/, etc.)
- 404 error pages

## Priority System

| Priority | Page Types | Examples |
|----------|------------|----------|
| 1.0 | Homepage | `/`, `/index.html` |
| 0.9 | Main sections | `/games/games.html`, `/news/news.html` |
| 0.8 | Important pages | `/about-us.html`, `/contact-us.html` |
| 0.7 | Games & Tools | `/games/snake.html`, `/tools/calculator.html` |
| 0.6 | News & Sports | `/news/news1.html`, `/sports/sports1.html` |
| 0.5 | Blog posts | `/blogs/tech/ai-guide.html` |

## Change Frequency

| Frequency | Page Types |
|-----------|------------|
| Daily | Homepage, News, Sports main pages |
| Weekly | Games, Tools, Blog categories |
| Monthly | Individual games, tools, blog posts |
| Yearly | Privacy policy, static pages |

## Customization

### Simple Version
Edit the rules directly in `generate_sitemap_simple.py`:
- Modify `get_priority()` function for custom priorities
- Modify `get_changefreq()` function for custom frequencies
- Update `exclude_*` variables to change what gets excluded

### Advanced Version
Edit `sitemap_config.py`:
```python
# Change domain
DOMAIN = "https://yourdomain.com"

# Add custom priorities
PRIORITY_MAP = {
    'special-page.html': 0.9,
    'important/section.html': 0.8,
}

# Add exclusions
EXCLUDE_PATTERNS.add('temp/')
```

## Automation

### Schedule Regular Updates (Windows)
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily/weekly)
4. Set action to run `update_sitemap.bat`

### Schedule Regular Updates (Linux/Mac)
Add to crontab:
```bash
# Update sitemap daily at 2 AM
0 2 * * * cd /path/to/website && python generate_sitemap_simple.py
```

## Troubleshooting

### Common Issues:

**"No module named 'xml'"**
- This is a built-in Python module, ensure you're using Python 3.x

**"Permission denied"**
- Make sure you have write permissions in the directory
- Run as administrator if needed

**"No HTML files found"**
- Check you're running the script in the correct directory
- Verify HTML files exist and aren't in excluded directories

### Getting Help:
```bash
python generate_sitemap.py --help
```

## Output Example

```
✅ Sitemap generated successfully!
📄 Found 156 URLs
💾 Saved to: sitemap.xml

📊 Priority Distribution:
   Priority 1.0: 2 URLs
   Priority 0.9: 4 URLs
   Priority 0.8: 6 URLs
   Priority 0.7: 24 URLs
   Priority 0.6: 10 URLs
   Priority 0.5: 110 URLs
```

## SEO Benefits

- **Better Indexing**: Search engines can find all your pages
- **Faster Discovery**: New pages get indexed quicker
- **Priority Signals**: Tell search engines which pages are most important
- **Update Frequency**: Inform crawlers how often to check for changes

## Next Steps

1. Generate your sitemap: `python generate_sitemap_simple.py`
2. Upload `sitemap.xml` to your website root directory
3. Submit to Google Search Console
4. Add sitemap URL to your robots.txt:
   ```
   Sitemap: https://ultimatrix.co.in/sitemap.xml
   ```

---

**Pro Tip**: Run the generator whenever you add new pages to keep your sitemap current!