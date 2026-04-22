# GPT-based Chat App

## Overview
This repository manages two independent chat applications built with Streamlit:
- chat-openai
- chat-azure-openai

## Repository Structure
```
.
├── README.md
├── chat-openai/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── chat-azure-openai/
    ├── app.py
    ├── requirements.txt
    └── README.md
```

## Purpose of This Repository
- Provide a clean comparison between OpenAI API and Azure OpenAI Service implementations
- Demonstrate secure API key handling using Streamlit Secrets
- Maintain production‑ready code for both environments

## Security Notes
- API keys must not be hard‑coded.
- All the secrets must be stored in Streamlit Secrets(e.g., Streamlit Cloud Secrets).

## License
This repository is provided for portfolio and educational purposes.
