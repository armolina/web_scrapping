import uvicorn
from fastapi import FastAPI

from scrapers import web_scraper
from actions import list_request_log_dict, get_request_log_dict

app = FastAPI(
    title="ARM: Web scraping exercise",
    description="Awesome util to scraping webs!",
    version="1.0"
)
v1 = app

@v1.get("/get_href")
def get_href():
    return web_scraper.get_href('https://www.geeksforgeeks.org/')

@v1.get("/get_requests_launched")
def get_requests_launched():
    return list_request_log_dict.get_entity_list()

@v1.get("/get_requests_launched_information")
def get_requests_launched_information():
    print(get_request_log_dict.get_entity())
    return get_request_log_dict.get_entity()

app.mount("/api/v1", v1)

def startApiService():
    uvicorn.run("api.runner:app", host="0.0.0.0", port=8080)