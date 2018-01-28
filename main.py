from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
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
    def build(self):
        return ScreenMan(transition=NoTransition())


if __name__ == '__main__':
    AnzandoApp().run()
