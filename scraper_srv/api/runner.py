import uvicorn
from typing import Optional
from fastapi import FastAPI

from scrapers import web_scraper

app = FastAPI(
    title="ARM: Web scraping exercise",
    description="Awesome util to scraping webs!",
    version="1.0"
)
v1 = app

@v1.get("/get_href")
def get_href():
    return web_scraper.get_href('https://www.geeksforgeeks.org/')

app.mount("/api/v1", v1)

def startApiService():
    uvicorn.run("api.runner:app", host="0.0.0.0", port=8080)