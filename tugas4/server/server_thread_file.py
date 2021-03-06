from socket import *
import socket
import threading
import logging
import time
import sys

from file_machine import FileMachine

fm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data=b''
            while True:
                dataa = self.connection.recv(100)
                if not dataa:
                    break
                data+=dataa
            if data:
                dd=b'a'
                if(len(data.split(b'split', 1))==2):
                    dd, data = data.split(b'split', 1)
                d = data.decode()
                cstring = d.split(" ")
                # print(cstring)
                # print(d)
                # print(dd)
                command = cstring[0].strip()
                hasil = fm.proses(d, dd)
                if(command == "download"):
                    # print('a')
                    self.connection.sendall(hasil)
                elif (command == "list"):
                    self.connection.sendall(hasil.encode())
                elif(command == "upload"):
                    self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('localhost', 10000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

