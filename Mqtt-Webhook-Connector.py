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
    MQTTtopic = data['deviceid']
    MQTTmessage = json.dumps(data['message'],separators=(',', ':'))
    MQTTtags = ','.join(data['tags'])
    publish.single('all-odin/' + MQTTtopic, MQTTmessage, hostname=host)
    # Units running old firmware
    if '2000' in data['tags']:
        publish.single('odin-old-firmware', data['devicename'], hostname=host)
    # This is for Masterton2020 (_TAG_9274_)
    if '_TAG_9274_' in data['tags']:
        publish.single('masterton2020/' + MQTTtopic, MQTTmessage, hostname=host)
        if 'report' in data['tags']:
            publish.single('masterton2020/restart', data['devicename'], hostname=host)
    # This is for Arrowtown2020 (_TAG_9180_)
    if '_TAG_9180_' in data['tags']:
        publish.single('arrowtown2020/' + MQTTtopic, MQTTmessage, hostname=host)
        if 'report' in data['tags']:
            publish.single('arrowtown2020/restart', data['devicename'], hostname=host)
        if 'fw_update_status_uptodate' in data['tags']:
            publish.single('arrowtown2020/firmwareOK', data['devicename'], hostname=host)
    # This is for Invercargill2020 (_TAG_9286_)
    if '_TAG_9286_' in data['tags']:
        publish.single('invercargill2020/' + MQTTtopic, MQTTmessage, hostname=host)
        if 'report' in data['tags']:
            publish.single('invercargill2020/restart', data['devicename'], hostname=host)
    # This is for Reefton2020 (_TAG_9650_)
    if '_TAG_9650_' in data['tags']:
        publish.single('reefton2020/' + MQTTtopic, MQTTmessage, hostname=host)
        if 'report' in data['tags']:
            publish.single('reefton2020/restart', data['devicename'], hostname=host)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
