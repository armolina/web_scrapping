import os
import json

from actions import persistance_request_log_dict
from api import runner

if "URL_TO_SCRAP" in os.environ:
    print("================================================")
    print("Docker URL_TO_SCRAP received, getting hrefs...")
    request_log = persistance_request_log_dict.persist_request_log(os.environ["URL_TO_SCRAP"])
    print(request_log["uuid"])
    print(json.dumps(request_log["payload"], indent=2))
    print("Scraping complete")
    print("================================================")

else:
    print("initialize API")
    runner.startApiService()