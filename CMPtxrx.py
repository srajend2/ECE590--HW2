
# This program has to be run on the computer (Linux)

import socket
import time
import re
import os
import binascii

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

#'<*' is to notify header symbols and '.>' is to notify trailer symbols
# the first two digits represent the speed of the left motor
# the next two digits represent the speed of the right motor
# The numbers represent the scale of 1 to 100:
# 50 = motor stop
# 51 to 99 = forward direction of motor, lowest speed at 51 and max speed at 99
# 1 to 49 = reverse direction of motor, lowest speed at 1 and max speed at 49
MESSAGE = "<*5050.>" #Motor control message

# IP address of Raspberry PI
ip = "192.168.1.170"

# IP address of the computer (Linux)
ip1 = "192.168.1.242"
port = 5005

sock.sendto(MESSAGE, (ip, port))
print "Sent 1 packet to %s through port %s successfully"%(ip, port)

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
sock.bind((ip1, port))

packetnum = 0
receivedimghex = " "
while (packetnum < 586):
	data, addr = sock.recvfrom(1024) 
        if data <> " ":
           packetnum = packetnum + 1
           print "Received Packet %s"%(packetnum)
           receivedimghex = receivedimghex + data
       	   pass

print "Received Image!!!, length is %s", len(receivedimghex)
reformatimg = receivedimghex[1:599029]
print "Reformatted Image!!!, length is ", len(reformatimg)
actualimg = binascii.unhexlify(reformatimg)

fo = open("ece590/pingpgms/rcvdrobotfin.bmp",'wb')
print "Name of the file: ", fo.name
fo.write(actualimg);
fo.close()	

file2 = "ece590/pingpgms/rcvdrobotfin.bmp"
import webbrowser
webbrowser.open(file2)

