# Streamlit-Based GPT Chat App

A chat application built with Streamlit and the OpenAI API.



## Overview

This application provides a simple chat interface powered by the OpenAI API.

It is implemented with Streamlit and designed as a transparent example of how to build a GPT-based chat UI.





## Features

- Streamlit-based chat UI

- OpenAI API integration

- Conversation history stored in st.session\_state

- Readable code structure

- Safe handling of an API key via Streamlit Secrets



## File Structure

- app.py            : Main script for the OpenAI chat app

- requirements.txt  : Dependencies for this app

- README.md         : This file



## Notes

- This application has been tested and verified to run on Streamlit Community Cloud.

- This application uses an API key issued by OpenAI. This key must be stored in Streamlit Secrets and should never be hard‑coded in the source code.

- MODEL\_NAME in the chat-openai/app.py must match the OpenAI model name specified in the API call.

