from collections import defaultdict

def rank_documents(query, index):
    query_words = query.split()
    doc_scores = defaultdict(int)
    for word in query_words:
        for doc_id in index.get(word, []):
            doc_scores[doc_id] += 1
    ranked_docs = sorted(doc_scores.items(), key=lambda item: item[1], reverse=True)
    return ranked_docs

# Example query for testing
query = "example"
index = {'example': [1, 2], 'content': [1, 2], 'more': [2]}
ranked_docs = rank_documents(query, index)
print(ranked_docs)
