# import kivy parts
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('design_builder_color.kv')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    surname = ObjectProperty(None)

    def press(self):
        name = self.name.text
        surname = self.surname.text
        print(f'{name} {surname}')


class WhateverName(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    WhateverName().run()
