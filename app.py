import streamlit as st
import matplotlib.pyplot as plt
from parser import extract_text_from_pdf
from analyzer import (
    extract_skills,
    extract_skills_by_category,
    calculate_score
)

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("🤖 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    resume_text = extract_text_from_pdf(uploaded_file)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    score, matched = calculate_score(resume_skills, job_skills)
    st.subheader("📊 ATS Score")
    st.metric(label="Match Score", value=f"{score}%")
    st.progress(int(score))

    st.subheader("✅ Matched Skills")
    st.success(", ".join(matched) if matched else "No matched skills")

    missing = list(set(job_skills) - set(resume_skills))

    st.subheader("❌ Missing Skills")
    st.error(", ".join(missing) if missing else "No missing skills")
    st.subheader("📈 Skill Comparison")

    chart_data = {
        "Matched": len(matched),
        "Missing": len(missing)
    }

    st.bar_chart(chart_data)
    st.subheader("📂 Skills by Category")

    category_data = extract_skills_by_category(resume_text)

    if category_data:
        for category, skills in category_data.items():
            st.write(f"**{category.upper()}**: {', '.join(skills)}")
    else:
        st.warning("No categorized skills found")

    st.subheader("💡 Suggestions")

    if missing:
        st.info(f"Consider adding these skills: {', '.join(missing)}")
    else:
        st.success("Great! Your resume matches the job requirements well.")