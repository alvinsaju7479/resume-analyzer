# 🤖 AI Resume Analyzer

## 🚀 Overview

The **AI Resume Analyzer** is a web-based application that analyzes resumes and compares them with job descriptions to calculate an ATS (Applicant Tracking System) score. It helps users identify missing skills and improve their resumes for better job matching.

---

## ✨ Features

* 📄 Upload and parse resumes (PDF format)
* 🧠 Extract skills using regex-based NLP
* 📊 Calculate ATS match score
* 📈 Visualize skill comparison (matched vs missing)
* 📂 Category-wise skill breakdown
* 💡 Smart suggestions for resume improvement

---

## 🛠 Tech Stack

* Python
* Streamlit
* spaCy
* Scikit-learn
* Matplotlib

---

## 📂 Project Structure

```plaintext
resume-analyzer/
│
├── app.py                 # Streamlit application (UI + workflow)
├── analyzer.py            # Skill extraction & scoring logic
├── parser.py              # PDF text extraction
├── skills_db.json         # Skills database (categorized)
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignore unnecessary files
```



## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume-analyzer
```

### 2. Create virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download spaCy model

```bash
python -m spacy download en_core_web_sm
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. Extracts text from the uploaded resume
2. Identifies skills using a JSON-based skill database
3. Compares extracted skills with job description
4. Calculates ATS match score
5. Displays insights and suggestions

---

## 💼 Use Case

* Job seekers optimizing resumes
* Students applying for internships/jobs
* Professionals improving ATS compatibility

---

## 🚀 Future Improvements

* 🔥 AI-based resume feedback (GPT integration)
* 🌐 Live deployment (Streamlit Cloud)
* 📑 Support for DOCX resumes
* 📊 Advanced NLP models for better accuracy

---

## 👨‍💻 Author

**Alvin Saju**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
