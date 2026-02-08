#!/usr/bin/env python3
"""
Markdown to PDF Converter
支持中文的 Markdown 转 PDF 工具
"""

import markdown
from weasyprint import HTML, CSS
import os
import sys

def convert_md_to_pdf(md_file, pdf_file):
    """Convert Markdown file to PDF"""
    
    # 读取 Markdown 文件
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Markdown 转 HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.nl2br'
        ]
    )
    
    # 完整的 HTML 文档，带样式
    html_template = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>IBM iSeries 开发从入门到精通教程</title>
    <style>
        @page {{
            size: A4;
            margin: 2.5cm;
            @bottom-center {{
                content: counter(page);
                font-size: 10pt;
                color: #666;
            }}
        }}
        
        body {{
            font-family: "Noto Sans CJK SC", "WenQuanYi Micro Hei", "Source Han Sans CN", 
                         "Microsoft YaHei", "SimHei", sans-serif;
            font-size: 11pt;
            line-height: 1.8;
            color: #333;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }}
        
        h1 {{
            font-size: 24pt;
            color: #1a1a1a;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
            margin-top: 30px;
            page-break-before: always;
        }}
        
        h1:first-of-type {{
            page-break-before: avoid;
        }}
        
        h2 {{
            font-size: 18pt;
            color: #2a2a2a;
            border-left: 5px solid #0066cc;
            padding-left: 15px;
            margin-top: 25px;
        }}
        
        h3 {{
            font-size: 14pt;
            color: #333;
            margin-top: 20px;
        }}
        
        h4 {{
            font-size: 12pt;
            color: #444;
        }}
        
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
        
        code {{
            background-color: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            font-size: 10pt;
            color: #c7254e;
        }}
        
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #e1e1e8;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            font-size: 9pt;
            line-height: 1.5;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
            color: #333;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            font-size: 10pt;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #0066cc;
            color: white;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        blockquote {{
            border-left: 4px solid #0066cc;
            margin: 15px 0;
            padding: 10px 20px;
            background-color: #f9f9f9;
            color: #555;
        }}
        
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 5px 0;
        }}
        
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ddd;
            margin: 30px 0;
        }}
        
        .toc {{
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
        
        /* 打印优化 */
        @media print {{
            body {{
                font-size: 10pt;
            }}
            
            pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
                font-size: 8pt;
            }}
            
            h1 {{
                page-break-before: always;
            }}
            
            h1:first-of-type {{
                page-break-before: avoid;
            }}
            
            tr {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>'''
    
    # 保存临时 HTML 文件（用于调试）
    html_file = pdf_file.replace('.pdf', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"HTML file saved: {html_file}")
    
    # HTML 转 PDF
    try:
        HTML(string=html_template).write_pdf(pdf_file)
        print(f"PDF file saved: {pdf_file}")
        
        # 获取文件大小
        pdf_size = os.path.getsize(pdf_file)
        print(f"PDF size: {pdf_size / 1024:.1f} KB")
        
        return True
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        md_file = '/root/openclaw/IBM_iSeries_开发从入门到精通教程.md'
        pdf_file = '/root/openclaw/IBM_iSeries_开发从入门到精通教程.pdf'
    else:
        md_file = sys.argv[1]
        pdf_file = sys.argv[2] if len(sys.argv) > 2 else md_file.replace('.md', '.pdf')
    
    print(f"Converting: {md_file}")
    print(f"Output: {pdf_file}")
    print("-" * 50)
    
    success = convert_md_to_pdf(md_file, pdf_file)
    
    if success:
        print("-" * 50)
        print("Conversion completed successfully!")
    else:
        print("-" * 50)
        print("Conversion failed!")
        sys.exit(1)
