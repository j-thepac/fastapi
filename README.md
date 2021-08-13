# FAST API (https://fastapi.tiangolo.com/)


## Features

1.  Asynchronous
2.  High Perfromance
3.  Less Code
4.  Data Type  and Data Models auto Conversions
5.  Auto Documentation
    - swagger (/docs)
    - ReDoc   (/redoc)

## pre-req:
make sure venv is on.

## steps :

 - cd to the folder containing main.py
  
 - pip install fastapi
  
 - pip install uvicorn #server
  
 

## To Execute :
- uvicorn main:app --reload --host 0.0.0.0 --port 5000

## requirements.txt
fastapi
uvicorn


## dockerfile
FROM python:3.8-slim
COPY $PWD /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
CMD uvicorn main:app --reload --host 0.0.0.0 --port 5000


