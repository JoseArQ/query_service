FROM python:3.8

WORKDIR /query_service

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

COPY ./app ./app

CMD ["python3", "./app/main.py"]

