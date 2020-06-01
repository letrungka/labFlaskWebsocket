FROM python:3.7-alpine3.10
COPY . .
RUN pip install -r requirements.txt
CMD python labwebsocket.py