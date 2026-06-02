# 📄 AI Resume Matcher

An AI-powered Resume Screening Tool that compares resumes with job descriptions and generates match scores, missing skills, and interview questions.

Built using Python and Streamlit for fast and simple local execution.

---

## 🚀 Features

📤 Upload Resume (PDF)  
📝 Paste Job Description  
📊 Match Score Generation (0–100%)  
✅ Matched Skills Detection  
❌ Missing Skills Identification  
🎤 AI-style Interview Questions  
📄 Resume text preview  
⚡ Lightweight Streamlit UI  

---

## 🏗️ Tech Stack

- Python 🐍  
- Streamlit 🎈  
- pdfplumber 📄  
- re (Regex)  

---

## 🧠 How It Works

1. User uploads resume PDF  
2. Job description is pasted  
3. Text is extracted using pdfplumber  
4. Keywords are compared  
5. System generates:
   - Match Score  
   - Matched Skills  
   - Missing Skills  
   - Interview Questions  

---

## 📸 Screenshots

🏠 Home Interface  
![Home](Screenshot (12).png)

📊 Result Output  
![Output](Screenshot (13).png) (Screenshot (14).png)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai-resume-matcher
cd ai-resume-matcher
pip install -r requirements.txt
streamlit run app.py

