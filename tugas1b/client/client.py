import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9998)
print('connecting to %s port %s' % server_address , file=sys.stderr)
sock.connect(server_address)

file = open('HelloClient.txt','wb')

# try:
#     # sock.sendall(file_send)
#     # fl_send = file.read(1024)
#     # print('sending file to server',file=sys.stderr)
message = 'request file'
sock.sendall(message.encode())
# finally:
#     print("closing")
#     sock.shutdown(2)
#     sock.close()
while True:
    file_receive = sock.recv(1024)
    # print(file_receive)
    while file_receive:
        file.write(file_receive)
        file_receive = sock.recv(1024)
        print('file from server received' , file=sys.stderr)
    file.close()
    sock.shutdown(2)
    sock.close()
    break
