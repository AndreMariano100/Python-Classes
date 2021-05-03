# import kivy parts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    surname = ObjectProperty(None)

    def press(self):
        name = self.name.text
        surname = self.surname.text
        print(f'{name} {surname}')


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()