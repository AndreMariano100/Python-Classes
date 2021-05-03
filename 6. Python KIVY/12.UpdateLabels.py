# import kivy parts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('update_labels.kv')

class MyExercise(Widget):
    def press(self):
        data = self.ids.data_input.text
        self.ids.data_label.text = data
        self.ids.data_input.text = ''

class TestAndLearn(App):
    def build(self):
        return MyExercise()


if __name__ == '__main__':
    TestAndLearn().run()
