from fastapi import FastAPI
import uvicorn

from knitportal.routers import products, scrape

app = FastAPI()

app.include_router(scrape.router)
app.include_router(products.router)


@app.get("/")
def get_home():
    return {"message": "you've reached the knitportal"}


def start():
    uvicorn.run("knitportal.main:app", host="0.0.0.0", port=8000, reload=True)
