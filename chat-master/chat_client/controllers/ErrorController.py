from chat_client.core import Controller
from chat_client.view.Error import Error


class ErrorController(Controller):

    def index(self, error):
        return self.render(Error(), 'index', error)