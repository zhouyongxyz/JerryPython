#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz
# clienttest.py
# just return the recv message and append "done" message

import socket
import sys
import time
import json

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
                head = str(sock.recv(5), "utf-8")
                # Receive data from the server and shut down
                print("recv = " + head)
                len = str(sock.recv(5), "utf-8")
                print("len = " + len)
                data = str(sock.recv(int(len)), "utf-8")
                #sock.sendall(bytes(received.strip() + " done" + "\n", "utf-8"))
                print("data = " + data)
                jsonobj = json.loads(data)
                print("lua = " + jsonobj["lua"])
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