import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Resume Matcher")

st.title("AI Resume Matcher")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type="pdf"
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:
                text += page.extract_text()

        st.subheader("Resume Text")
        st.write(text[:3000])

        resume_words = set(text.lower().split())
        jd_words = set(job_description.lower().split())

        matched = resume_words.intersection(jd_words)
        missing = jd_words.difference(resume_words)

        st.subheader("Matched Keywords")
        st.write(list(matched)[:20])

        st.subheader("Missing Keywords")
        st.write(list(missing)[:20])

        score = int(
            (len(matched) / len(jd_words)) * 100
        )

        st.subheader("Match Score")
        st.write(f"{score}%")

    else:
        st.warning("Please upload resume and paste job description.")