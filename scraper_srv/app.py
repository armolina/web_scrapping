import os

from actions import persistance_request_log_dict
from entrypoints import fast_api, auto_scraper

if "URL_TO_SCRAP" in os.environ:
    auto_scraper.AutoScrap.auto_web_scrap(os.environ["URL_TO_SCRAP"])
else:
    fast_api.startApiService()