from collections import defaultdict

def build_index(documents):
    index = defaultdict(list)
    for doc_id, content in documents.items():
        words = content.split()
        for word in words:
            index[word].append(doc_id)
    return index

# Example documents for testing
documents = {1: "example content", 2: "more example content"}
index = build_index(documents)
print(index)
