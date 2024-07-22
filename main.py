from fastapi import FastAPI
from .my_project.exercises.maths.router import math_router

app = FastAPI()

app.include_router(math_router, tags=['maths'])

@app.get("/test")
def test():
    return {"result": "If you are reading this, something went fine"}