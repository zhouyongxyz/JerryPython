from datetime import datetime

from chat_client.core.AuthUser import AuthUser
from chat_client.core.ConnectSocket import ConnectSocket
from chat_client.core import Model


class Chat(Model):

    def getMessages(self, count):
        ConnectSocket.send({'get_message': {'count': count}})

        # получаем ответ от сервера
        result = ConnectSocket.getData(10024)
        return result

    def sendMessage(self, message):
        date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        ConnectSocket.send({'message': {'text': message, "date": date, "id_user": AuthUser.id, "room_id": 1}})
        return True
