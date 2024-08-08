import os
import openai
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from logger import setup_logging

# Initialize logging
logger = setup_logging()

app = FastAPI()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    print("Root endpoint was called")
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    print(f"say_hello endpoint was called with name: {name}")
    return {"message": f"Hello {name}"}

@app.post("/ask-chatgpt")
async def ask_chatgpt(question: Question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content":question.question}
            ],
            max_tokens=150
        )
        answer = response.choices[0].message['content'].strip()
        return {"answer": answer}
    except Exception as e:
        print(f"Error asking ChatGPT: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
