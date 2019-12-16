BROADCAST_TO_PORT = 5005
import time
from socket import *
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
sense.clear()

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
	temp = round (sense.get_temperature(), 1)
	data = str('{"HotelID":"0","Temperature":"'+ str(temp) +'"}' )
	sock.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(data)
	print (datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
	#time.sleep(10)
	time.sleep(600)




