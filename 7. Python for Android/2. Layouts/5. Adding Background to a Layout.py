"""
https://kivy.org/doc/stable/guide/widgets.html

Adding a Background to a Layout

One of the frequently asked questions about layouts is:
    "How to add a background image/color/video/... to a Layout"

Layouts by their nature have no visual representation: they have no canvas instructions by default.
However you can add canvas instructions to a layout instance easily, as with adding a colored background:

In Python:

    from kivy.graphics import Color, Rectangle

    with layout_instance.canvas.before:
        Color(0, 1, 0, 1) # green; colors range from 0-1 instead of 0-255
        self.rect = Rectangle(size=layout_instance.size,
                               pos=layout_instance.pos)

Unfortunately, this will only draw a rectangle at the layout’s initial position and size.
To make sure the rect is drawn inside the layout, when the layout size/pos changes, we need to listen to any
changes and update the rectangles size and pos. We can do that as follows:

    with layout_instance.canvas.before:
        Color(0, 1, 0, 1) # green; colors range from 0-1 instead of 0-255
        self.rect = Rectangle(size=layout_instance.size,
                               pos=layout_instance.pos)

    def update_rect(instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    # listen to size and position changes
    layout_instance.bind(pos=update_rect, size=update_rect)

In kv:

    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 1, 0, 1
            Rectangle:
                # self here refers to the widget i.e BoxLayout
                pos: self.pos
                size: self.size

The kv declaration sets an implicit binding: the last two kv lines ensure that the pos and size values of
the rectangle will update when the pos of the floatlayout changes.

Now we put the snippets above into the shell of Kivy App.

Pure Python way:
"""
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MainApp().run()

"""
Using the kv Language:

from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Button:
        text: 'Hello World!!'
        size_hint: .5, .5
        pos_hint: {'center_x':.5, 'center_y': .5}
''')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()

"""