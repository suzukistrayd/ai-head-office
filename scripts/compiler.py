import os
import markdown
import pdfkit  # Requires wkhtmltopdf installed locally for PDF generation

MANUSCRIPT_DIR = "manuscript/"
OUTPUT_DIR = "output/"

def compile_book_manuscript():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    full_html = "<html><head><style>body { font-family: Georgia, serif; line-height: 1.6; margin: 40px; }</style></head><body>"
    full_html += "<h1>SECRET SERVICE: Backstage with Martin Strayd</h1><h2>Volume 1</h2><hr>"

    # Read all markdown files in order
    if os.path.exists(MANUSCRIPT_DIR):
        files = sorted(os.listdir(MANUSCRIPT_DIR))
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(MANUSCRIPT_DIR, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                    html_content = markdown.markdown(md_content)
                    full_html += f"<div style='page-break-after: always;'>{html_content}</div><hr>"

    full_html += "</body></html>"

    output_html_path = os.path.join(OUTPUT_DIR, "secret-service-vol1.html")
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Manuscript successfully compiled to HTML: {output_html_path}")
    print("You can open this HTML file in Word, Calibre, or Kindle Create to generate your Amazon EPUB/PDF instantly!")

if __name__ == "__main__":
    compile_book_manuscript()
