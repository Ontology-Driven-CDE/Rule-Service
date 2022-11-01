from fastapi import FastAPI
from routes import shapes

app = FastAPI()

app.include_router(shapes.router)



