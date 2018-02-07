import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

from Chat import Chat
from Login import Login
from connected import Connected


class ChatApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Chat(name='chat'))

        return manager

    def get_application_config(self):
        if not self.username:
            return super(ChatApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if not os.path.exists(conf_directory):
            os.makedirs(conf_directory)

        return super(ChatApp, self).get_application_config(
            '%s/config.cfg' % conf_directory
)

if __name__ == '__main__':
    ChatApp().run()
