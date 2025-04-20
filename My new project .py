
# EduVision: AI-Powered Career Path Recommender
# Created by Arique Hussain

import streamlit as st
import random

st.set_page_config(page_title="EduVision - Career Recommender", page_icon=":mortar_board:")

st.title("EduVision: AI-Powered Career Path Recommender")
st.write("Welcome! I’m your AI assistant. Tell me about your interests, subjects you like, or your strengths, and I’ll suggest a career path for you.")

# Predefined simple recommendation logic
career_paths = {
    "programming": ["Software Engineer", "AI Engineer", "Data Scientist"],
    "math": ["Data Analyst", "Financial Analyst", "Machine Learning Engineer"],
    "biology": ["Biotech Researcher", "Pharmacologist", "Medical Lab Technician"],
    "art": ["Graphic Designer", "Animator", "UX/UI Designer"],
    "communication": ["Marketing Specialist", "Public Relations Officer", "Content Creator"],
    "hardware": ["System Engineer", "Embedded Systems Developer", "IoT Engineer"]
}

user_input = st.text_area("Describe your interests, favorite subjects, or what you're good at:")

if st.button("Get Career Recommendation"):
    found = False
    for key in career_paths:
        if key in user_input.lower():
            st.success(f"Recommended Career Path: **{random.choice(career_paths[key])}**")
            found = True
            break
    if not found:
        st.info("Hmm... I need a bit more detail to give a suggestion. Try mentioning subjects or skills you like!")

st.markdown("---")
st.markdown("**Created by Arique Hussain** | Powered by AI & Streamlit")
