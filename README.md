# web_scrapping
Currently, this application has two different ways to work:
- First, if we set URL_TO_SCRAP=any_existent_url environment variable the application does an automatic scrap of this url and prints on screen the existent hrefs links.
- Second, if we don't set URL_TO_SCRAP environment variable the application launch an uvicorn service with a FastAPI application.


docker-compose.yml to runfrom docker and scrap URL_TO_SCRAP automatically
```
version: "3.3"

services:
    mongodb:
        image : mongo
        environment:
            - PUID=1000
            - PGID=1000
        volumes:
            - /mongodb/database:/data/db
        ports:
            - 27017:27017
        restart: unless-stopped
    scraper_srv:
        build: ./scraper_srv
        ports: 
            - "8081:8080"
        environment: 
            - URL_TO_SCRAP=https://www.xataka.com/
            - DB_HOST=mongodb
```

docker-compose.yml to execute uvicorn service with Scraping API inside.
```
version: "3.3"

services:
    mongodb:
        image : mongo
        environment:
            - PUID=1000
            - PGID=1000
        volumes:
            - /mongodb/database:/data/db
        ports:
            - 27017:27017
        restart: unless-stopped
    scraper_srv:
        build: ./scraper_srv
        ports: 
            - "8081:8080"
        environment: 
            - DB_HOST=mongodb
```


## Initialice application
```
docker-compose --build
```
## Api swagger documentation
```
http://127.0.0.1:8081/api/v1/docs
```

# Prepare environment

Crate a workspace folder, for example:

```
$ mkdir ~/workspaces
```

Download project from repository
```
$ git clone https://github.com/armolina/web_scrapping.git
```

Crate local environment to work isolated from operative system
```
$ cd scraper_srv
$ python3 -m venv env #linux
$ .\env\Scripts\activate #windows
$ source /env/bin/activate
```

Install project requirements
```
$ pip3 install -r requirements.txt
```

Export sysvar with mongodb IP
```
$ export DB_HOST=127.0.0.1
```

Run application and take fun!
```
$ pyton3 app.py
```

# Testing and coverage
## Lauch tests
```
coverage run -m --rcfile=.coveragec pytest
```
## View coverage report
```
coverage report --rcfile=.coveragec -m
```