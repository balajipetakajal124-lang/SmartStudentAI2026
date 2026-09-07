from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_notes(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert teacher. Write easy-to-understand study "
                        "notes with headings, bullet points, and a short summary."
                    )
                },
                {
                    "role": "user",
                    "content": f"Create study notes on: {topic}"
                }
            ],
            temperature=0.5
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating notes: {e}"
