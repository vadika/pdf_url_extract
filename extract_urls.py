#/usr/bin/env python3
import fitz  # PyMuPDF
import sys

def extract_urls_from_pdf(pdf_path):
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        sys.exit(1)

    urls = []
    
    # Iterate over each page
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        links = page.get_links()

        # Extract URLs from the links
        for link in links:
            if 'uri' in link:
                urls.append(link['uri'])

    return urls

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_urls.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    urls = extract_urls_from_pdf(pdf_path)
    print("Extracted URLs:")
    for url in urls:
        print(url)

