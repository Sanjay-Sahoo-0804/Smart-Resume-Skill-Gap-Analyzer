Smart Resume Skill Gap Analyzer & Job Recommendation System

An ATS-style machine learning web application that analyzes resumes, identifies skill gaps, computes semantic match scores with job descriptions, and recommends the most suitable jobs using Sentence-BERT embeddings.

🚀 Features

📄 Upload resume in PDF format

🧠 Semantic resume–job matching using Sentence-BERT (BERT-based embeddings)

📊 Overall match percentage

🧩 Skill-wise match percentage

❌ Identification of missing skills

💼 Job recommendation engine (Top-N jobs ranked by relevance)

🌐 Deployed as a live Flask web application

🧠 Technologies Used

Python

Flask – Web framework

NLTK – Text preprocessing

Sentence-Transformers (BERT) – Semantic embeddings

Scikit-learn – Cosine similarity

PyPDF2 – Resume PDF parsing

HTML / CSS – Frontend

Render – Cloud deployment

🏗️ Project Architecture
Resume (PDF)
   ↓
PDF Text Extraction
   ↓
Text Preprocessing (NLP)
   ↓
Sentence-BERT Embeddings
   ↓
Semantic Similarity (Cosine)
   ↓
Match Score + Skill Gap
   ↓
Job Recommendation Engine

📁 Project Structure
Smart-Resume-Skill-Gap-Analyzer/
│
├── app.py
├── preprocess.py
├── pdf_reader.py
├── semantic_similarity.py
├── semantic_skill_match.py
├── job_recommender.py
├── skill_gap.py
├── skills_list.txt
├── requirements.txt
│
├── jobs/
│   └── jobs.json
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css

▶️ How to Run Locally
pip install -r requirements.txt
python app.py


Open browser →
http://127.0.0.1:5000

🌐 Live Demo

🔗 Deployed on Render
(Add your Render URL here once deployment finishes)

📌 How It Works (Brief)

Resume and job descriptions are converted into semantic embeddings using Sentence-BERT.

Cosine similarity is used to compute relevance scores.

Skills are matched semantically to identify strengths and gaps.

Jobs are ranked and recommended based on similarity.

💡 Future Enhancements

PDF/DOCX support with advanced parsing

Recruiter dashboard

Candidate ranking system

GPU-based inference for faster performance

👨‍💻 Author

Sanjay Sahoo
GitHub: https://github.com/Sanjay-Sahoo-0804
