'''

tkinter common message boxes

this module provides an interface to the native message boxes
available in Tk 4.2 and newer.

options (all have default values):
- default: which button to make default (one of the reply codes)
- icon: which icon to display (see below)
- message: the message to display
- parent: which window to place the dialog on top of
- title: dialog title
- type: dialog type; that is, which buttons to display (see below)

'''

#########################################################################################################
# App Imports
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import simpledialog

#########################################################################################################
# App Functions
def popup(selection):

    if selection == 'info':
        messagebox.showinfo(title='Necessary title', message='Your message comes here. Nothing too long.')

    elif selection == 'warning':
        messagebox.showwarning(title='Warning alert!', message='You have made a huge mistake!')

    elif selection == 'error':
        messagebox.showerror(title='Error Message', message='You made another mistake')

    elif selection == 'question':
        answer = messagebox.askquestion(title='Question!', message='Do you know the answer?')
        print('Answer:', answer)

    elif selection == 'ok/cancel':
        answer = messagebox.askokcancel(title='OK or Cancel!', message='Do you want to leave?')
        print('Answer:', answer)

    elif selection == 'yes/no':
        answer = messagebox.askyesno(title='Yes or Yes', message='Do you want to leave?')
        print('Answer:', answer)

    elif selection == 'color':
        color = colorchooser.askcolor()
        print('Color:', color)

    elif selection == 'simple':
        name = simpledialog.askstring('Input', 'What is your first name?', parent=root)
        age = simpledialog.askinteger('Input', 'What is your age?', parent=root)
        weight = simpledialog.askfloat('Input', 'What is your weight?', parent=root)
        print('Name:', name)
        print('Age:', age)
        print('Weight:', weight)


#########################################################################################################
# App GUIs
root = tk.Tk()
root.iconbitmap('Images/python.ico')
root.columnconfigure(0, weight=1)

for i in range(1, 9):
    root.rowconfigure(i, weight=1)

button1 = tk.Button(root, text='Show Info', command=lambda: popup('info'))
button1.grid(row=1, column=0, sticky='nsew')

button2 = tk.Button(root, text='Show Warning', command=lambda: popup('warning'))
button2.grid(row=2, column=0, sticky='nsew')

button3 = tk.Button(root, text='Show Error', command=lambda: popup('error'))
button3.grid(row=3, column=0, sticky='nsew')

button4 = tk.Button(root, text='Ask Question', command=lambda: popup('question'))
button4.grid(row=4, column=0, sticky='nsew')

button5 = tk.Button(root, text='Ask OK/CANCEL', command=lambda: popup('ok/cancel'))
button5.grid(row=5, column=0, sticky='nsew')

button6 = tk.Button(root, text='Ask YES/NO', command=lambda: popup('yes/no'))
button6.grid(row=6, column=0, sticky='nsew')

button7 = tk.Button(root, text='Why not...\nColor Chooser', command=lambda: popup('color'))
button7.grid(row=7, column=0, sticky='nsew')

button8 = tk.Button(root, text='Some small data collection', command=lambda: popup('simple'))
button8.grid(row=8, column=0, sticky='nsew')

#####################
# Run the App
if __name__ == "__main__":
    root.mainloop()
