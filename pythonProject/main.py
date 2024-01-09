from difflib import SequenceMatcher

def compare_documents(doc1, doc2, threshold=0.7):
  """
  Compares two documents using SequenceMatcher and highlights potential plagiarism.

  Args:
    doc1: String containing the first document.
    doc2: String containing the second document.
    threshold: Similarity threshold for marking plagiarism (0-1).

  Returns:
    A tuple containing:
      - plagiarized_text: String with highlighted potential plagiarism from doc1.
      - similarity_score: Float representing the overall similarity between documents.
  """
  matcher = SequenceMatcher(None, doc1, doc2)
  match_blocks = list(matcher.get_matching_blocks())

  plagiarized_text = ""
  similarity_score = 0

  for block in match_blocks:
    size = block[2]
    if size / len(doc1) >= threshold:
      # Highlight match in doc1
      plagiarized_text += f"<span style='background-color: yellow;'>{doc1[block[1]:block[1]+size]}</span>"
    else:
      plagiarized_text += doc1[block[1]:block[1]+size]

    similarity_score += size / len(doc1)

  return plagiarized_text, similarity_score

# Example usage
doc1 = open("document1.txt", "r").read()
doc2 = open("document2.txt", "r").read()

plagiarized_text, similarity_score = compare_documents(doc1, doc2)

print(f"Similarity score: {similarity_score:.2f}")
print("Highlighted text:")
print(plagiarized_text)

