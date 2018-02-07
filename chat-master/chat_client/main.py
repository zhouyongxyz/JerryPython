#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from chat_client.controllers.AuthController import AuthController
from chat_client.controllers.ChatController import ChatController
from chat_client.controllers.ErrorController import ErrorController
from chat_client.core import Route
from chat_client.core.AuthUser import AuthUser
from chat_client.core.ConnectSocket import ConnectSocket


def main():
    status = True
    try:
        ConnectSocket.instance()
        while status:
            try:
                if AuthUser.AUTH_LOGIN is None:
                    data = Route.go(AuthController(), 'viewLogin')
                    Route.go(AuthController(), 'login', data)
                else:
                    data = Route.go(ChatController(), 'index')
                    Route.go(ChatController(), 'sendMessage', data)
            except BaseException as e:
                Route.go(ErrorController(), 'index', e)
    except ConnectionRefusedError as e:
        Route.go(ErrorController(), 'index', e)


if __name__ == '__main__':
    ''' Main endpoint '''
    sys.exit(main())