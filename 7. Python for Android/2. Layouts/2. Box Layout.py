"""
BoxLayout arranges children in a vertical or horizontal box.

To position widgets above/below each other, use a vertical BoxLayout:

layout = BoxLayout(orientation='vertical')
btn1 = Button(text='Hello')
btn2 = Button(text='World')
layout.add_widget(btn1)
layout.add_widget(btn2)

To position widgets next to each other, use a horizontal BoxLayout. In this example,
we use 10 pixel spacing between children; the first button covers 70% of the horizontal space, the second covers 30%:

layout = BoxLayout(spacing=10)
btn1 = Button(text='Hello', size_hint=(.7, 1))
btn2 = Button(text='World', size_hint=(.3, 1))
layout.add_widget(btn1)
layout.add_widget(btn2)

Kv Example:

BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'this on top'
    Label:
        text: 'this right aligned'
        size_hint_x: None
        pos_hint: {'right': 1}
    Label:
        text: 'this on bottom'


"""