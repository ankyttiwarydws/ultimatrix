"""
Configuration file for sitemap generator
Customize these settings for your website
"""

# Website configuration
DOMAIN = "https://ultimatrix.co.in"
OUTPUT_FILE = "sitemap.xml"

# Priority mappings (higher = more important)
PRIORITY_MAP = {
    'index.html': 1.0,
    '/': 1.0,
    'games/games.html': 0.9,
    'news/news.html': 0.9,
    'blogs/blogs.html': 0.9,
    'tools/tools.html': 0.9,
    'sports/sports.html': 0.8,
    'about-us.html': 0.8,
    'contact-us.html': 0.8,
    'gta5.html': 0.8,
}

# Change frequency mappings
CHANGEFREQ_MAP = {
    'index.html': 'daily',
    '/': 'daily',
    'news/': 'daily',
    'sports/': 'daily',
    'blogs/blogs.html': 'daily',
    'games/': 'weekly',
    'tools/': 'weekly',
    'blogs/': 'weekly',
    'privacy.html': 'yearly',
}

# Files and patterns to exclude
EXCLUDE_PATTERNS = {
    '.DS_Store', 
    '*.css', 
    '*.js', 
    '*.txt', 
    '*.json',
    '*.md',
    '404.html', 
    '_next/', 
    'dist/', 
    'node_modules/',
    'blog-styles.css', 
    'blogs.css', 
    'header-footer.css',
    'related-articles-styles.css', 
    'style.css',
    '.git/',
    '__pycache__/',
    '.vscode/',
    '.idea/',
}

# Default priorities by section
DEFAULT_PRIORITIES = {
    'games/': 0.7,
    'tools/': 0.7,
    'news/': 0.6,
    'sports/': 0.6,
    'blogs/': 0.5,
}

# Default change frequencies by section
DEFAULT_CHANGEFREQ = {
    'news/': 'weekly',
    'sports/': 'weekly',
    'games/': 'monthly',
    'tools/': 'monthly',
    'blogs/': 'monthly',
}