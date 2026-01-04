from sklearn.metrics.pairwise import cosine_similarity
from bert_model import model

def semantic_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(score * 100, 2)
