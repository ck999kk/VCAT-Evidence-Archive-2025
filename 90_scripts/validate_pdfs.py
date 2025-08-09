#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
import PyPDF2

def check_pdf_readability(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            page_count = len(reader.pages)
            
            # Check if PDF has text content
            text_content = ""
            for page in reader.pages[:3]:  # Check first 3 pages
                text_content += page.extract_text()
            
            has_text = len(text_content.strip()) > 10
            return True, page_count, has_text
    except Exception as e:
        return False, 0, False

def main():
    errors = []
    pdf_files = list(Path("VCAT_SUBMISSION_PACKAGE").glob("**/*.pdf"))
    pdf_files += list(Path("VCAT_NON_GMAIL_EVIDENCE").glob("**/*.pdf"))
    
    for pdf in pdf_files:
        readable, pages, has_text = check_pdf_readability(pdf)
        
        if not readable:
            errors.append(f"CORRUPTED: {pdf}")
        elif not has_text:
            errors.append(f"NO_TEXT_CONTENT: {pdf}")
        else:
            print(f"✓ {pdf} ({pages} pages, text content: OK)")
    
    if errors:
        print("\nERRORS FOUND:")
        for error in errors:
            print(error)
        sys.exit(1)
    
    print(f"\n✅ All {len(pdf_files)} PDFs validated successfully")

if __name__ == "__main__":
    main()