# claude-api-demo

This repo contains a simple demo of how to use the Claude API.

It creates a chatbot interface that saves messages and history as context.

## Setup

Create a virtual environment (recommended): `python -m venv venv`

Activate the virtual environment: `venv\Scripts\activate`

Install dependencies: `pip install -r requirements.txt`

Add API key to `.env` file
 - ANTHROPIC_API_KEY='your-api-key'

Run `python api_call.py` for the simple api call.

Run `streamlit run chatbot.py` to run the Streamlit app.

## Guidelines for Lessons

Make sure to set up the environement and install libraries before beginning to code as installation takes a while.

Show the quickstart guide here: [Anthropic API Docs](https://platform.claude.com/docs/en/get-started#python)

Show the available models: [Anthropic Models](https://platform.claude.com/docs/en/about-claude/models/overview)

Manually code out the api call (shown in api_call.py) and explain each part of the code.

Show the chatbot interface (shown in chatbot.py). This can be done using Claude Code since we're not focused on UI.

### For Claude Code:

Show off @ing files to give Claude Code context.

Show off pasting images (alt + v on Windows, ctrl + v on Mac) to make the UI look a certain way.
