import socket
import binascii

UDP_IP = "192.168.1.247"
UDP_IP2 = "192.168.1.37"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size = 1024 bytes
	print "received message:", data
	if data <> " ":
	   break

#for i in range(0, len(data)):
#    print(data[i])
print(len(data))
print data[0]
print data[1]
print data[6]
print data[7]
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
   # print "Image text length:",len(imgtext)
   # imghdr="HDR"+str(len(imgtext))
   # sock.sendto(imglenencode, (UDP_IP, UDP_PORT))
    while (packetnum < 586):
          sock.sendto(imgtext[count1:count2], (UDP_IP2, UDP_PORT))
          count1 = count1 + 1024
          count2 = count2 + 1024
          packetnum = packetnum + 1
          
    
#    HOST = '127.0.0.1'
#    PORT = 5005
#    BUFSIZE = 1024
#    ADDR = (HOST, PORT)
#    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    serversock.bind(ADDR)
#    serversock.listen(SOMAXCONN)
#    fileOpen = open("/ece590/pingpgms/robot1.bmp")
#    g = f.read()
#    print 'Waiting For Connection..'
#    clientsock, addr = serversock.accept()
#    print 'Connection Established From: ', addr
#   clientsock.sendall(fileOpen)
else:
    print "Bad data!!! Please resend..."


