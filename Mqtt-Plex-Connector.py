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
    print('Something is coming')
    data = request.json
    MQTTtopic = data['topic']
    MQTTmessage = json.dumps(data['message'],separators=(',', ':'))
    MQTTtags = ','.join(data['tags'])
    publish.single(MQTTtopic, MQTTmessage, hostname=host)
    publish.single(MQTTtopic + '/tags', MQTTtags, hostname=host)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
