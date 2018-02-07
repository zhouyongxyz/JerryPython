class Auth:

    def viewLogin(self):
        login = input('Enter login:')
        password = input('Enter password:')
        return {"login": login, "password": password}

    def login(self, data):
        print(data.error)