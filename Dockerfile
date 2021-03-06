FROM python:3.8.7-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
