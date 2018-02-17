from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivy.uix import settings
from kivy.config import ConfigParser
from version import __version__

class MainMenuScreen(Screen):
    pass


class AnzanMenuScreen(Screen):
    pass


class DateMenuScreen(Screen):
    pass


class SettingsMenuScreen(Screen):
    pass


class ScreenMan(ScreenManager):
    pass


class AnzandoApp(App):
    use_kivy_settings = False

    def build(self):
        self.settings_cls = settings.SettingsWithTabbedPanel
        return ScreenMan(transition=NoTransition())

    def build_config(self, config):
        config.setdefaults('main', {
            'name': 'player1',
            'language': 'English'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Settings',
            self.config, filename='settings.json')

if __name__ == '__main__':
    AnzandoApp().run()
