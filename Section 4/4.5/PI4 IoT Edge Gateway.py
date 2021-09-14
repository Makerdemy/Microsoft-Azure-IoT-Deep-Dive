import random  
import time  
import paho.mqtt.client as mqtt 
  
from azure.iot.device import IoTHubDeviceClient, Message  
  
CONNECTION_STRING = "Connection_String Here"  
  
client = mqtt.Client() 
client.on_connect = on_connect 
client.connect("<BROKER IP >", 1883, 60) 

client.subscribe("downstreamdevice1/temperature")
temperature1 = msg.payload
client.subscribe("downstreamdevice1/humidity")
humidity1 = = msg.payload

client.subscribe("downstreamdevice2/temperature")
temperature2 = msg.payload
client.subscribe("downstreamdevice2/humidity")
humidity2 = = msg.payload


MSG_TXT1 = '{{"device1temperature": {temperature1},"device1humidity": {humidity1}}}' 
MSG_TXT2 = '{{"device2temperature": {temperature2},"device2humidity": {humidity2}}}'
  
def iothub_client_init():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def iothub_client_telemetry_run():  
    try:  
        client = iothub_client_init()  
        print ( "IoT Hub device sending messages, press Ctrl-C to exit" )  
        while True:  
            msg_txt_formatted = MSG_TXT1.format(temperature1=temperature1, humidity1=humidity1)  
            message = Message(msg_txt_formatted)  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(3)
			
			msg_txt_formatted = MSG_TXT2.format(temperature2=temperature2, humidity2=humidity2)  
            message = Message(msg_txt_formatted)  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(3)  
  
    except KeyboardInterrupt:  
        print ( "IoTHubClient sample stopped" )  
  
if __name__ == '__main__':  
    print ( "Press Ctrl-C to exit" )  
    iothub_client_telemetry_run()  