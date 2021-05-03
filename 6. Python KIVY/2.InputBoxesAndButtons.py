# import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set number of columns
        self.cols = 2

        # Add widgets
        self.name_text = Label(text='Name: ')
        self.add_widget(self.name_text)
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.surname_text = Label(text='Surname: ')
        self.add_widget(self.surname_text)
        self.surname_input = TextInput(multiline=False)
        self.add_widget(self.surname_input)

        self.button = Button(text='Save Name')
        self.button.bind(on_press=self.press)
        self.add_widget(self.button)

    def press(self, instance):
        name = self.name_input.text
        surname = self.surname_input.text
        print(f'{name} {surname}')


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()