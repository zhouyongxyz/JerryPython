#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# clienttest.py
# just return the recv message and append "done" message

import socket
import sys
import time

HOST, PORT = "localhost", 9008
data = "connecting"
data2 = "reconnecting"

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    try:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
        while 1:
            # inputStr = input("input：");
            # print("input = " + inputStr)
            # Receive data from the server and shut down
            try:
                received = str(sock.recv(1024), "utf-8")
                # Receive data from the server and shut down
                print("recv :" + received)
                sock.sendall(bytes(received.strip() + " done" + "\n", "utf-8"))
            except:
                print("except try to reconnect server ...")
                time.sleep(2)
                try:
                    sock.connect((HOST, PORT))
                    sock.sendall(bytes(data2 + "\n", "utf-8"))
                except:
                    pass
    except:
        print("except try to reconnect server ...")
        time.sleep(2)
        try:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data2 + "\n", "utf-8"))
        except:
            pass

print("client exit")