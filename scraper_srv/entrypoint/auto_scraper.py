import json
from controller.request_log import RequestLog

class AutoScrap():
    def auto_web_scrap(url: str):
        print("================================================")
        print("Docker URL_TO_SCRAP received, getting hrefs...")
        request_log = RequestLog.persist_request_log(str)
        print(request_log["uuid"])
        print(json.dumps(request_log["payload"], indent=2))
        print("Scraping complete")
        print("================================================")