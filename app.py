import streamlit as st
from auth import sign_up, sign_in, sign_out

st.set_page_config(page_title="Smart Student AI", page_icon="🎓")

if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- LOGIN / SIGN UP ----------------
if st.session_state.user is None:

    st.title("🎓 Smart Student AI")

    choice = st.radio("Select", ["Login", "Sign Up"])

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if choice == "Sign Up":
        if st.button("Create Account"):
            try:
                sign_up(email, password)
                st.success("Account created successfully! Please log in.")
            except Exception as e:
                st.error(f"Error: {e}")

    if choice == "Login":
        if st.button("Login"):
            try:
                response = sign_in(email, password)
                st.session_state.user = response.user
                st.rerun()
            except Exception:
                st.error("Invalid email or password.")

# ---------------- DASHBOARD ----------------
else:

    st.sidebar.success(f"Welcome {st.session_state.user.email}")

    page = st.sidebar.selectbox(
        "Menu",
        [
            "🏠 Home",
            "🤖 Ask AI",
            "📝 Quiz",
            "📚 Notes",
            "📊 Progress",
            "🚪 Logout"
        ]
    )

    if page == "🏠 Home":
        st.title("🏠 Home")
        st.write("Welcome to Smart Student AI!")

    elif page == "🤖 Ask AI":
        st.title("🤖 Ask AI")
        st.info("AI integration will be added after your OpenAI API key is configured.")

    elif page == "📝 Quiz":
        st.title("📝 Quiz")
        st.write("Quiz feature coming next.")

    elif page == "📚 Notes":
        st.title("📚 Notes")
        st.write("Notes feature coming next.")

    elif page == "📊 Progress":
        st.title("📊 Progress")
        st.progress(0.65)

    elif page == "🚪 Logout":
        sign_out()
        st.session_state.user = None
        st.rerun()
