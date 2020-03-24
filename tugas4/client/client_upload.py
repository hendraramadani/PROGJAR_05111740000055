import sys
import socket
import os

def c_upload(sock,command,Filename):
    if os.path.isfile("../File Client/" + Filename):
        data = "split" + command + " " + Filename
        print("Sending: " + Filename)
        File = open("../File Client/" + Filename, "rb")
        data_encode = data.encode("utf-8")
        datasend = File.read() + data_encode
        print(datasend)
        sock.send(datasend)
        sock.shutdown(socket.SHUT_WR)
        hasil = sock.recv(10).decode()
        print(hasil)
    else:
        print("File not Exist")

    print("Closing Upload Process")