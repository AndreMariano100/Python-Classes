"""
Construct an optionmenu widget with the parent MASTER, with
the resource textvariable set to VARIABLE, the initially selected
value VALUE, the other menu values VALUES and an additional
keyword argument command.
"""

import tkinter as tk


def menu_selected(event):
    print('Selection:', event)


master = tk.Tk()

variable = tk.StringVar()
choice_list = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
variable.set(choice_list[0])

menu = tk.OptionMenu(master, variable, *choice_list, command=menu_selected)
menu.grid()

if __name__ == '__main__':
    master.mainloop()
