from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Salut": "Marseille !"}

@app.get("/toto")
def read_root():
    return {"Salut": "Dume !"}
