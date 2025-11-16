#!/usr/bin/env python3
"""
Link Validation Script for AI-900 Training Materials
Checks all markdown files for broken links (404s)
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
from collections import defaultdict

def find_markdown_files(root_dir):
    """Find all markdown files in the directory"""
    markdown_files = []
    for path in Path(root_dir).rglob("*.md"):
        # Skip node_modules and other common exclude directories
        if 'node_modules' not in str(path) and '.git' not in str(path):
            markdown_files.append(str(path))
    return markdown_files

def extract_links_from_markdown(file_path):
    """Extract all URLs from a markdown file"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Regex patterns for different link formats
    patterns = [
        r'\[.*?\]\((https?://[^\)]+)\)',  # Markdown links [text](url)
        r'https?://[^\s\)<>"]+',           # Plain URLs
    ]

    links = []
    for pattern in patterns:
        found_links = re.findall(pattern, content)
        links.extend(found_links)

    # Remove duplicates while preserving order
    seen = set()
    unique_links = []
    for link in links:
        # Clean up the link
        link = link.rstrip('.,;:)')
        if link not in seen:
            seen.add(link)
            unique_links.append(link)

    return unique_links

def check_url(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        # Add headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)

        # If HEAD fails, try GET (some servers don't support HEAD)
        if response.status_code == 405 or response.status_code == 404:
            response = requests.get(url, timeout=timeout, headers=headers, allow_redirects=True)

        return response.status_code, response.url
    except requests.exceptions.Timeout:
        return 'TIMEOUT', url
    except requests.exceptions.TooManyRedirects:
        return 'TOO_MANY_REDIRECTS', url
    except requests.exceptions.RequestException as e:
        return f'ERROR: {str(e)}', url
    except Exception as e:
        return f'EXCEPTION: {str(e)}', url

def validate_links(root_dir, delay=0.5):
    """Validate all links in markdown files"""
    print(f"🔍 Scanning for markdown files in: {root_dir}\n")

    markdown_files = find_markdown_files(root_dir)
    print(f"📄 Found {len(markdown_files)} markdown files\n")

    # Collect all links from all files
    file_links = {}
    all_links = set()

    for md_file in markdown_files:
        links = extract_links_from_markdown(md_file)
        if links:
            file_links[md_file] = links
            all_links.update(links)

    print(f"🔗 Found {len(all_links)} unique URLs to check\n")
    print("=" * 80)

    # Check each unique link
    results = {}
    broken_links = defaultdict(list)

    for i, url in enumerate(sorted(all_links), 1):
        print(f"[{i}/{len(all_links)}] Checking: {url[:80]}...")
        status, final_url = check_url(url)
        results[url] = (status, final_url)

        # Track broken links
        if isinstance(status, int):
            if status >= 400:
                for file_path, links in file_links.items():
                    if url in links:
                        broken_links[file_path].append((url, status, final_url))
        else:
            # Non-integer status means error
            for file_path, links in file_links.items():
                if url in links:
                    broken_links[file_path].append((url, status, final_url))

        # Be nice to servers
        time.sleep(delay)

    # Print summary
    print("\n" + "=" * 80)
    print("\n📊 VALIDATION SUMMARY\n")

    # Count by status
    status_counts = defaultdict(int)
    for status, _ in results.values():
        if isinstance(status, int):
            if status < 300:
                status_counts['✅ OK (2xx)'] += 1
            elif status < 400:
                status_counts['⚠️  Redirect (3xx)'] += 1
            elif status < 500:
                status_counts['❌ Client Error (4xx)'] += 1
            else:
                status_counts['❌ Server Error (5xx)'] += 1
        else:
            status_counts[f'❌ {status.split(":")[0]}'] += 1

    for status_type, count in sorted(status_counts.items()):
        print(f"{status_type}: {count}")

    # Print broken links by file
    if broken_links:
        print("\n" + "=" * 80)
        print("\n🔴 BROKEN LINKS BY FILE\n")

        for file_path, links in sorted(broken_links.items()):
            print(f"\n📄 {file_path}")
            for url, status, final_url in links:
                print(f"  ❌ [{status}] {url}")
                if url != final_url:
                    print(f"      → Redirects to: {final_url}")
    else:
        print("\n✅ No broken links found!")

    # Generate report file
    report_path = os.path.join(root_dir, 'link-validation-report.txt')
    with open(report_path, 'w') as f:
        f.write("AI-900 Link Validation Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total markdown files: {len(markdown_files)}\n")
        f.write(f"Total unique URLs: {len(all_links)}\n\n")

        f.write("Status Summary:\n")
        for status_type, count in sorted(status_counts.items()):
            f.write(f"  {status_type}: {count}\n")

        if broken_links:
            f.write("\n" + "=" * 80 + "\n")
            f.write("Broken Links by File:\n\n")
            for file_path, links in sorted(broken_links.items()):
                f.write(f"\n{file_path}\n")
                for url, status, final_url in links:
                    f.write(f"  [{status}] {url}\n")
                    if url != final_url:
                        f.write(f"    → {final_url}\n")

    print(f"\n📄 Full report saved to: {report_path}")

    return len(broken_links) == 0

if __name__ == "__main__":
    import sys

    # Get root directory from command line or use current directory
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "/home/user/ai900"

    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   AI-900 Link Validation Script                              ║
║                   Checking all markdown files for broken links               ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    all_good = validate_links(root_dir)

    if all_good:
        print("\n✅ All links are valid!")
        sys.exit(0)
    else:
        print("\n⚠️  Some links need attention. Please review the report above.")
        sys.exit(1)
