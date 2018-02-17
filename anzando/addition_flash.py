from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang.builder import Builder

from .addition import AnzanRoot, AnzanResult

import time

Builder.load_file('anzando/addition_flash.kv')

class AnzanFlash(BoxLayout):
    current_number = StringProperty()
    numbers = ListProperty()
    delay = NumericProperty(1)

    def start(self):
        self.current_number = ''
        self.iter_numbers = iter(self.numbers)
        self.flash_event = Clock.schedule_interval(
            self.next_number, self.delay)

    def blink(self):
        self.number.opacity = 0
        anim = Animation(opacity=1, duration=0.2*self.delay, t='in_out_expo')
        anim.start(self.number)

    def next_number(self, dt):
        print(dt)
        try:
            self.blink()
            n = next(self.iter_numbers)
            self.current_number = str(n)
        except StopIteration:
            self.flash_event.cancel()
            self.parent.show_keyboard('keyboard_layout')


class AnzanFlashConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1, 6))))
    times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])
    delay_values = ListProperty(["1",
                                 "0.9",
                                 "0.8",
                                 "0.7",
                                 "0.6",
                                 "0.5",
                                 "0.4",
                                 "0.3"])


class AnzanFlashRoot(AnzanRoot):

    def __init__(self, **kwargs):
        super(AnzanFlashRoot, self).__init__(**kwargs)
        self.game_factory = Factory.AnzanFlash
        self.result_factory = Factory.AnzanResult
        self.configuration = Factory.AnzanFlashConfiguration()
        self.show_config()

    def show_exercise(self):
        self.clear_widgets()
        self.game = self.game_factory(
            numbers=self.numbers, delay=float(
                self.configuration.delay.text))
        self.start_time = time.time()
        self.add_widget(self.game)
        self.game.start()


class AnzanFlashScreen(Screen):
    pass
