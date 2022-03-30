import kivy
from kivy.app import App
from kivy.uix.label import Label
# The uix module is the section that holds the user interface elements like layouts and widgets.

kivy.require('2.0.0')  # replace with your current kivy version !


# It’s required that the base Class of your App inherits from the Kivy App class
class MyApp(App):

    # Build method from Kivy App Class
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':

    # The entry point to the app is by calling the run() method.
    MyApp().run()
