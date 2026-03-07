import fitz
import re,os

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    text = re.split(r"REFERENCES|References|Bibliography", text)[0]

    return text


def load_papers(folder="papers"):

    papers = []

    files = os.listdir(folder)

    pdf_files = [f for f in files if f.endswith(".pdf")]

    if len(pdf_files) == 0:
        print("No PDFs found in papers/ folder")
        return papers

    for file in pdf_files:

        path = os.path.join(folder, file)

        text = extract_text(path)

        papers.append({
            "title": file,
            "text": text
        })

    return papers