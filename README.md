# Plex-Mqtt-Connector
**This fork is customised for a specific application, not, I repeat, NOT for general use out of the box**
The basic idea is to turn webhooks into items published to a MQTT server.

This specific fork is to support the dataflow of NIWA's low-cost air quality sensor ODIN. If you have questions, get in touch with Gustavo Olivares AT niwa.co.nz

## Example

For example you can connect OpenHAB to Plex with this script. Plex will send it's webhooks to your local machine on port 5000. The script will receive this webhooks and publish a part of the content into a topic on your MQTT-Server. Items in your OpenHAB instance are able to show the latest message (player state, title and type of the media).

If you use rules you are able to dim your lights everytime a movie or episode of your favorite series begins. Also you can turn on your lights after the player stopped.

## Requirements

You can use this script on your local machine. But this machine has to be turned on everytime you wanna use this function. Otherwise you could use a Raspberry Pi.

Don't forget to install the Python packages and Python itself.

Also you have to install a MQTT-Server on any machine. E. g. Mosquitto

---

Clone or fork this repo to add functions.

And don't forget to take a look at [Hobbyblogging](https://hobbyblogging.de). Thank you!