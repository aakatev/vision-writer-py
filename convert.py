from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path, convert_from_bytes

pages = convert_from_path('./media/in/document.pdf')
page_number = 0

for page in pages:
    page_number += 1
    page.save('./media/out/page'+str(page_number)+'.jpg', 'JPEG')
