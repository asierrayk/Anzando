from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.animation import Animation

from .addition import AnzanRoot, AnzanResult

Builder.load_file('anzando/addition_manual.kv')

class AnzanManual(BoxLayout):
    current_number = StringProperty()
    numbers = ListProperty()

    def __init__(self, **kwargs):
        super(AnzanManual, self).__init__(**kwargs)
        self.start()

    def start(self):
        self.iter_numbers = iter(self.numbers)
        self.next_number()

    def next_number(self):
        try:
            n = next(self.iter_numbers)
            self.current_number = str(n)
        except StopIteration:
            self.parent.show_keyboard('keyboard_layout')

    def blink(self):
        self.number.opacity = 0
        anim = Animation(opacity=1, duration=0.1, t='in_out_expo')
        anim.start(self.number)


class AnzanManualConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1, 6))))
    times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])


class AnzanManualRoot(AnzanRoot):

    def __init__(self, **kwargs):
        super(AnzanManualRoot, self).__init__(**kwargs)
        self.game_factory = Factory.AnzanManual
        self.result_factory = Factory.AnzanResult
        self.configuration = Factory.AnzanManualConfiguration()
        self.show_config()


class AnzanManualScreen(Screen):
    pass
