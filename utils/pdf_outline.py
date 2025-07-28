
from PyPDF2 import PdfReader

def extract_outline(pdf_path):
    reader = PdfReader(pdf_path)
    outlines = reader.outline
    outline_data = []

    def parse_outline(items, parent=None):
        for item in items:
            if isinstance(item, list):
                parse_outline(item, parent)
            else:
                title = item.title
                page_num = reader.get_destination_page_number(item)
                outline_data.append({
                    'title': title,
                    'page': page_num + 1  # PyPDF2 page numbering starts at 0
                })

    parse_outline(outlines)
    return outline_data
