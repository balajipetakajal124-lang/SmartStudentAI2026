from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_quiz(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a teacher. Create a quiz with 5 multiple-choice "
                        "questions. After the questions, include the correct answers."
                    )
                },
                {
                    "role": "user",
                    "content": f"Create a quiz about {topic}."
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating quiz: {e}"
