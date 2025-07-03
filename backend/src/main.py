from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "my name is Shahmeer Ali"}