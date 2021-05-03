"""
Construct menu widget with the parent MASTER.

Valid resource names:
    activebackground, activeborderwidth,
    activeforeground, background, bd, bg, borderwidth, cursor,
    disabledforeground, fg, font, foreground, postcommand, relief,
    selectcolor, takefocus, tearoff, tearoffcommand, title, type.

"""

import tkinter as tk

def donothing():
    print('I will do nothing')


root = tk.Tk()

# Create the menu bar
menubar = tk.Menu(root)

# Prepares a group of items for the menu (like a list of commands)
filemenu = tk.Menu(menubar, tearoff=0)

# Adds options to the group created
filemenu.add_command(label="New", command=donothing, accelerator='Ctrl + N', underline=0)
filemenu.add_command(label="Open", command=donothing, accelerator='Ctrl + O')
filemenu.add_command(label="Save", command=donothing, accelerator='Ctrl + S')
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

# Create a separator in the menu
filemenu.add_separator()
# Adds more commands after the separator
filemenu.add_command(label="Exit", command=root.quit)

# Finally assigns the group created to the menu bar
menubar.add_cascade(label="File", menu=filemenu)

# Creates another item to the menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

# Yet another
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

# Some other types of Menus
# menu_types = tk.Menu(menubar, tearoff=0)
# option = tk.BooleanVar(value=1)
# menu_types.add_checkbutton(label="Option to Select/Deselect", variable=option)
# themes_menu = ('Black', 'White', 'High Contrast')
# menu_types.add_cascade(label="Themes", menu=themes_menu)
# theme_var = tk.StringVar()
# themes_menu.add_radiobutton(label="Default White", variable=theme_var)

# And finally the menu bar is shown (kind of gridded)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
