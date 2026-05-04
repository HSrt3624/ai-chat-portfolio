"""
OpenAI Chat App
(Built with Streamlit and a GPT model)

"""

import streamlit as st
from openai import OpenAI

API_KEY = st.secrets["OPENAI_API_KEY"]
MODEL_NAME = "gpt-4o"
AI_MODEL = "openai_model"

client = OpenAI(
    api_key=API_KEY
)

if AI_MODEL not in st.session_state:
    st.session_state[AI_MODEL] = MODEL_NAME

if "messages" not in st.session_state:
    st.session_state["messages"] = []


st.title("Streamlit-Based GPT Chat App")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=st.session_state[AI_MODEL],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        except Exception as e:
            st.error(f"An error has occurred: {e}")
    st.session_state.messages.append({"role": "assistant", "content": response})
