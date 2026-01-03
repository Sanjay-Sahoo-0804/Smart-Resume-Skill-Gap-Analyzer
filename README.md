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




▶️ How to Run Locally
pip install -r requirements.txt
python app.py


Open browser →
http://127.0.0.1:5000

🌐 Live Demo

🔗 Deployed on Render
(https://smart-resume-skill-gap-analyzer.onrender.com)

📌 How It Works 

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
