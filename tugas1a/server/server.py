import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 9998)
print('starting up on %s port %s' % server_address , file=sys.stderr)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
file = open('HelloServer.txt','wb')
while True:
	# Wait for a connection
	print('waiting for a connection' , file=sys.stderr)
	connection, client_address = sock.accept()
	print('connection from', client_address , file=sys.stderr)
	# Receive the data in small chunks and retransmit it
	file_receive=connection.recv(1024)
	while file_receive:
		file.write(file_receive)
		file_receive = connection.recv(1024)
		print('file from client received' , file=sys.stderr)
	# Clean up the connection
	file.close
	connection.shutdown(2)
	connection.close()
	sock.close()
	break

