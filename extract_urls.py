#!/usr/bin/env python3
import sys
from PyPDF2 import PdfReader

def extract_urls_from_pdf(pdf_path):
    try:
        # Open the PDF file
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        sys.exit(1)

    urls = []
    
    # Iterate over each page
    for page in reader.pages:
        # Extract annotations (which include links)
        if '/Annots' in page:
            for annot in page['/Annots']:
                obj = annot.get_object()
                if obj.get('/Subtype') == '/Link' and '/A' in obj:
                    action = obj['/A']
                    if action.get('/S') == '/URI':
                        urls.append(action.get('/URI'))

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

