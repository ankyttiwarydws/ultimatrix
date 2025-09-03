#!/usr/bin/env python3
"""
Simple Sitemap Generator - Easy to use version
Just run this script to generate sitemap.xml
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def generate_sitemap():
    """Generate sitemap.xml for the current directory"""
    
    domain = "https://ultimatrix.co.in"
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Files to exclude
    exclude_files = {'.DS_Store', '404.html'}
    exclude_extensions = {'.css', '.js', '.txt', '.json', '.md', '.py'}
    exclude_dirs = {'_next', 'dist', 'node_modules', '.git', '__pycache__', '.vscode'}
    
    # Priority rules
    def get_priority(path):
        if path in ['/', '/index.html']:
            return 1.0
        elif any(x in path for x in ['/games.html', '/news.html', '/blogs.html', '/tools.html']):
            return 0.9
        elif any(x in path for x in ['/sports.html', '/about-us.html', '/contact-us.html']):
            return 0.8
        elif '/games/' in path or '/tools/' in path:
            return 0.7
        elif '/news/' in path or '/sports/' in path:
            return 0.6
        elif '/blogs/' in path:
            return 0.5
        else:
            return 0.5
    
    # Change frequency rules
    def get_changefreq(path):
        if path in ['/', '/index.html'] or '/news/' in path or '/sports/' in path:
            return 'daily'
        elif '/games/' in path or '/tools/' in path or '/blogs.html' in path:
            return 'weekly'
        elif 'privacy.html' in path:
            return 'yearly'
        else:
            return 'monthly'
    
    # Collect HTML files
    urls = []
    root_dir = Path('.')
    
    # Add root URL
    urls.append({
        'loc': domain + '/',
        'lastmod': current_date,
        'changefreq': 'daily',
        'priority': 1.0
    })
    
    # Scan for HTML files
    for html_file in root_dir.rglob('*.html'):
        # Skip excluded files and directories
        if any(exclude_dir in str(html_file) for exclude_dir in exclude_dirs):
            continue
        if html_file.name in exclude_files:
            continue
        if html_file.suffix in exclude_extensions:
            continue
            
        # Get relative path
        rel_path = html_file.relative_to(root_dir)
        url_path = '/' + str(rel_path).replace('\\', '/')
        
        # Skip root index.html (already added as /)
        if url_path == '/index.html':
            urls.append({
                'loc': domain + '/index.html',
                'lastmod': current_date,
                'changefreq': 'daily',
                'priority': 1.0
            })
            continue
        
        urls.append({
            'loc': domain + url_path,
            'lastmod': current_date,
            'changefreq': get_changefreq(url_path),
            'priority': get_priority(url_path)
        })
    
    # Sort by priority (highest first), then by URL
    urls.sort(key=lambda x: (-x['priority'], x['loc']))
    
    # Generate XML
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    for url_data in urls:
        url_elem = ET.SubElement(urlset, 'url')
        
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = url_data['loc']
        
        lastmod_elem = ET.SubElement(url_elem, 'lastmod')
        lastmod_elem.text = url_data['lastmod']
        
        changefreq_elem = ET.SubElement(url_elem, 'changefreq')
        changefreq_elem.text = url_data['changefreq']
        
        priority_elem = ET.SubElement(url_elem, 'priority')
        priority_elem.text = str(url_data['priority'])
    
    # Format XML with indentation
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for child in elem:
                indent(child, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    indent(urlset)
    
    # Write to file
    with open('sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        ET.ElementTree(urlset).write(f, encoding='utf-8', xml_declaration=False)
    
    print(f"✅ Sitemap generated successfully!")
    print(f"📄 Found {len(urls)} URLs")
    print(f"💾 Saved to: sitemap.xml")
    
    # Show summary
    priority_counts = {}
    for url in urls:
        p = url['priority']
        priority_counts[p] = priority_counts.get(p, 0) + 1
    
    print("\n📊 Priority Distribution:")
    for priority in sorted(priority_counts.keys(), reverse=True):
        count = priority_counts[priority]
        print(f"   Priority {priority}: {count} URLs")

if __name__ == '__main__':
    generate_sitemap()