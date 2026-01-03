import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_jobs(file_path="jobs/jobs.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def recommend_jobs(resume_text, top_n=3):
    jobs = load_jobs()

    resume_embedding = model.encode(resume_text)

    recommendations = []

    for job in jobs:
        job_embedding = model.encode(job["description"])
        score = cosine_similarity(
            [resume_embedding],
            [job_embedding]
        )[0][0]

        recommendations.append({
            "title": job["title"],
            "score": round(score * 100, 2)
        })

    # Sort jobs by similarity score (descending)
    recommendations = sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:top_n]
