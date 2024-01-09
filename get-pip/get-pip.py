import difflib
import docx
import PyMuPDF
from tika import parser

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_docx(file_path):
    doc = docx.Document(file_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(paragraphs)

def read_pdf(file_path):
    doc = PyMuPDF.PdfFileReader(file_path)
    text = ''
    for page_num in range(doc.numPages):
        text += doc.getPageText(page_num)
    return text

def read_any_document(file_path):
    if file_path.endswith('.txt'):
        return read_text_file(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")

def calculate_similarity(file1_content, file2_content):
    d = difflib.Differ()
    diff = d.compare(file1_content.splitlines(), file2_content.splitlines())
    similarity = 1 - sum(1 for line in diff if line.startswith(' ')) / max(len(file1_content), len(file2_content))
    return similarity * 100, '\n'.join(line[2:] for line in diff if line.startswith(' '))

def main():
    file1_path = 'path/to/file1.txt'  # Replace with the path to your first document
    file2_path = 'path/to/file2.docx'  # Replace with the path to your second document

    file1_content = read_any_document(file1_path)
    file2_content = read_any_document(file2_path)

    similarity_percentage, matched_text = calculate_similarity(file1_content, file2_content)

    print(f"Similarity Percentage: {similarity_percentage:.2f}%")
    print("\nMatched Text:\n", matched_text)

if __name__ == "__main__":
    main()
