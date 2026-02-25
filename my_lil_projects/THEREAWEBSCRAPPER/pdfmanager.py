import requests
import pdfplumber
import io


def pdf_manager(pdf_href):
    row_selected = None
    row_reference = None

    try:
        response = requests.get(pdf_href)
        response.raise_for_status()  # Raises an error if the download failed
    except requests.exceptions.InvalidSchema:
        return None

    with pdfplumber.open(io.BytesIO(response.content)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            rows = text.splitlines()
            for row in rows:
                if "Illia Kucher" in row:
                    print(row)
                    row_selected = row
                elif "Nome" in row:
                    #print(row)
                    row_reference = row
    if row_selected == None:
        return None
    else:
        return row_reference, row_selected