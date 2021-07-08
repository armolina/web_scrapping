# web_scrapping
Currently, this application has two different ways to work:
- First, if we set URL_TO_SCRAP=any_existent_url environment variable the application does an automatic scrap of this url and prints on screen the existent hrefs links.
- Second, if we don't set URL_TO_SCRAP environment variable the application launch an uvicorn service with a FastAPI application.

## Initialice application
```
docker-compose --build
```
## Api swagger documentation
```
http://127.0.0.1:8081/api/v1/docs
```