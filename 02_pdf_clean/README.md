# Folder Policy — /02_pdf_clean

## Purpose
เก็บไฟล์ที่ผ่านการประมวลผลแล้ว (Processed PDFs)

## Processing Standards
- PDF/A-2b compliance
- OCR 100% complete
- Searchable text content
- Optimized for court submission

## Allowed Operations
- OCR processing from /01_sources
- PDF/A conversion
- File optimization
- Metadata sanitization

## Naming Convention
- Original_Name_YYYYMMDD_processed.pdf
- Maintain traceability to source files

## Quality Requirements
- All files must pass CI validation
- SHA-256 checksums recorded
- Processing logs maintained

## Claude & Gemini Rules
- Always verify source file exists in /01_sources
- Record processing commands and parameters
- Generate integrity manifest entry
- Never modify source files directly