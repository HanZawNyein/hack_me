from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/english-number/{number}")
async def english_number(number: int):
    return {"english-number": number}
