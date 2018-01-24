from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition
from kivy.factory import Factory
from kivy.clock import Clock

from anzan import anzan_addition

import time

__version__ = '0.0.0'

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
class AnzanRoot(BoxLayout):
    configuration = ObjectProperty()
    game_factory = ObjectProperty()
    result_factory = ObjectProperty()
    elapsed_time = NumericProperty(0)

    def show_config(self):
        self.clear_widgets()
        self.add_widget(self.configuration)

    def new_exercise(self):
        self.numbers, self.result = anzan_addition(
            digits=int(self.configuration.digits.text),
            times=int(self.configuration.times.text),
            negative=self.configuration.negative.active,
            fixed=self.configuration.fixed.active)

    def show_exercise(self):
        self.clear_widgets()
        game = self.game_factory(self.numbers)
        self.start_time = time.perf_counter()
        self.add_widget(game)

    def next_exercise(self):
        self.new_exercise()
        self.show_exercise()

    def repeat_exercise(self):
        self.clear_widgets()
        game = self.game_factory(self.numbers)
        self.add_widget(game)

    def show_keyboard(self, keyboard_layout):
        self.clear_widgets()
        keyboard = Factory.AnzanKeyboard()
        self.add_widget(keyboard)

    def check_answer(self, answer):
        self.answer = answer
        self.clear_widgets()
        self.elapsed_time = time.perf_counter() - self.start_time
        check = self.result_factory(self.result, self.answer, self.elapsed_time)
        self.add_widget(check)

    def go_back(self):
        App.get_running_app().root.current = 'anzan_menu'

class AnzanConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1,6))))
    times_values = ListProperty(["3","4","5","7","10","15","25","100"])

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
            if self.negative:
                self.negative = not self.negative
        elif len(str(abs(self.number))) == 1:
            self.number = None
        elif self.negative:
            self.number = -(self.number // -10)
        else:
            self.number = self.number // 10

    def ok(self):
        if self.number is not None:
            self.parent.check_answer(self.number)

class AnzanResult(BoxLayout):
    mark = StringProperty()
    result = NumericProperty()
    answer = NumericProperty()
    elapsed_time = NumericProperty()

    def __init__(self, result, answer, elapsed_time, **kwargs):
        super(AnzanResult,self).__init__(**kwargs)
        self.result = result
        self.answer = answer
        self.elapsed_time = elapsed_time

        if self.answer == self.result:
            self.mark = 'Correct!'
        else:
            self.mark = 'Wrong'


# FLASH #
class AnzanFlash(BoxLayout):
    current_number = StringProperty()

    def __init__(self, numbers, **kwargs):
        super(AnzanFlash,self).__init__(**kwargs)
        self.iter_numbers = iter(numbers)
        self.flash_event = Clock.schedule_interval(self.next_number, 0.5)

    def next_number(self, dt):
        print(dt)
        print(type(dt))
        try:
            n = next(self.iter_numbers)
            self.current_number = str(n)
        except StopIteration:
            self.flash_event.cancel()
            self.parent.show_keyboard('keyboard_layout')

class AnzanFlashConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1,6))))
    times_values = ListProperty(["3","4","5","7","10","15","25","100"])

class AnzanFlashRoot(AnzanRoot):

    def __init__(self, **kwargs):
        super(AnzanFlashRoot,self).__init__(**kwargs)
        self.game_factory = Factory.AnzanFlash
        self.result_factory = Factory.AnzanResult
        self.configuration = Factory.AnzanFlashConfiguration()
        self.show_config()

class AnzanFlashScreen(Screen):
    pass

# MANUAL #
class AnzanManual(BoxLayout):
    current_number = StringProperty()

    def __init__(self, numbers, **kwargs):
        super(AnzanManual,self).__init__(**kwargs)
        self.iter_numbers = iter(numbers)
        self.next_number()

    def next_number(self):
        try:
            n = next(self.iter_numbers)
            self.current_number = str(n)
        except StopIteration:
            self.parent.show_keyboard('keyboard_layout')

class AnzanManualConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1,6))))
    times_values = ListProperty(["3","4","5","7","10","15","25","100"])

class AnzanManualRoot(AnzanRoot):

    def __init__(self, **kwargs):
        super(AnzanManualRoot,self).__init__(**kwargs)
        self.game_factory = Factory.AnzanManual
        self.result_factory = Factory.AnzanResult
        self.configuration = Factory.AnzanManualConfiguration()
        self.show_config()

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
