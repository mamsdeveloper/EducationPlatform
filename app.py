# do not replace imports 
# this import order fix kivy Config bag

from kivy.config import Config
from config import config

Config.read(config.APP_CONFIG)
Config.write()

from kivymd.app import MDApp

from widgets.main_widget import MainWidget


class Application(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self) -> MainWidget:
        """Configure kivy core, set app options, create main widget

        Returns:
            MainWidget: main application widget

        """
        
        self.title = config.TITLE
        self.main_widget = MainWidget()

        return self.main_widget


if __name__ == '__main__':
    Application().run()