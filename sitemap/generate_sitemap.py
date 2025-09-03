#!/usr/bin/env python3
"""
Sitemap Generator for Ultimatrix.co.in
Automatically generates sitemap.xml by scanning the directory structure
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
import argparse


class SitemapGenerator:
    def __init__(self, domain="https://ultimatrix.co.in", root_dir="."):
        self.domain = domain.rstrip('/')
        self.root_dir = Path(root_dir)
        self.current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Priority and change frequency mappings
        self.priority_map = {
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
        
        self.changefreq_map = {
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
        
        # Files to exclude from sitemap
        self.exclude_patterns = {
            '.DS_Store', '*.css', '*.js', '*.txt', '*.json', 
            '404.html', '_next/', 'dist/', 'node_modules/',
            'blog-styles.css', 'blogs.css', 'header-footer.css',
            'related-articles-styles.css', 'style.css'
        }

    def should_exclude(self, file_path):
        """Check if file should be excluded from sitemap"""
        file_name = file_path.name
        path_str = str(file_path)
        
        # Exclude specific patterns
        for pattern in self.exclude_patterns:
            if pattern in file_name or pattern in path_str:
                return True
                
        # Only include HTML files
        if not file_name.endswith('.html'):
            return True
            
        return False

    def get_priority(self, relative_path):
        """Get priority for a given path"""
        path_str = str(relative_path).replace('\\', '/')
        
        # Check exact matches first
        if path_str in self.priority_map:
            return self.priority_map[path_str]
            
        # Check for main section pages
        if path_str.endswith('/games.html') or path_str.endswith('/news.html') or path_str.endswith('/blogs.html'):
            return 0.9
        elif path_str.endswith('/tools.html') or path_str.endswith('/sports.html'):
            return 0.8
        elif 'games/' in path_str or 'tools/' in path_str:
            return 0.7
        elif 'news/' in path_str or 'sports/' in path_str:
            return 0.6
        elif 'blogs/' in path_str:
            return 0.5
        else:
            return 0.5

    def get_changefreq(self, relative_path):
        """Get change frequency for a given path"""
        path_str = str(relative_path).replace('\\', '/')
        
        # Check for specific patterns
        for pattern, freq in self.changefreq_map.items():
            if pattern in path_str:
                return freq
                
        # Default frequencies based on content type
        if 'news/' in path_str or 'sports/' in path_str:
            return 'weekly'
        elif 'games/' in path_str or 'tools/' in path_str:
            return 'monthly'
        elif 'blogs/' in path_str:
            return 'monthly'
        else:
            return 'monthly'

    def scan_directory(self):
        """Scan directory structure and collect HTML files"""
        html_files = []
        
        # Add root index
        html_files.append({
            'loc': f"{self.domain}/",
            'lastmod': self.current_date,
            'changefreq': 'daily',
            'priority': 1.0
        })
        
        # Scan for HTML files
        for file_path in self.root_dir.rglob('*.html'):
            if self.should_exclude(file_path):
                continue
                
            # Get relative path from root
            relative_path = file_path.relative_to(self.root_dir)
            url_path = str(relative_path).replace('\\', '/')
            
            # Skip if it's the root index.html (already added as /)
            if url_path == 'index.html':
                html_files.append({
                    'loc': f"{self.domain}/index.html",
                    'lastmod': self.current_date,
                    'changefreq': 'daily',
                    'priority': 1.0
                })
                continue
            
            html_files.append({
                'loc': f"{self.domain}/{url_path}",
                'lastmod': self.current_date,
                'changefreq': self.get_changefreq(relative_path),
                'priority': self.get_priority(relative_path)
            })
        
        return sorted(html_files, key=lambda x: (-x['priority'], x['loc']))

    def generate_xml(self, urls):
        """Generate XML sitemap content"""
        # Create root element
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        
        # Add URLs
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
        
        return urlset

    def format_xml(self, root):
        """Format XML with proper indentation"""
        def indent(elem, level=0):
            i = "\n" + level * "  "
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + "  "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i
        
        indent(root)
        return root

    def generate_sitemap(self, output_file='sitemap.xml'):
        """Main method to generate sitemap"""
        print(f"Scanning directory: {self.root_dir}")
        urls = self.scan_directory()
        print(f"Found {len(urls)} URLs")
        
        # Generate XML
        xml_root = self.generate_xml(urls)
        formatted_root = self.format_xml(xml_root)
        
        # Create XML tree and write to file
        tree = ET.ElementTree(formatted_root)
        
        # Write XML declaration and content
        with open(output_file, 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            tree.write(f, encoding='utf-8', xml_declaration=False)
        
        print(f"Sitemap generated: {output_file}")
        return output_file

    def print_summary(self):
        """Print summary of found URLs"""
        urls = self.scan_directory()
        
        print("\n=== SITEMAP SUMMARY ===")
        print(f"Total URLs: {len(urls)}")
        
        # Group by priority
        priority_groups = {}
        for url in urls:
            priority = url['priority']
            if priority not in priority_groups:
                priority_groups[priority] = []
            priority_groups[priority].append(url['loc'])
        
        for priority in sorted(priority_groups.keys(), reverse=True):
            print(f"\nPriority {priority}: {len(priority_groups[priority])} URLs")
            for url in priority_groups[priority][:5]:  # Show first 5
                print(f"  - {url}")
            if len(priority_groups[priority]) > 5:
                print(f"  ... and {len(priority_groups[priority]) - 5} more")


def main():
    parser = argparse.ArgumentParser(description='Generate sitemap.xml for Ultimatrix website')
    parser.add_argument('--domain', default='https://ultimatrix.co.in', 
                       help='Website domain (default: https://ultimatrix.co.in)')
    parser.add_argument('--output', default='sitemap.xml', 
                       help='Output file name (default: sitemap.xml)')
    parser.add_argument('--directory', default='.', 
                       help='Root directory to scan (default: current directory)')
    parser.add_argument('--summary', action='store_true', 
                       help='Show summary without generating file')
    
    args = parser.parse_args()
    
    generator = SitemapGenerator(domain=args.domain, root_dir=args.directory)
    
    if args.summary:
        generator.print_summary()
    else:
        generator.generate_sitemap(args.output)


if __name__ == '__main__':
    main()