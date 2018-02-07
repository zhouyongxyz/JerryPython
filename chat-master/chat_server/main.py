#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import socket
import datetime

import pymysql.cursors
from bson import json_util

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'db': 'chat',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}

connect = pymysql.connect(**config)


def server():
    print("Run server")
    sock = socket.socket()
    sock.bind(("", 9090))
    while True:
        sock.listen(10)
        conn, addr = sock.accept()
        print(addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            result = parseCommand(data)
            result = json.dumps(result, default=json_util.default)
            conn.send(result.encode())


def parseCommand(data):
    data = json.loads(data.decode())
    if "login" in data:
        sql = "Select id, login, nickname FROM user WHERE login = %s AND password = %s"
        params = data['login']
        return sendQuery(sql, (params['login'], params['password'])).fetchone()
    if "get_message" in data:
        sql = "SELECT `messages`.`id`, `text`, `nickname`, `date` " \
              "FROM `messages` " \
              "INNER JOIN `user` ON (`user`.`id` = `id_user`) " \
              "ORDER BY `date` DESC " \
              "LIMIT %s"
        params = data['get_message']
        data = sendQuery(sql, (params['count'])).fetchall()
        i = 0
        result = {}
        while i < len(data):
            result.update({i: data[i]})
            i += 1
        print(result)
        return result

    if "message" in data:
        sql = "INSERT INTO messages (`date`, `id_user`, `text`, `room_id`) VALUES (%s, %s, %s, %s)"
        params = data['message']
        return sendQuery(sql, (params['date'], params['id_user'], params['text'], params['room_id']), "insert")


def sendQuery(sql, data, type='select'):
        with connect.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, data)
            if type == 'select':
                return cursor
            if type == 'insert':
                connect.commit()
        return True

if __name__ == '__main__':
    server()