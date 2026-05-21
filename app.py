import streamlit as st
import pdfplumber
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📄 AI Resume Matcher")
st.caption("Compare your resume with job descriptions using AI-style keyword analysis")

# ---------------- CLEAN TEXT FUNCTION ----------------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📤 Upload Your Resume (PDF)",
    type="pdf"
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200
)

# ---------------- BUTTON ----------------
if st.button("🚀 Analyze Resume"):

    if uploaded_file and job_description:

        text = ""

        # ---------------- PDF READ SAFELY ----------------
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        text = clean_text(text)

        # ---------------- SHOW RESUME PREVIEW ----------------
        with st.expander("📄 View Extracted Resume Text"):
            st.write(text[:3000])

        # ---------------- PROCESSING ----------------
        resume_words = set(text.lower().split())
        jd_words = set(job_description.lower().split())

        matched = resume_words.intersection(jd_words)
        missing = jd_words.difference(resume_words)

        # ---------------- SCORE CALCULATION (SAFE) ----------------
        if len(jd_words) > 0:
            score = int((len(matched) / len(jd_words)) * 100)
        else:
            score = 0

        # ---------------- OUTPUT UI ----------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📊 Match Score", f"{score}%")

        with col2:
            st.metric("✅ Matched Keywords", len(matched))

        with col3:
            st.metric("❌ Missing Keywords", len(missing))

               # ---------------- DETAILS ----------------
        st.subheader("✅ Matched Skills")
        st.write(list(matched)[:20])

        st.subheader("❌ Missing Skills")
        st.write(list(missing)[:20])

        # ---------------- INTERVIEW QUESTIONS ----------------
        st.subheader("🎤 Suggested Interview Questions")

        questions = []

        # Questions based on missing skills
        for skill in list(missing)[:5]:
            questions.append(
                f"What is your experience with {skill}?"
            )

        # Default fallback questions
        default_questions = [
            "Tell me about yourself.",
            "Why are you interested in this role?",
            "What are your strengths?",
            "Describe a challenging project you worked on.",
            "How do you solve technical problems?"
        ]

        # Add default questions if needed
        while len(questions) < 5:
            questions.append(
                default_questions[len(questions)]
            )

        # Display questions
        for i, q in enumerate(questions, start=1):
            st.write(f"{i}. {q}")

    else:
        st.warning("⚠️ Please upload resume and paste job description first.")