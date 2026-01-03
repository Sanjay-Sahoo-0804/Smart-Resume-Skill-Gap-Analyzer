from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_texts(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    return vectors
