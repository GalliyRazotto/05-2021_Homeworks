from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/ping/')
def some_get():
    return {"message": "pong"}
