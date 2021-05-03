# import kivy parts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('text_colors.kv')

class MyExercise(Widget):
    pass

class TestAndLearn(App):
    def build(self):
        return MyExercise()


if __name__ == '__main__':
    TestAndLearn().run()
