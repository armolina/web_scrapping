FROM python:3.8-slim

COPY . /home/app
WORKDIR /home/app

EXPOSE 8081

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

ENTRYPOINT python3 app.py