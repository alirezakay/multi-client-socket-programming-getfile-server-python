# pylint: disable-all

import socket               # Import socket module
import _thread as thread
import re
import os


ROOT="./"
def on_new_client(clientsocket, addr):
    print(addr, ' Connected')
    while True:
        msg = clientsocket.recv(1024)
        msg = msg.decode()
        if re.match(r'.*(\r\n)|(\n)$', msg):
            break

    msg = msg.split("\r\n")[0]            
    if os.path.exists(ROOT+msg):
        file = open(ROOT+msg, "rb")
        size = os.path.getsize(ROOT+msg)
        clientsocket.send("200".encode()) # code
        clientsocket.send(str(msg).split(".")[len(str(msg).split("."))-1].encode()) # type
        clientsocket.send(str(size).encode()) # size
        clientsocket.send((file.read()))
    else:
        clientsocket.send("404".encode())
        clientsocket.send("No File !!!".encode())

    print(addr, ' X ')
    clientsocket.close()

def main():
    s = socket.socket()         # Create a socket object
    host = "127.0.0.1"          # localhost
    port = 80                # Reserve a port for your service.

    print('Server started!')
    print('Waiting for clients...')

    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.

    while True:
        c, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        thread.start_new_thread(on_new_client, (c, addr))

    s.close()


main()


