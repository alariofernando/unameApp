FROM python:3.8-alpine

COPY ./app ./app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN chmod +x ./app/app.py
ENTRYPOINT [ "python3 ./app/app.py" ]