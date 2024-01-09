import difflib
import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_match_text_file(content):
    with open("match_text_file.txt", 'w') as file:
        for line in content:
            file.write(line + '\n')

def compare_percentage(file1_content, file2_content):
    match = difflib.SequenceMatcher(None, file1_content, file2_content).ratio()
    return match

def compare_text(file1_content, file2_content):
    difference = difflib.Differ()
    diff = difference.compare(file1_content.splitlines(), file2_content.splitlines())
    matched_lines = [line[2:] for line in diff if line.startswith(' ')]
    return matched_lines

def read_any_document(file_path):
    if file_path.endswith('.txt'):
        return read_text(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    else:
        print("Unsupported format")

file1_path = input("Input first file location: ")
file2_path = input("Input Second file location: ")

file1_content = read_any_document(file1_path)
file2_content = read_any_document(file2_path)


match_percentage = compare_percentage(file1_content, file2_content) * 100
format_match_percentage = "{:.2f}".format(match_percentage)
match_text_lines = compare_text(file1_content, file2_content)

print(f"\n{format_match_percentage}% Plagiarism detected...\n")
print("\t\tMatched Text\n\t--------------------\n")

# Print and write each matched line separately
for line in match_text_lines:
    print(line)
write_match_text_file(match_text_lines)
