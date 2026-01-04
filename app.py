from flask import Flask, render_template, request
from preprocess import clean_text
from pdf_reader import extract_text_from_pdf
from skill_gap import load_skills, find_skill_gap
from tfidf_similarity import tfidf_similarity
from tfidf_skill_match import tfidf_skill_match
from job_recommender import recommend_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        pdf_file = request.files.get("resume_pdf")
        job_desc = request.form.get("job", "")

        if not pdf_file:
            return "Invalid input"

        resume_text = extract_text_from_pdf(pdf_file)
        resume_clean = clean_text(resume_text)

        overall_score = None
        if job_desc.strip():
            overall_score = tfidf_similarity(
                resume_clean,
                clean_text(job_desc)
            )

        skills = load_skills()
        present, missing = find_skill_gap(resume_clean, skills)
        skill_scores = tfidf_skill_match(resume_clean, skills)
        jobs = recommend_jobs(resume_clean)

        return render_template(
            "result.html",
            score=overall_score,
            present=present,
            missing=missing,
            skill_scores=skill_scores,
            jobs=jobs
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
