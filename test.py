from collections import defaultdict

def build_index(documents):
    index = defaultdict(list)
    for doc_id, content in documents.items():
        words = content.split()
        for word in words:
            index[word].append(doc_id)
            print(index[word])
    print(index)
    


documents = {1: "mpple dc is example", 2: "none example"}

build_index(documents)