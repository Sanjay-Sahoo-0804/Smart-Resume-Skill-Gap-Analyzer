import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_jobs(file_path="jobs/jobs.json"):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        return []

def recommend_jobs(resume_text, top_n=3):
    jobs = load_jobs()
    if not jobs:
        return []

    documents = [resume_text] + [job["description"] for job in jobs]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(vectors[0], vectors[1:])[0]

    recommendations = []
    for job, score in zip(jobs, scores):
        recommendations.append({
            "title": job["title"],
            "score": round(score * 100, 2)
        })

    return sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )[:top_n]
