"""
https://kivy.org/doc/stable/api-kivy.uix.stacklayout.html#module-kivy.uix.stacklayout

The StackLayout arranges children vertically or horizontally, as many as the layout can fit.
The size of the individual children widgets do not have to be uniform.

For example, to display widgets that get progressively larger in width:

root = StackLayout()
for i in range(25):
    btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
    root.add_widget(btn)


"""