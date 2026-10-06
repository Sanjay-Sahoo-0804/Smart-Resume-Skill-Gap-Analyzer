# Smart Resume & Skill Gap Analyzer

Smart Resume & Skill Gap Analyzer is an intelligent, NLP-driven web application designed to evaluate resumes against target job descriptions. By utilizing mathematical vectorization models (TF-IDF) alongside deep semantic understanding frameworks (BERT embeddings), the system computes precise textual similarity metrics, highlights critical technical skill discrepancies, and maps applicants directly to alternate relevant professional profiles.

---

## 🚀 Key Features

- **Automated Document Extraction:** Efficient extraction of unstructured text components from complex multi-page PDF resumes using high-speed layout parsers.
- **Hybrid Similarity Scoring Engine:** Side-by-side processing utilizing TF-IDF calculations for exact-token keyword frequency extraction and BERT architecture models to deduce implicit conceptual alignments.
- **Granular Skill Gap Analysis:** Automated tracking matrix cross-referencing extracted candidate traits against target vacancy configurations to build dynamic missing-skill reports.
- **Automated Profile Recommender:** An intelligent engine matching existing resume profiles against an internal storage manifest of open corporate opportunities to output relevant alternatives.
- **Clean Interactive Interface:** A lightweight multi-stage frontend layout built to streamline profile uploads, job target definitions, and clear analytical visuals.

---

## 🛠️ Tech Stack & Dependencies

- **Web Server Framework:** Flask (Python-driven lightweight backend pipeline)
- **Natural Language Processing (NLP):** NLTK (Text cleaning, tokenization, filtering)
- **Machine Learning & Mathematical Vectorization:** Scikit-Learn (TF-IDF, Cosine Similarity matrices)
- **Deep Semantic Embeddings:** Hugging Face Transformers (BERT semantic text vector models)
- **PDF Extraction Core:** PyPDF2
- **Production Server Layer:** Gunicorn

---

## 📁 Project Architecture & Directory Structure

Based on your repository snapshot, here is the official folder design of the tool:

```text
Smart-Resume-Skill-Gap-Analyzer-main/
├── data/                       # Local raw text verification logs
│   ├── job_description.txt     # Cached operational criteria snapshot
│   └── resume.txt              # Extracted plain-text storage segment
├── experimental/               # Core deep-learning modeling logic
│   ├── bert_model.py           # Instantiates deep BERT networks for embedding generation
│   ├── semantic_similarity.py  # Matrix mathematical calculations over BERT spaces
│   └── semantic_skill_match.py # Concept-based dictionary scoring scripts
├── jobs/                       # Dynamic role repository
│   └── jobs.json               # Profile database manifest mapping matching parameters
├── static/                     # Global client-side presentation assets
│   └── style.css               # Central typography, layout grid, and visual rule-sheet
├── templates/                  # Server-side HTML render layouts
│   ├── index.html              # Document upload and data configuration landing interface
│   └── result.html             # Profile evaluation and metrics visualization dashboard
├── app.py                      # Main Flask application driver orchestrating user lifecycles
├── job_recommender.py          # Proximity match runner pairing skills to open corporate specs
├── pdf_reader.py               # Buffer file processing stream extracting text from raw PDFs
├── preprocess.py               # Stop-word removal, text case adjustments, and regex filters
├── requirements.txt            # Operational library dependency manifest
├── runtime.txt                 # Specifies execution environment runtime version bindings
├── similarity.py               # Core orchestrator executing standard proximity comparison hooks
├── skill_gap.py                # Set-difference array compiler identifying absent profile skills
├── skill_match.py              # Boolean validation module sorting candidate strengths
├── start.sh                    # Automation bootstrapper script firing production servers
├── tfidf_similarity.py         # Cosine closeness metric calculator over sparse frequency matrices
├── tfidf_skill_match.py        # Token-frequency mapping loop verifying candidate matches
└── vectorizer.py               # Matrix building component transforming raw vocabularies
```

---

## ⚙️ Installation & Local Setup

Follow these sequential instructions to stand up the workspace locally on your system:

### 1. Prerequisites
Ensure you have the required **Python 3.10** engine installed.

### 2. Install Project Dependencies
Travel into the root folder directory path using your host CLI terminal and initialize dependencies:

```bash
# Initialize clean execution space environments (Optional)
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

# Clean compile the necessary system frameworks
pip install -r requirements.txt
```

### 3. Launch the Server Locally
To start the developer test framework on your host device, run:
```bash
python app.py
```
Open your preferred desktop browser and target `http://localhost:5000` to interact with the platform interface.

### 4. Deploying to Production
For highly stable, scalable multi-worker operational layers, run the localized environment wrapper bash shell script:
```bash
bash start.sh
```

---

## 🛣️ NLP Pipeline & Operational Flowchart

### 1. Ingestion & Preprocessing (`pdf_reader.py` & `preprocess.py`)
- The multi-page resume PDF upload stream is parsed into raw, unformatted text segments.
- Extracted characters undergo systematic stop-word removal, regex string normalization, lowercasing, and whitespace consolidation to prepare clean data payloads.

### 2. Evaluation Strategy (`tfidf_similarity.py` & `experimental/`)
- **Token Accuracy Processing:** The app constructs frequency vector arrays to calculate precise keyword cosine proximity dimensions between the candidate profile and the target job description.
- **Deep Semantic Matching:** In parallel, words are parsed through an underlying BERT multi-layer encoder architecture to map phrases conceptually, ensuring relevant synonyms or correlated tools register as valid matches even without an exact textual match.

### 3. Discrepancy Parsing & Delivery (`skill_gap.py` & `job_recommender.py`)
- Missing technical traits are filtered out into distinct lists to provide actionable training recommendations.
- The compiled capability footprint is indexed against `jobs.json` parameters to offer alternate job vacancies with high contextual match percentages.
