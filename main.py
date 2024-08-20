import uvicorn
from fastapi import FastAPI
from logger import setup_logging

# Initialize logging
logger = setup_logging()

app = FastAPI()


@app.get("/")
def root():
    print("Root endpoint was called")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    print(f"say_hello endpoint was called with name: {name}")
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
