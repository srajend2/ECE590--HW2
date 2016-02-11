import socket
import time
import re
import os

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
					 
MESSAGE = "<*5050.>" #Motor control message
#'<*' is to notify header symbols and '.>' is to notify trailer symbols
# the first two digits represent the speed of the left motor
# the next two digits represent the speed of the right motor
# The numbers represent the scale of 1 to 100:
# 50 = motor stop
# 51 to 99 = forward direction of motor, lowest speed at 51 and max speed at 99
# 1 to 49 = reverse direction of motor, lowest speed at 1 and max speed at 49

ip = "192.168.1.247"
ip1 = "192.168.1.37"
port = 5005
port1 = 5006

sock.sendto(MESSAGE, (ip, port))
print "Sent 1 packet to %s through port %s successfully"%(ip, port)

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
sock.bind((ip1, port))

packetnum = 0
receivedimg = " "
while (packetnum < 586):
	data, addr = sock.recvfrom(1024) 
       # if data[0,3]=="HDR":
       #    r = re.compile("([a-zA-Z]+)([0-9]+)")
       #    m = r.match(data)
       ##    m.group(1)
       #    imglen= m.group(2)
        if data <> " ":
           packetnum = packetnum + 1
           print "Received Packet %s", packetnum
           receivedimg = receivedimg + data
       	   pass

print "Received Image!!!, length is %s", len(receivedimg)
reformatimg = receivedimg[0,599029]
print "Reformatted Image!!!, length is ", len(reformatimg)
#path1 = "ece590/pingpgms"
#os.chdir( path1 )
#file1 = 'ece590/pingpgms/rcvdrobot1.bmp'
fo = open("ece590/pingpgms/rcvdrobot1.bmp",'wb')
print "Name of the file: ", fo.name
fo.write(receivedimg);
fo.close()	

file2 = "ece590/pingpgms/robot1.bmp"
import webbrowser
webbrowser.open(file2)

