#################################################################################################
"""
Tkinter provides classes which allow the display, positioning and
control of widgets.

Toplevel widgets are Tk and Toplevel.

Other widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton, Menu, Image, Photoimage,
Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox, LabelFrame and PanedWindow.

Properties of the widgets are specified with keyword arguments.
Keyword arguments have the same name as the corresponding resource under Tk.

Widgets are positioned with one of the geometry managers Place, Pack or Grid.
These managers can be called with methods place, pack, grid available in every Widget.

Actions are bound to events by resources (e.g. keyword argument command) or with the method bind.
"""

#################################################################################################
"""
General sequence for creation
Import tkinter (tk suggested as a nickname)
"""

import tkinter as tk

"""
Create top level window - Tk()
Each application has one and only one Tk() entity (base window)
Other windows, if needed, shall be created as: w = tk.Toplevel()
"""

root = tk.Tk()  # root is only the name of the widget

'''
Base and toplevel windows do not need to be placed/packed/grided

You may get the keys to the properties of the root with: print(root.keys())
['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 'background', 'bg',
'colormap', 'container', 'cursor', 'height', 'highlightbackground', 'highlightcolor',
'highlightthickness', 'padx', 'pady', 'takefocus', 'visual', 'width']
'''

"""
The application must be put under a loop
"""
root.mainloop()
