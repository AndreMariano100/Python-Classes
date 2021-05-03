# import kivy parts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('images.kv')

class MyExercise(Widget):
    pass

class TestAndLearn(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyExercise()


if __name__ == '__main__':
    TestAndLearn().run()
