#!/usr/bin/env python3
import markdown
from weasyprint import HTML, CSS
import os

# Read the markdown file
input_file = "/workspaces/Idexx-notes/Idexx/IDEXX_MASTER_MANUAL_FOR_PDF.md"
output_file = "/workspaces/Idexx-notes/Idexx/IDEXX_MASTER_MANUAL.pdf"

# Read markdown content
with open(input_file, 'r') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'extra', 'toc'])

# Add CSS styling for professional PDF
css_string = """
<style>
body {
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    color: #1a5490;
    border-bottom: 3px solid #1a5490;
    padding-bottom: 10px;
    margin-top: 0;
    page-break-after: avoid;
    font-size: 28px;
}

h2 {
    color: #2a5aa0;
    border-left: 4px solid #2a5aa0;
    padding-left: 10px;
    margin-top: 30px;
    page-break-after: avoid;
    font-size: 24px;
}

h3 {
    color: #3a6ab0;
    margin-top: 20px;
    page-break-after: avoid;
    font-size: 18px;
}

h4, h5, h6 {
    color: #4a7ac0;
    page-break-after: avoid;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    page-break-inside: avoid;
}

th {
    background-color: #2a5aa0;
    color: white;
    padding: 10px;
    text-align: left;
    font-weight: bold;
}

td {
    border: 1px solid #ddd;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #f0f0f0;
}

code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
}

pre {
    background-color: #f4f4f4;
    padding: 12px;
    border-radius: 4px;
    overflow-x: auto;
    page-break-inside: avoid;
}

blockquote {
    border-left: 4px solid #2a5aa0;
    padding-left: 15px;
    margin-left: 0;
    color: #666;
    font-style: italic;
}

ul, ol {
    margin: 15px 0;
    padding-left: 30px;
}

li {
    margin: 5px 0;
}

a {
    color: #1a5490;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.toc {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 4px;
    margin: 20px 0;
    page-break-inside: avoid;
}

.toc ul {
    list-style-type: none;
    padding-left: 0;
}

.toc li {
    margin: 5px 0;
    padding-left: 20px;
}

.toc > ul > li {
    padding-left: 0;
}

strong {
    color: #1a5490;
    font-weight: 600;
}

em {
    color: #555;
}

hr {
    border: none;
    border-top: 2px solid #2a5aa0;
    margin: 30px 0;
    page-break-after: avoid;
}

p {
    margin: 10px 0;
    text-align: justify;
}

@page {
    margin: 1in;
    size: letter;
}

@page :first {
    margin-top: 1.5in;
}
</style>
"""

# Combine CSS and HTML
full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>IDEXX Credit Specialist Complete Reference Manual</title>
    {css_string}
</head>
<body>
{html_content}
</body>
</html>"""

# Generate PDF
try:
    HTML(string=full_html).write_pdf(output_file)
    print(f"✓ PDF created successfully: {output_file}")
    print(f"✓ File size: {os.path.getsize(output_file) / 1024:.1f} KB")
except Exception as e:
    print(f"✗ Error creating PDF: {e}")
