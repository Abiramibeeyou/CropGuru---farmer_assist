import streamlit as st
from google import genai

def initialize_gemini_client():
    api_key = st.secrets["gemini_api_key"]
    return genai.Client(api_key=api_key)

def query_gemini_farm_assistant(client, question):
    prompt = (
        "You are an experienced and empathetic agricultural advisor designed to assist farmers in making wise farming decisions. "
        "Respond in clear, simple, and friendly language without technical jargon. "
        "Offer practical, actionable, and regionally relevant advice on crop care, cultivation best practices, pest and disease management, fertilizer recommendations, "
        "weather advisory, irrigation planning, and soil health management. "
        "Be concise, factual, and easy to follow. Use a positive and supportive tone. Avoid long explanations or complex terms. "
        "Maintain context for multi-turn conversations."
    )
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"{prompt}\n\nUser Query: {question}"
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    client = initialize_gemini_client()
    user_question = input("Ask your farming related question: ")
    answer = query_gemini_farm_assistant(client, user_question)
    print("\nAI Assistant Response:\n", answer)
