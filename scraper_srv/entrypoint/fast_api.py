from entity.request_log import request_log
import uvicorn
from fastapi import FastAPI, HTTPException

from entity.post_body import PostBody
from entity.post_response import post_response
from controller.request_log import RequestLog

app = FastAPI(
    title="ARM: Web scraping 1.0",
    description="Awesome util to scraping webs!",
    version="1.0"
)
v1 = app

@v1.post("/get_href")
def get_href(post_body:PostBody):
    if(post_body.url!=''):
        request_log = RequestLog(post_body.url)
        response = request_log.persist_request_log()
        return post_response(response["uuid"], response["payload"])
    else:
        raise HTTPException(status_code=400, detail="Some needed parameter is null")

@v1.get("/get_requests_launched")
def get_requests_launched():
    request_log = RequestLog()
    return request_log.get_request_log_list()

@v1.get("/get_requests_launched_information/")
def get_requests_launched_information(request_log_id: str = ""):
    request_log = RequestLog()
    return request_log.get_request_log(request_log_id)

app.mount("/api/v1", v1)

def startApiService():
    uvicorn.run("entrypoint.fast_api:app", host="0.0.0.0", port=8088)