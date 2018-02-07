from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


class Login(Screen):

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        if self._validate(loginText, passwordText):

            app.username = loginText
            app.password = passwordText

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'chat'

            app.config.read(app.get_application_config())
            app.config.write()
        else:
            app.error = self.error

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def _validate(self, login, password):
        if login and password:
            return True
        self.error = 'Please fill in the field'
        return False
