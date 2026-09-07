from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Smart Student AI, a helpful tutor. "
                        "Explain answers in a simple way for students."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"
