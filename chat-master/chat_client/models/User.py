from chat_client.core import Model
from chat_client.core.AuthUser import AuthUser


class User(Model):

    login = None
    password = None
    status = False

    # проверяем на правельный ввод данных
    # return True or False
    def validate(self, data):
        if (data['login'] is None) or (data['password'] is None):
            return False
        login = data['login']
        password = data['password']
        if (len(login) < 4) or (len(login) > 155):
            self.error.update({"login": "Login must be > 4 and < 155"})

        if (len(password) < 4) or (len(password) > 55):
            self.error.update({"password": "Password must be > 4 and < 55"})

        if self.error == {}:
            self.login = login
            self.password = password
            self.status = True
            return True
        else:
            return False

    def loginUser(self):
        if self.status:
           if AuthUser.login(self.login,  self.password):
                return True
           else:
               return False
        else:
            return False
