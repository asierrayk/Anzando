from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (ObjectProperty,
                             NumericProperty,
                             StringProperty,
                             BooleanProperty,
                             ListProperty)
from kivy.factory import Factory

import utils

import time


class AnzanRoot(BoxLayout):
    configuration = ObjectProperty()
    game_factory = ObjectProperty()
    result_factory = ObjectProperty()
    total_elapsed_time = NumericProperty(0)
    exercise_elapsed_time = NumericProperty(0)
    answer_elapsed_time = NumericProperty(0)

    hits = NumericProperty(0)
    fails = NumericProperty(0)

    current_streak = NumericProperty(0)
    best_session_streak = NumericProperty(0)

    def show_config(self):
        self.clear_widgets()
        self.add_widget(self.configuration)
        self.current_streak = 0
        self.best_session_streak = 0

    def new_exercise(self):
        self.numbers, self.result = utils.addition_exercise(
            digits=int(self.configuration.digits.text),
            times=int(self.configuration.times.text),
            negative=self.configuration.negative.active,
            fixed=self.configuration.fixed.active)

    def show_exercise(self):
        self.clear_widgets()
        self.game = self.game_factory(numbers=self.numbers)
        self.add_widget(self.game)
        self.start_time = time.time()
        self.game.start()

    def next_exercise(self):
        self.new_exercise()
        self.show_exercise()

    def repeat_exercise(self):
        self.clear_widgets()
        self.add_widget(self.game)
        self.start_time = time.time()
        self.game.start()

    def show_keyboard(self, keyboard_layout):
        self.end_time = time.time()
        self.clear_widgets()
        keyboard = Factory.AnzanKeyboard()
        self.add_widget(keyboard)

    def check_answer(self, answer):
        self.answer_time = time.time()
        self.total_elapsed_time = self.answer_time - self.start_time
        self.answer_elapsed_time = self.answer_time - self.end_time
        self.exercise_elapsed_time = self.end_time - self.start_time

        self.answer = answer
        self.is_correct = (self.answer == self.result)

        if self.is_correct:
            self.hits += 1
            self.current_streak += 1
            if self.current_streak > self.best_session_streak:
                self.best_session_streak = self.current_streak
        else:
            self.fails += 1
            self.current_streak = 0

        self.clear_widgets()
        check = self.result_factory(
            is_correct=self.is_correct,
            result=self.result, answer=self.answer,
            total_elapsed_time=self.total_elapsed_time,
            exercise_elapsed_time=self.exercise_elapsed_time,
            answer_elapsed_time=self.answer_elapsed_time,
            current_streak=self.current_streak,
            best_session_streak=self.best_session_streak,
            hits=self.hits,
            fails=self.fails)

        self.add_widget(check)

    def go_back(self):
        App.get_running_app().root.current = 'anzan_menu'
        self.show_config()


class AnzanConfiguration(BoxLayout):
    digits_values = ListProperty(map(str, list(range(1, 6))))
    times_values = ListProperty(["3", "4", "5", "7", "10", "15", "25", "100"])


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
    is_correct = BooleanProperty()
    result = NumericProperty()
    answer = NumericProperty()
    total_elapsed_time = NumericProperty()
    exercise_elapsed_time = NumericProperty()
    answer_elapsed_time = NumericProperty()
    current_streak = NumericProperty()
    best_session_streak = NumericProperty()
    hits = NumericProperty()
    fails = NumericProperty()
