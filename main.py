from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.animation import Animation

import utils

import time

from version import __version__

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


# class AnzanRoot(BoxLayout):
#     configuration = ObjectProperty()
#     game_factory = ObjectProperty()
#     result_factory = ObjectProperty()
#     total_elapsed_time = NumericProperty(0)
#     exercise_elapsed_time = NumericProperty(0)
#     answer_elapsed_time = NumericProperty(0)

#     def show_config(self):
#         self.clear_widgets()
#         self.add_widget(self.configuration)

#     def new_exercise(self):
#         self.numbers, self.result = utils.addition_exercise(
#             digits=int(self.configuration.digits.text),
#             times=int(self.configuration.times.text),
#             negative=self.configuration.negative.active,
#             fixed=self.configuration.fixed.active)

#     def show_exercise(self):
#         self.clear_widgets()
#         self.game = self.game_factory(numbers=self.numbers)
#         self.add_widget(self.game)
#         self.start_time = time.time()
#         self.game.start()

#     def next_exercise(self):
#         self.new_exercise()
#         self.show_exercise()

#     def repeat_exercise(self):
#         self.clear_widgets()
#         self.add_widget(self.game)
#         self.start_time = time.time()
#         self.game.start()

#     def show_keyboard(self, keyboard_layout):
#         self.end_time = time.time()
#         self.clear_widgets()
#         keyboard = Factory.AnzanKeyboard()
#         self.add_widget(keyboard)

#     def check_answer(self, answer):
#         self.answer_time = time.time()
#         self.total_elapsed_time = self.answer_time - self.start_time
#         self.answer_elapsed_time = self.answer_time - self.end_time
#         self.exercise_elapsed_time = self.end_time - self.start_time

#         self.answer = answer
#         self.clear_widgets()
#         check = self.result_factory(
#             result=self.result, answer=self.answer,
#             total_elapsed_time=self.total_elapsed_time)
#         self.add_widget(check)

#     def go_back(self):
#         App.get_running_app().root.current = 'anzan_menu'


# class AnzanConfiguration(BoxLayout):
#     digits_values = ListProperty(map(str, list(range(1, 6))))
#     times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])


# class AnzanKeyboard(BoxLayout):
#     number = NumericProperty(None, allownone=True)
#     answer_text = StringProperty('')
#     negative = BooleanProperty(False)

#     def on_negative(self, instance, value):
#         print(instance, value)
#         if self.negative:
#             self.answer_text = '-'
#         else:
#             self.answer_text = ''

#     def on_number(self, instance, value):
#         print(instance, value)
#         if self.number is None:
#             self.answer_text = '-' if self.negative else ''
#         else:
#             self.answer_text = str(value)

#     def key_press(self, key):
#         number_pressed = -int(key) if self.negative else int(key)

#         if self.number is None:
#             self.number = number_pressed
#         else:
#             self.number = self.number*10 + number_pressed

#     def minus(self):
#         self.negative = not self.negative
#         if self.number is not None:
#             self.number = - self.number

#     def clear(self):
#         if self.number is None:
#             if self.negative:
#                 self.negative = not self.negative
#         elif len(str(abs(self.number))) == 1:
#             self.number = None
#         elif self.negative:
#             self.number = -(self.number // -10)
#         else:
#             self.number = self.number // 10

#     def ok(self):
#         if self.number is not None:
#             self.parent.check_answer(self.number)


# class AnzanResult(BoxLayout):
#     mark = StringProperty()
#     result = NumericProperty()
#     answer = NumericProperty()
#     total_elapsed_time = NumericProperty()

#     def __init__(self, **kwargs):
#         super(AnzanResult, self).__init__(**kwargs)

#         if self.answer == self.result:
#             self.mark = 'Correct!'
#         else:
#             self.mark = 'Wrong'


# FLASH #
# class AnzanFlash(BoxLayout):
#     current_number = StringProperty()
#     numbers = ListProperty()
#     delay = NumericProperty(1)

#     def __init__(self, **kwargs):
#         super(AnzanFlash, self).__init__(**kwargs)

#     def start(self):
#         self.iter_numbers = iter(self.numbers)
#         self.flash_event = Clock.schedule_interval(
#             self.next_number, self.delay)

#     def op(self, dt):
#         self.number.opacity = 1

#     def blink(self):
#         self.number.opacity = 0
#         anim = Animation(opacity=1, duration=0.2*self.delay, t='in_out_expo')
#         anim.start(self.number)

#     def next_number(self, dt):
#         print(dt)
#         try:
#             self.blink()
#             n = next(self.iter_numbers)
#             self.current_number = str(n)
#         except StopIteration:
#             self.flash_event.cancel()
#             self.parent.show_keyboard('keyboard_layout')


# class AnzanFlashConfiguration(BoxLayout):
#     digits_values = ListProperty(map(str, list(range(1, 6))))
#     times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])
#     delay_values = ListProperty(["1",
#                                  "0.9",
#                                  "0.8",
#                                  "0.7",
#                                  "0.6",
#                                  "0.5",
#                                  "0.4",
#                                  "0.3"])


# class AnzanFlashRoot(AnzanRoot):

#     def __init__(self, **kwargs):
#         super(AnzanFlashRoot, self).__init__(**kwargs)
#         self.game_factory = Factory.AnzanFlash
#         self.result_factory = Factory.AnzanResult
#         self.configuration = Factory.AnzanFlashConfiguration()
#         self.show_config()

#     def show_exercise(self):
#         self.clear_widgets()
#         self.game = self.game_factory(
#             numbers=self.numbers, delay=float(
#                 self.configuration.delay.text))
#         self.start_time = time.time()
#         self.add_widget(self.game)
#         self.game.start()


# class AnzanFlashScreen(Screen):
#     pass

# MANUAL #
# class AnzanManual(BoxLayout):
#     current_number = StringProperty()
#     numbers = ListProperty()

#     def __init__(self, **kwargs):
#         super(AnzanManual, self).__init__(**kwargs)
#         self.start()

#     def start(self):
#         self.iter_numbers = iter(self.numbers)
#         self.next_number()

#     def next_number(self):
#         try:
#             n = next(self.iter_numbers)
#             self.current_number = str(n)
#         except StopIteration:
#             self.parent.show_keyboard('keyboard_layout')


# class AnzanManualConfiguration(BoxLayout):
#     digits_values = ListProperty(map(str, list(range(1, 6))))
#     times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])


# class AnzanManualRoot(AnzanRoot):

#     def __init__(self, **kwargs):
#         super(AnzanManualRoot, self).__init__(**kwargs)
#         self.game_factory = Factory.AnzanManual
#         self.result_factory = Factory.AnzanResult
#         self.configuration = Factory.AnzanManualConfiguration()
#         self.show_config()


# class AnzanManualScreen(Screen):
#     pass


class ScreenMan(ScreenManager):
    pass

####### APP #######
class AnzandoApp(App):
    def build(self):
        return ScreenMan(transition=NoTransition())

if __name__ == '__main__':
    AnzandoApp().run()
