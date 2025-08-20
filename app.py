import streamlit as st
import utils
import os

st.set_page_config(page_title="📚 Shiva AI Tutor", layout="wide")

# Initialize session state
if "progress" not in st.session_state:
    st.session_state.progress = {"Ch1": 0, "Ch2": 0}

# Sidebar Navigation
st.sidebar.title("📖 Navigation")
page = st.sidebar.radio("Go to", ["Tutor", "Progress Dashboard"])

if page == "Tutor":
    st.title("🤖 Shiva AI Study Buddy")
    st.write("Ask questions from your NCERT chapters and I’ll explain them.")

    query = st.text_input("❓ Ask a question:")
    if query:
        answer = utils.retrieve_answer(query)
        st.success(answer)

        # Simple progress tracking (increment when answered)
        st.session_state.progress["Ch1"] += 10
        if st.session_state.progress["Ch1"] > 100:
            st.session_state.progress["Ch1"] = 100

elif page == "Progress Dashboard":
    st.title("📊 Your Progress Dashboard")
    st.write("Track how much you’ve studied so far.")

    for chapter, progress in st.session_state.progress.items():
        st.write(f"**{chapter}**")
        st.progress(progress)
