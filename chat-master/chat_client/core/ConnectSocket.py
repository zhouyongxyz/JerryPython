import json
import socket
from json import JSONDecodeError

from chat_client.core.Log import Log


class ConnectSocket:
    sock = None

    @staticmethod
    def instance():
        if ConnectSocket.sock is None:
            ConnectSocket.sock = socket.socket()
            ConnectSocket.sock.connect(('localhost', 9090))

    @staticmethod
    def send(data):
        data = json.dumps(data)
        ConnectSocket.sock.sendall(data.encode())
        return True

    @staticmethod
    def getData(byte):
        result = ConnectSocket.sock.recv(byte).decode()
        print('get' + result)
        Log.logFile(result, 'Get websocket, Json')
        try:
            result = json.loads(result)
        except JSONDecodeError as e:
            print(e)
        return result
