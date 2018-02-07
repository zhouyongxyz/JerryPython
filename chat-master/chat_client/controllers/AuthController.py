from chat_client.core import Controller
from chat_client.models.User import User
from chat_client.view.Auth import Auth


class AuthController(Controller):

    def viewLogin(self):
        """

        :rtype: object
        """
        return self.render(Auth(), 'viewLogin')

    # метод для авторизации юзера
    # @params login string
    # @params password string
    def login(self, data=None):
        user = User()
        if user.validate(data):
            return user.loginUser()
        return self.render(Auth(), 'login', user)

    def logout(self):
        # TODO: add logout user
        pass



