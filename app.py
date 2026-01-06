import streamlit as st
from PyPDF2 import PdfReader
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")

# -------- FUNCTIONS --------

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words("english")]
    return " ".join(words)


# -------- STREAMLIT UI --------

st.set_page_config(page_title="ATS Resume Analyzer")

st.title("📄 ATS Resume Analyzer")
st.write("Upload resume and paste job description to check ATS score")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    if uploaded_resume is None or job_description.strip() == "":
        st.warning("Please upload resume and enter job description")
    else:
        resume_text = extract_text_from_pdf(uploaded_resume)

        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([clean_resume, clean_jd])

        similarity = cosine_similarity(vectors[0:1], vectors[1:2])
        ats_score = round(similarity[0][0] * 100, 2)

        st.subheader("📊 ATS Score")
        st.progress(int(ats_score))
        st.write(f"*ATS Match Score: {ats_score}%*")

        resume_words = set(clean_resume.split())
        jd_words = set(clean_jd.split())

        missing_skills = jd_words - resume_words

        st.subheader("❌ Missing Keywords")
        if len(missing_skills) == 0:
            st.success("No major keywords missing 🎉")
        else:
            for skill in list(missing_skills)[:15]:
                st.write("•", skill)