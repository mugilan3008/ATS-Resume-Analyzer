## ATS Resume Analyzer
A Streamlit app to calculate ATS score using NLP (TF-IDF & cosine similarity)

### Features
- Resume PDF upload
- Job description matching
- ATS score calculation
- Missing keyword detection
- Resume improvement suggestions

  
##  Smart Suggestions
- Suggests resume improvements when ATS score is low
- Recommends adding missing skills from Job Description
- Provides formatting & optimization tips for ATS systems

### Live Demo
https://ats-resume-analyzer-2svcv7opvrv8fdearq5nc7.streamlit.app/

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

