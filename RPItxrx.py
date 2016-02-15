# This program has to be run on Raspberry PI

import socket
import binascii
import time

# IP address of Raspberry PI
UDP_IP = "192.168.1.170"

# IP address of the computer (Linux)
UDP_IP2 = "192.168.1.242"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size = 1024 bytes
	print "received message:", data
	if data <> " ":
	   break

packetnum = 0
count1 = 0
count2 = 1024
if (len(data)==8 and data[0]=="<" and data[1]=="*" and data[6]=="." and data[7]==">"):
    print "Command Received for Left  Motor : ",data[2:4]
    print "Command Recieved for Right Motor : ",data[4:6]
    filename = '/home/pi/Downloads/robot1.bmp'
    with open(filename, 'rb') as f:
         content = f.read()
#    print(binascii.hexlify(content))
    imgtext = binascii.hexlify(content)
    while (packetnum < 586):
          # To reduce packet drops at the listening end
          time.sleep (20.0 / 1000.0);
          sock.sendto(imgtext[count1:count2], (UDP_IP2, UDP_PORT))
          count1 = count1 + 1024
          count2 = count2 + 1024
          packetnum = packetnum + 1
          
else:
    print "Bad data!!! Please resend..."


