# Folder Policy — /01_sources

## Purpose
เก็บไฟล์ต้นฉบับ (Immutable Originals)

## DO
- เก็บเฉพาะไฟล์ดิบ/สแกนจากแหล่งที่มา
- บันทึก hash และ metadata ทันที

## DON'T
- ห้ามแก้ไข/เปลี่ยนชื่อ
- ห้าม OCR/Redact ในโฟลเดอร์นี้

## Allowed Types
- .pdf, .tif, .jpg, .png

## Naming
- ชื่อเดิมจากแหล่ง + timestamp

## Claude & Gemini Rules
- อ่าน README.md ก่อนทำงาน (pre-flight)
- ถ้าต้องแปลง ให้ส่งผลลัพธ์ไป /02_pdf_clean เท่านั้น
- ห้าม overwrite; ต้องสร้างไฟล์ใหม่พร้อม suffix
- บันทึก command log และ SHA-256 ของทุก output