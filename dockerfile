FROM python:3.8-slim-buster
ADD Mqtt-Webhook-Connector.py .
RUN pip install flask-restful paho-mqtt requests

CMD [ "python", "./Mqtt-Webhook-Connector.py" ]
