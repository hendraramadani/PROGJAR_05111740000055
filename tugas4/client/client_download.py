import sys
import socket
import os

def c_download(sock,command,Filename):
    Data = command+" "+Filename
    sock.send(Data.encode('utf-8'))
    sock.shutdown(socket.SHUT_WR)

    data = sock.recv(1024)
    if data == b'File not Exist':
        print("File not exist")
    else:
        f = open("../File Client/"+Filename, 'wb')
        while (data):
            f.write(data)
            data = sock.recv(1024)
        print("File Downloaded")
        f.close()
    print("Closing Download Process")