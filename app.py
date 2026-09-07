import streamlit as st
from database import register_user, login_user
from ai import ask_ai
from notes import generate_notes
from quize import generate_quiz

st.set_page_config(page_title="Smart Student AI", page_icon="🎓")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- LOGIN ----------------
if not st.session_state.logged_in:

    st.title("🎓 Smart Student AI")

    option = st.radio("Choose", ["Login", "Sign Up"])

    if option == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

    else:
        username = st.text_input("Create Username")
        password = st.text_input("Create Password", type="password")

        if st.button("Create Account"):
            if register_user(username, password):
                st.success("Account created successfully!")
            else:
                st.error("Username already exists")

# ---------------- DASHBOARD ----------------
else:

    st.sidebar.title(f"Welcome {st.session_state.username}")

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Home",
            "Ask AI",
            "Quiz",
            "Notes",
            "Logout"
        ]
    )

    if menu == "Home":
        st.title("🎓 Smart Student AI")
        st.write("Welcome to your dashboard!")

    elif menu == "Ask AI":
        st.title("🤖 Ask AI")
        question = st.text_area("Ask any question")

        if st.button("Get Answer"):
            if question:
                answer = ask_ai(question)
                st.write(answer)

    elif menu == "Quiz":
        st.title("📝 Quiz Generator")
        topic = st.text_input("Quiz Topic")

        if st.button("Generate Quiz"):
            if topic:
                st.write(generate_quiz(topic))

    elif menu == "Notes":
        st.title("📚 Notes Generator")
        topic = st.text_input("Notes Topic")

        if st.button("Generate Notes"):
            if topic:
                st.write(generate_notes(topic))

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
