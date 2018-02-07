import json

from datetime import datetime

from chat_client.core.ConnectSocket import ConnectSocket


class AuthUser:
    """ клас для манипуляции с юзером """

    AUTH_LOGIN = None
    time = "Y-m-s H:i:s"
    ipAddress = "127.0.0.1"
    nickname = None
    id = 0

    @staticmethod
    def login(login: object, password: object) -> object:

        ConnectSocket.send({"login": {"login": login, "password": password}})

        # получаем ответ от сервера
        result = ConnectSocket.getData(1024)

        if result is None:
            return False
        else:
            print(result)
            AuthUser.AUTH_LOGIN = result['login']
            AuthUser.time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
            AuthUser.ipAddress = "127.0.0.1"
            AuthUser.nickname = result['nickname']
            AuthUser.id = result['id']
            return True

    @staticmethod
    def isGuest():
        if AuthUser.AUTH_LOGIN is None:
            return True
        return False