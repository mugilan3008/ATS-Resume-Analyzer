# ATS Resume Analyzer

A web-based Applicant Tracking System (ATS) Resume Analyzer that evaluates
how well a resume matches a given job description using NLP techniques.

## Features
- Upload resume in PDF format
- Paste job description
- Calculates ATS match score (%)
- Displays missing keywords
- Simple and interactive Streamlit UI

## Tech Stack
- Python
- Streamlit
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF2

## How It Works
1. Resume text is extracted from PDF
2. Resume and Job Description are cleaned using NLP preprocessing
3. TF-IDF converts text into numerical vectors
4. Cosine similarity calculates ATS match score
5. Missing keywords are identified

##Use Case

Resume optimization
Job matching analysis
Career guidance tools

##Future Improvements

Skill weightage system
Resume improvement suggestions
Multiple resume ranking
Deployment to cloud
   

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

