from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json
import paho.mqtt.publish as publish

app = Flask(__name__)
api = Api(app)

host = 'localhost'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    MQTTtopic = data['devicename']
    MQTTmessage = json.dumps(data['message'],separators=(',', ':'))
    MQTTtags = ','.join(data['tags'])
    publish.single(MQTTtopic, MQTTmessage, hostname=host)
    publish.single(MQTTtopic + '/tags', MQTTtags, hostname=host)
    # This is for Masterton2020 (_TAG_9274_)
    if '_TAG_9274_' in data['tags']:
        publish.single('masterton2020/latest', MQTTtopic, hostname=host)
        if 'report' in data['tags']:
            publish.single('masterton2020/restart', MQTTtopic, hostname=host)
    # This is for Arrowtown2020 (_TAG_9180_)
    if '_TAG_9180_' in data['tags']:
        publish.single('arrowtown2020/latest', MQTTtopic, hostname=host)
        if 'report' in data['tags']:
            publish.single('arrowtown2020/restart', MQTTtopic, hostname=host)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
