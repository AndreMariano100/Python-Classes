# import kivy parts
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set number of columns
        self.cols = 1

        # Second grid layout
        self.top_grid = GridLayout()
        # self.top_grid = GridLayout(
        #     row_force_default=True,
        #     row_default_height=40,
        #     col_force_default=True,
        #     col_default_width=100
        # )
        self.top_grid.cols = 2
        self.add_widget(self.top_grid)

        # Create and add widgets
        self.name_text = Label(text='Name: ',
                               size_hint_y=None, height=30,
                               size_hint_x=None, width=100
                               )
        self.top_grid.add_widget(self.name_text)
        self.name_input = TextInput(multiline=False,
                                    size_hint_y=None, height=30,
                                    size_hint_x=None, width=200
                                    )
        self.top_grid.add_widget(self.name_input)

        self.surname_text = Label(text='Surname: ',
                                  size_hint_y=None, height=30,
                                  size_hint_x=None, width=100
                                  )
        self.top_grid.add_widget(self.surname_text)
        self.surname_input = TextInput(multiline=False,
                                       size_hint_y=None, height=30,
                                       size_hint_x=None, width=200
                                       )
        self.top_grid.add_widget(self.surname_input)

        # Create the button
        self.button = Button(text='Save Name', font_size=32,
                             size_hint_y=None, height=50,
                             size_hint_x=None, width=200)
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