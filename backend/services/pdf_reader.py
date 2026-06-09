import pdfplumber


def extract_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            ## if there is is empty page, skip it
            if page_text:
                text += page_text + "\n"

    return text
