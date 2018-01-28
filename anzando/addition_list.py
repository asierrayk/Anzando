from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.recycleview import RecycleView

from .addition import AnzanRoot, AnzanResult

Builder.load_file('anzando/addition_list.kv')

class AnzanList(RecycleView):
    current_number = StringProperty()
    numbers = ListProperty()

    def start(self):
        pass

    def end(self):
        self.parent.show_keyboard('keyboard_layout')




class AnzanListConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1, 6))))
    times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])


class AnzanListRoot(AnzanRoot):

    def __init__(self, **kwargs):
        super(AnzanListRoot, self).__init__(**kwargs)
        self.game_factory = Factory.AnzanList
        self.result_factory = Factory.AnzanResult
        self.configuration = Factory.AnzanListConfiguration()
        self.show_config()


class AnzanListScreen(Screen):
    pass
