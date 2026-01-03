from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vectors):
    similarity_score = cosine_similarity(vectors[0], vectors[1])
    return round(similarity_score[0][0] * 100, 2)
