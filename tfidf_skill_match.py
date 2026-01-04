from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_skill_match(resume_text, skills):
    results = {}
    vectorizer = TfidfVectorizer()

    for skill in skills:
        vectors = vectorizer.fit_transform([resume_text, skill])
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        results[skill] = round(score * 100, 2)

    return results
