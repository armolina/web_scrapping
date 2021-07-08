import os
import uvicorn
from scrapers import web_scraper
from api import runner

if "URL_TO_SCRAP" in os.environ:
    print("Docker URL_TO_SCRAP received, getting hrefs...")
    print(web_scraper.get_href(os.environ["URL_TO_SCRAP"]))
else:
    print("initialize API")
    runner.startApiService()