from flask import Flask, render_template, request
from preprocess import clean_text
from pdf_reader import extract_text_from_pdf
from semantic_similarity import semantic_similarity
from semantic_skill_match import semantic_skill_match
from skill_gap import load_skills, find_skill_gap
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

        # Optional overall match with pasted JD
        overall_score = None
        if job_desc.strip():
            overall_score = semantic_similarity(
                resume_clean,
                clean_text(job_desc)
            )

        skills = load_skills()
        present, missing = find_skill_gap(resume_clean, skills)
        skill_scores = semantic_skill_match(resume_clean, skills)

        # 🔥 JOB RECOMMENDATION
        recommended_jobs = recommend_jobs(resume_clean)

        return render_template(
            "result.html",
            score=overall_score,
            present=present,
            missing=missing,
            skill_scores=skill_scores,
            jobs=recommended_jobs
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
