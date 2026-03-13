import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="ShivIQ", layout="wide")

HTML_DIR = Path("pages")

PAGES = {
    "Home": "index.html",
    "Resume": "resume.html",
    "Company": "company.html",
    "Process": "process.html",
    "Dress Code": "dresscode.html",
    "Self Intro Choice": "selfintro-choice.html",
    "Self Intro Text": "selfintro-text.html",
    "Self Intro Voice": "selfintro-voice.html",
    "HR Questions": "hrquestions.html",
    "Result": "result.html",
}

st.title("ShivIQ - Streamlit Wrapper")

selected = st.sidebar.radio("Open page", list(PAGES.keys()))

file_path = HTML_DIR / PAGES[selected]

if not file_path.exists():
    st.error(f"Missing file: {file_path}")
else:
    html = file_path.read_text(encoding="utf-8")
    components.html(html, height=1000, scrolling=True)