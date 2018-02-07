from chat_client.core import Controller
from chat_client.models.Chat import Chat
from chat_client.view.ChatView import ChatView


class ChatController(Controller):

    def index(self):
        model = Chat()
        return self.render(ChatView(), 'view', model.getMessages(25))

    def sendMessage(self, message):
        model = Chat()
        model.sendMessage(message)
        return self.render(ChatView(), 'send')