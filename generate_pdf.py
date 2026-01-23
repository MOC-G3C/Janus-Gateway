import markdown
from xhtml2pdf import pisa
import os

# Configuration for MOC-G3C Governance
def convert_md_to_pdf(source_file, output_file):
    # 1. Read the Markdown file
    with open(source_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 2. Convert Markdown to HTML
    html_content = markdown.markdown(content, extensions=['extra', 'smarty'])
    
    # 3. Add basic styling for a professional look
    styled_html = f"""
    <html>
        <head><style>
            body {{ font-family: Helvetica, Arial, sans-serif; line-height: 1.5; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; }}
            h2 {{ color: #2980b9; margin-top: 20px; }}
            pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; }}
            blockquote {{ border-left: 5px solid #ccc; padding-left: 10px; font-style: italic; }}
        </style></head>
        <body>{html_content}</body>
    </html>
    """

    # 4. Generate the PDF
    with open(output_file, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(styled_html, dest=result_file)
    
    return pisa_status.err

# Automatic processing for active project files
files_to_convert = [
    "DEVIS_TEMPLATE.md",
    "CHECKLIST_LIVRAISON.md",
    "SAFETY_LIFTING_CHECKLIST.md"
]

for md_file in files_to_convert:
    if os.path.exists(md_file):
        pdf_name = md_file.replace(".md", ".pdf")
        print(f"Generating {pdf_name}...")
        convert_md_to_pdf(md_file, pdf_name)

print("\n[SUCCESS] All documents updated according to Protocol Lambda v1.1.")
