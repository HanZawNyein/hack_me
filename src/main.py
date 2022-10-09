from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome From FastAPI with CI-CD"}


@app.get("/english-number/{number}")
async def english_number(number: int):
    return {"english-number": number}
