from flask import Flask, request, render_template
from collections import defaultdict

app = Flask(__name__)

# Function to build an index from documents
def build_document_index(documents):
    index = defaultdict(list)
    for doc_id, content in documents.items():
        words = content.split()
        for word in words:
            index[word].append(doc_id)
    return index

# Function to rank documents based on a query
def rank_documents(query, index):
    query_words = query.split()
    doc_scores = defaultdict(int)
    for word in query_words:
        for doc_id in index.get(word, []):
            doc_scores[doc_id] += 1
    ranked_docs = sorted(doc_scores.items(), key=lambda item: item[1], reverse=True)
    return ranked_docs

# Example documents for testing
documents = {1: "example content", 2: "more example content",3:"another example none"}
doc_index = build_document_index(documents)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = rank_documents(query, doc_index)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
