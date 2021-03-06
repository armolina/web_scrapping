import os

from entrypoint import fast_api, auto_scraper

if "URL_TO_SCRAP" in os.environ:
    auto_scraper.AutoScrap.auto_web_scrap(os.environ["URL_TO_SCRAP"])
else:
    fast_api.startApiService()