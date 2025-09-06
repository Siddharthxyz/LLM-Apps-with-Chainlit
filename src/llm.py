import os
import google.generativeai as genai
from src.prompt import system_instruction
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, model="gemini-1.5-flash", temperature=0):
    model = genai.GenerativeModel(model)
    
    # Convert messages into plain text prompt
    user_content = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    
    response = model.generate_content(
        user_content,
        generation_config={"temperature": temperature}
    )

    return response.text
