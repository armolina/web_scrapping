import json
from actions import persistance_request_log_dict

class AutoScrap():
    def auto_web_scrap(url: str):
        print("================================================")
        print("Docker URL_TO_SCRAP received, getting hrefs...")
        request_log = persistance_request_log_dict.persist_request_log(str)
        print(request_log["uuid"])
        print(json.dumps(request_log["payload"], indent=2))
        print("Scraping complete")
        print("================================================")