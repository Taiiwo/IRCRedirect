import socket #gets the socket libs ready
s1 = socket(socket.AF_INET,socket.SOCK_STREAM)#makes a new socket called s1
s2 = socket(socket.AF_INET,socket.SOCK_STREAM)#makes a new socket called s2
s1.connect((server1,port))#Connects to s1
s2.connect((server2,port))#connects to s2
s1.send('user taiiwo 8 *\r\n')#logs in to s1
s2.send('user taiiwo 8 *\r\n')#logs in to s2
s1.send('join #channel1\r\n')#s1 joins channel 1
while 1 == True:#makes an infinite loop
	recv = s1.recv(1024)#fetches 1024 bits from IRC on s1
	s2.send("privmsg #channel2 :" + recv + "\r\n")#sends that data to a channel on s2
