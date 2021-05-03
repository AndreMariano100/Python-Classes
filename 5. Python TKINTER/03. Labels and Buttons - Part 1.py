'''
LABELS STANDARD OPTIONS
    activebackground, activeforeground, anchor, background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground, highlightbackground, highlightcolor,
    highlightthickness, image, justify, padx, pady, relief, takefocus, text,
    textvariable, underline, wraplength

WIDGET-SPECIFIC OPTIONS
    height, state, width

    anchor => 'center', 'e', 'w', 'n', 's', 'ne', 'se', 'sw', 'nw'
    relief => 'flat', 'raised', 'sunken', 'groove', 'ridge'
    justify => 'left', 'center', 'right'
    compound => 'top', 'bottom', 'left', 'right', 'center', 'none'


BUTTON STANDARD OPTIONS
    activebackground, activeforeground, anchor, background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground, highlightbackground, highlightcolor,
    highlightthickness, image, justify, padx, pady, relief, repeatdelay,
    repeatinterval, takefocus, text, textvariable, underline, wraplength

WIDGET-SPECIFIC OPTIONS
    command, compound, default, height, overrelief, state, width

WIDGET METHODS
    button_name.flash() - alternate between active and normal color
    button_name.invoke() - invokes the command associated with the button

'''
# ---------------------------------------------------------------------------------------
# App Imports
import tkinter as tk


# ---------------------------------------------------------------------------------------
# App Buttons Functions
def action_1():
    print('Button 1 clicked')
    button_2.config(state='normal')


def action_2():
    print('Button 2 clicked')
    button_3.config(state='normal')


def action_3():
    print('Button 3 clicked')
    button_1.flash()
    button_2.config(state='disabled')
    button_3.config(state='disabled')


# ---------------------------------------------------------------------------------------
# Main Window
root = tk.Tk()
root.config(padx=5)
root.columnconfigure(0, weight=1)

# minsize=300

for i in range(8):
    root.rowconfigure(i, weight=1)

# Create Labels
label_1 = tk.Label(root, text='Label 1', bg='gray40')
label_2 = tk.Label(root, text='Label 2', bg='gray50')
label_3 = tk.Label(root, text='Label 3', bg='gray60')
label_4 = tk.Label(root, text='Label 4', bg='gray70')

# width = 50 -> assumed to be in characters
# height = 3 -> assumed to be in characters
# cursor='crosshair', bitmap='hourglass'
# compound='left
# bd=5, relief='ridge'

# Grid labels
label_1.grid(row=0, column=0, sticky='nsew')
label_2.grid(row=1, column=0, sticky='nsew')
label_3.grid(row=2, column=0, sticky='nsew')
label_4.grid(row=3, column=0, sticky='nsew')

# ------------------------------------------------------------------------------------------------
# Create buttons
button_1 = tk.Button(root, text='First Button', command=action_1)
button_1.grid(row=10, column=0, sticky='nsew')

button_2 = tk.Button(root, text='Second Button', state='disabled', command=action_2)
button_2.grid(row=11, column=0, sticky='nsew')

button_3 = tk.Button(root, text='Third Button', state='disabled', command=action_3)
button_3.grid(row=12, column=0, sticky='nsew')

button_4 = tk.Button(root, text='Quit', command=root.destroy)
button_4.grid(row=13, column=0, sticky='nsew')

# button_5 = tk.Checkbutton(root, text='A Check Button', indicatoron=0)
# button_5.grid(row=14, column=0, sticky='nsew')
#
# button_6 = tk.Button(root, text='Image Button', bitmap='@IMAGES/file_open.xbm', width=50)
# button_6.grid(row=15, column=0, sticky='nsew')

# background='yellow', foreground='pink'
# activebackground='green', activeforeground='blue'
# anchor='e'
# justify='left'
# padx = 10, pady=10
# underline=[0]
# wraplength=5 , '5c', '5i', '5m', '5p' (centimeter, inches, milimiter, printers point)
# command=action_1, command=quit
# state = 'normal', 'active', 'disabled
# disabledforeground='white'
# highlightbackground='green', highlightcolor='red', highlightthickness=10
# relief / overrelief: flat, groove, raised, ridge, solid, or sunken
# height, width
# repeatdelay=500, repeatinterval=100
# takefocus=0


"""
"command" keyword makes a reference to a method, does not call it.
Therefore no parenthesis shall be placed after the method name.

If the method requires any argument, we must use a "lambda" function:
command=method
command=lambda: method(argument)

"command" keyword responds to the left mouse click and to the space bar (not the return key).

For widgets that do not have a "command" keyword, actions shall be assigned with the BIND event method.
Bind assigned events may respond to any mouse click or to any keyboard key.
"""

if __name__ == '__main__':
    root.mainloop()
