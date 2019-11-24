FROM python:2.7.15-alpine

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "main.py", "192.168.25.36"]

