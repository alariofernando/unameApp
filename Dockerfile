FROM jfloff/alpine-python:3.8

COPY ./app ./app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN chmod +x ./app/app.py
ENTRYPOINT [ "/usr/local/bin/python ./app/app.py" ]