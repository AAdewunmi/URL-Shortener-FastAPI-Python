# main.py
# FastAPI Implementation

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Welcome to the URL shortener API ;-)"
