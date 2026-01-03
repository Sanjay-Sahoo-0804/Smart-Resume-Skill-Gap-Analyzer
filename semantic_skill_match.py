from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_skill_match(resume_text, skills):
    results = {}

    resume_embedding = model.encode(resume_text)

    for skill in skills:
        skill_embedding = model.encode(skill)
        score = cosine_similarity(
            [resume_embedding],
            [skill_embedding]
        )[0][0]

        results[skill] = round(score * 100, 2)

    return results
