import requests
import pdfplumber

import io

pdf_href = 'https://www.federacao-triatlo.pt/ftp2015/wp-content/uploads/2025/09/2025-09-07-ix-duatlo-fatima-cadetes-masculinos-rev01.pdf#navpanes=0'

row_selected = None
row_reference = None

response = requests.get(pdf_href)
response.raise_for_status()  # Raises an error if the download failed

with pdfplumber.open(io.BytesIO(response.content)) as pdf:
    for page in pdf.pages:
        text = page.extract_text() or ""
        rows = text.splitlines()
        for row in rows:
            if "Illia Kucher" in row:
                print(row)
                row_selected = row
            elif "Nome" in row:
                print(row)
                row_reference = row