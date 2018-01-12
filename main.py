from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition

class MainMenuScreen(Screen):
    pass

class AnzanMenuScreen(Screen):
    pass

class AnzanFlash(BoxLayout):
    current_number = StringProperty()
    n = 0

    def next_number(self):
        print(self.current_number)
        self.n += 1
        self.current_number = str(self.n)

class AnzanFlashScreen(Screen):
    pass

class DateMenuScreen(Screen):
    pass

class SettingsMenuScreen(Screen):
    pass

# Create the screen manager

class AnzanToolApp(App):
    def build(self):
        pass
        # sm = ScreenManager(transition=NoTransition())
        # sm.add_widget(MainMenuScreen(name='main_menu'))

        # sm.add_widget(AnzanMenuScreen(name='anzan_menu'))
        # sm.add_widget(AnzanFlashScreen(name='play_flash_anzan'))

        # sm.add_widget(DateMenuScreen(name='date_menu'))

        # sm.add_widget(SettingsMenuScreen(name='settings_menu'))

        # return sm
        # return AnzanFlashScreen(name='play_flash_anzan')

if __name__ == '__main__':
    AnzanToolApp().run()
