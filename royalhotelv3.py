from sense_hat import SenseHat
import time
import socket
from datetime import datetime

sense = SenseHat()
sense.clear()
sense.low_light = True


minucheck = [00, 10, 20, 30, 40, 50, 60]
even = [00, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]


#Netvaerkspakke
udp_port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
data = str("booting")
sock.sendto(bytes(data, "UTF-8"), ('<broadcast>', udp_port))


def repeat():
    global sock
    global datetime
    global minucheck
    global even
    temp =  sense.get_temperature()
    newtemp = round (temp, 1)
    minute = datetime.now().minute

    print (datetime.now().strftime("%H:%M:%S"))
    data = str("booting")
    sock.sendto(bytes(data, "UTF-8"), ('<broadcast>', udp_port))
    
    if minute in even:
        print (datetime.now().strftime("%H:%M:%S"))
        data2 = str("Current time: " + str(datetime.now())+ "/" + "Hotel ID: " + "1" + "/" + "Current temp: " + str(newtemp)))
        sock.sendto(bytes(data2, "UTF-8"), ('<broadcast>', udp_port))
        time.sleep(10)
        
    else:
        data3 = str("Ikke Sendt test")
        sock.sendto(bytes(data3, "UTF-8"), ('<broadcast>', udp_port))
        time.sleep(20)

while True:
    repeat()