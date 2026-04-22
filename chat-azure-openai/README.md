# Streamlit-Based GPT Chat App

A chat application built with Streamlit and Azure OpenAI Service.



## Overview

This application provides a simple chat interface powered by Azure OpenAI Service.

It is implemented with Streamlit and designed as a transparent example of how to build a GPT-based chat UI.





## Features

- Streamlit-based chat UI

- Azure OpenAI Service integration

- Conversation history stored in st.session\_state

- Readable code structure

- Safe handling of an API key and endpoint via Streamlit Secrets



## File Structure

- app.py            : Main script for the Azure OpenAI chat app

- requirements.txt  : Dependencies for this app

- README.md         : This file



## Notes

- This application has been tested and verified to run on Streamlit Community Cloud.

- This application uses an API key and endpoint from Azure OpenAI Service. These keys must be stored in Streamlit Secrets and should never be hard‑coded in the source code.

- Both API\_VERSION and MODEL\_DEPLOYMENT\_NAME in the chat-azure-openai/app.py must match the settings configured in the Azure OpenAI deployment.

