from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def skill_match_percentage(resume_text, skills):
    results = {}

    for skill in skills:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, skill])

        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        results[skill] = round(score * 100, 2)

    return results
