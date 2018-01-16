from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition
from kivy.factory import Factory

from anzan import anzan_addition

####### MENUS #######
class MainMenuScreen(Screen):
    pass

class AnzanMenuScreen(Screen):
    pass

class DateMenuScreen(Screen):
    pass

class SettingsMenuScreen(Screen):
    pass

####### ANZAN #######

class AnzanKeyboard(BoxLayout):
    number = NumericProperty(None, allownone=True)
    answer_text = StringProperty('')
    negative = BooleanProperty(False)

    def on_negative(self, instance, value):
        print(instance, value)
        if self.negative:
            self.answer_text = '-'
        else:
            self.answer_text = ''

    def on_number(self, instance, value):
        print(instance, value)
        if self.number is None:
            self.answer_text = '-' if self.negative else ''
        else:
            self.answer_text = str(value)
        # self.answer.text = str(self.number)

    def key_press(self, key):
        number_pressed = -int(key) if self.negative else int(key)

        if self.number is None:
            self.number = number_pressed
        else:
            self.number = self.number*10 + number_pressed

    def minus(self):
        self.negative = not self.negative
        if self.number is not None:
            self.number = - self.number

    def clear(self):
        if self.number is None:
            print('none')
            if self.negative:
                print('negative')
                self.negative = not self.negative
        elif len(str(abs(self.number))) == 1:
            print('one_digit')
            self.number = None
        elif self.negative:
            print('more digits negative')
            self.number = -(self.number // -10)
        else:
            print('more digits positive')
            self.number = self.number // 10



# FLASH #
class AnzanFlash(BoxLayout):
    pass

class AnzanFlashRoot(BoxLayout):
    pass

class AnzanFlashScreen(Screen):
    pass

# MANUAL #
class AnzanManual(BoxLayout):
    current_number = StringProperty()
    numbers, result = anzan_addition()
    it = iter(numbers)

    def next_number(self):
        try:
            n = next(self.it)
            self.current_number = str(n)
        except StopIteration:
            self.parent.show_keyboard('keyboard_layout')

class AnzanManualRoot(BoxLayout):
    def show_keyboard(self, keyboard_layout):
        self.clear_widgets()
        keyboard = Factory.AnzanKeyboard()
        # keyboard.layout = keyboard_layout
        self.add_widget(keyboard)

class AnzanManualScreen(Screen):
    pass

# AUDIO #
class AnzanAudioScreen(Screen):
    pass

# ENDURANCE #
class AnzanEnduranceScreen(Screen):
    pass

# DRAG #
class AnzanDragScreen(Screen):
    pass


####### APP #######
class AnzanToolApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainMenuScreen(name='main_menu'))

        sm.add_widget(AnzanMenuScreen(name='anzan_menu'))
        sm.add_widget(AnzanManualScreen(name='play_manual_anzan'))
        sm.add_widget(AnzanAudioScreen(name='play_audio_anzan'))
        sm.add_widget(AnzanFlashScreen(name='play_flash_anzan'))

        sm.add_widget(DateMenuScreen(name='date_menu'))

        sm.add_widget(SettingsMenuScreen(name='settings_menu'))

        return sm

if __name__ == '__main__':
    AnzanToolApp().run()
