import socket
s1,s2 = (socket(socket.AF_INET,socket.SOCK_STREAM),socket(socket.AF_INET,socket.SOCK_STREAM))
cheat1 = (s1.connect((server1,port)) + s2.connect((server2,port)) + s1.send('user taiiwo 8 *\r\n') + s2.send('user taiiwo 8 *\r\n') + s1.send('join #channel1\r\n'))
while l:
	s2.send("privmsg #channel2 :" + str(s1.recv(1024)) + "\r\n")
