import streamlit as st
from PyPDF2 import PdfReader
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# PDF TEXT EXTRACTION
# -----------------------------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


# -----------------------------
# TEXT CLEANING
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# -----------------------------
# ATS SCORE CALCULATION
# -----------------------------
def calculate_ats_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    score = round(similarity[0][0] * 100, 2)
    return score


# -----------------------------
# MISSING KEYWORDS
# -----------------------------
def find_missing_keywords(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    missing = jd_words - resume_words
    return sorted(list(missing))


# -----------------------------
# IMPROVEMENT SUGGESTIONS 
# -----------------------------
def generate_suggestions(score, missing_keywords):
    suggestions = []

    if score < 40:
        suggestions.append("Your resume has very low ATS match. Major improvements needed.")
    elif score < 70:
        suggestions.append("Your resume matches partially. Try improving skills and keywords.")
    else:
        suggestions.append("Good ATS score. Minor keyword optimization can improve further.")

    if missing_keywords:
        suggestions.append(
            f"Add these important skills/keywords to your resume: {', '.join(missing_keywords[:10])}"
        )

    suggestions.append("Use simple resume format (no tables, no graphics).")
    suggestions.append("Add skills exactly as mentioned in the Job Description.")
    suggestions.append("Use standard headings like Skills, Experience, Projects, Education.")

    return suggestions


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")

st.title("📄 ATS Resume Analyzer")
st.write("Upload your resume and paste Job Description to check ATS match score.")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description here")

if st.button("Analyze Resume"):
    if uploaded_resume is None or jd_text.strip() == "":
        st.error("Please upload resume and paste Job Description.")
    else:
        # Extract & clean
        resume_text = extract_text_from_pdf(uploaded_resume)
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        # ATS score
        ats_score = calculate_ats_score(clean_resume, clean_jd)

        st.subheader("📊 ATS Match Score")
        st.progress(int(ats_score))
        st.write(f"*ATS Score:* {ats_score}%")

        # Missing keywords
        missing_keywords = find_missing_keywords(clean_resume, clean_jd)

        st.subheader("❌ Missing Keywords")
        if missing_keywords:
            for word in missing_keywords[:15]:
                st.write("•", word)
        else:
            st.success("No major keywords missing!")

        # Suggestions
        suggestions = generate_suggestions(ats_score, missing_keywords)

        st.subheader("✅ Resume Improvement Suggestions")
        for s in suggestions:
            st.write("✔", s)