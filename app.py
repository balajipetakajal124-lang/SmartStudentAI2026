import streamlit as st
from auth import sign_up, sign_in, sign_out
from notes import generate_notes

st.set_page_config(page_title="Smart Student AI", page_icon="🎓", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- LOGIN PAGE ----------------

if st.session_state.user is None:

    st.title("🎓 Smart Student AI")
    st.subheader("Login or Create a New Account")

    option = st.radio("Choose", ["Login", "Sign Up"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign Up":
        if st.button("Create Account"):
            try:
                sign_up(email, password)
                st.success("Account created successfully. Please login.")
            except Exception as e:
                st.error(e)

    if option == "Login":
        if st.button("Login"):
            try:
                response = sign_in(email, password)
                st.session_state.user = response.user
                st.rerun()
            except Exception:
                st.error("Invalid Email or Password")

# ---------------- HOME PAGE ----------------

else:

    st.sidebar.title("🎓 Smart Student AI")
    st.sidebar.success(f"Welcome\n{st.session_state.user.email}")

    page = st.sidebar.selectbox(
        "Menu",
        [
            "🏠 Home",
            "📚 Notes",
            "📝 Quiz",
            "🤖 Ask AI",
            "📊 Progress",
            "🚪 Logout"
        ]
    )

    if page == "🏠 Home":

        st.title("🏠 Dashboard")
        st.write("Welcome to Smart Student AI.")

        st.info("Choose a feature from the left menu.")

    elif page == "📚 Notes":

        st.title("📚 Study Notes")

        topic = st.text_input("Enter Topic")

        if st.button("Generate Notes"):
            if topic:
                st.markdown(generate_notes(topic))
            else:
                st.warning("Please enter a topic.")

    elif page == "📝 Quiz":

        st.title("📝 Quiz")

        st.write("Question:")

        answer = st.radio(
            "What does AI stand for?",
            [
                "Artificial Intelligence",
                "Automatic Internet",
                "Advanced Information",
                "Artificial Internet"
            ]
        )

        if st.button("Submit Quiz"):
            if answer == "Artificial Intelligence":
                st.success("✅ Correct!")
            else:
                st.error("❌ Wrong Answer")

    elif page == "🤖 Ask AI":

        st.title("🤖 Ask AI")

        st.info("AI will be added after connecting the OpenAI API.")

    elif page == "📊 Progress":

        st.title("📊 Progress")

        st.progress(50)

        st.write("Keep learning every day!")

    elif page == "🚪 Logout":

        sign_out()
        st.session_state.user = None
        st.rerun()
