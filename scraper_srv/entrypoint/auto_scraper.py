import json
from controller.request_log import RequestLog

class AutoScrap():
    def auto_web_scrap(url: str):
        print("================================================")
        print("Docker URL_TO_SCRAP received, getting hrefs...")
        request_log = RequestLog(url)
        result = request_log.persist_request_log()
        print(result["uuid"])
        print(json.dumps(result["payload"], indent=2))
        print("Scraping complete")
        print("================================================")