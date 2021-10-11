import socket	#for sockets
import sys	#for exit

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print('Failed to create socket')
	sys.exit()

host = 'localhost'
port = 8888

while 1:
	msg = input('Enter message to send : ')
	
	try :
		#Set the whole string
		s.sendto(msg.encode(), (host, port))

		if msg == "exit":
			print("Client exit")
			break
		
		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		reply = d[0].decode()
		addr = d[1]
		print('Server reply : ' + reply)

	except socket.error as msg:
		print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()

    