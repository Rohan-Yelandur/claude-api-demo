import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5",       # Which Claude model to use 
    max_tokens=100,                 # Maximum number of tokens Claude can output
    messages=[
        {
            "role": "user",
            "content": "Yo Claude, what's the best university in Texas?"
        }
    ]
)

print(message.content[0].text)