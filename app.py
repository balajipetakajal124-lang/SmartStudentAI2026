import streamlit as st

st.title("🎓 Smart Student AI")

topic = st.text_input("Enter your study topic:")

if st.button("Explain"):
    if topic:
        st.success(f"Topic: {topic}")

        if topic.lower() == "python":
            st.write("Python is a programming language used for AI, web development, and automation.")
        elif topic.lower() == "ai":
            st.write("Artificial Intelligence helps computers learn and solve problems.")
        elif topic.lower() == "machine learning":
            st.write("Machine Learning is a branch of AI that learns from data.")
        else:
            st.write("This topic will be explained in future updates!")

        st.subheader("📌 Study Tip")
        st.write("Study for 25 minutes and take a 5-minute break.")

        st.subheader("📝 Quiz")
        st.write("Q: What is AI?")
    else:
        st.warning("Please enter a topic.")