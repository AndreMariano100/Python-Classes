import tkinter as tk


def read_values():
    number = entry_1_var.get()
    text = entry_2_var.get()
    entry_1_var.set('')
    entry_2_var.set('')
    label.configure(text=f'Number:{number} / Text:{text}')


# Functions that will allow only float input from the user
def float_only(action, value_if_allowed, text):
    permitted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', '+']
    if action == '1':
        if text in permitted:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
    else:
        return True


# Functions that will allow only char input from the user
def string_only(action, text):
    if action == '1':
        if text.isalpha() or text == ' ':
            return True
        else:
            return False
    else:
        return True


root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# The callback functions must be registered in tkinter
validate_numbers = root.register(float_only)
validate_strings = root.register(string_only)

'''
Callback substitution codes
'%d' 	Action code:
        0 for an attempted deletion,
        1 for an attempted insertion,
        -1 if the callback was called for focus in, focus out, or a change to the textvariable.
'%i' 	When the user attempts to insert or delete text,
        this argument will be the index of the beginning of the insertion or deletion.
        If the callback was due to focus in, focus out, or a change to the textvariable,
        the argument will be -1.
'%P' 	The value that the text will have if the change is allowed.
'%s' 	The text in the entry before the change.
'%S' 	If the call was due to an insertion or deletion, this argument will be the text
        being inserted or deleted.
'%v' 	The current value of the widget's validate option.
'%V' 	The reason for this callback: one of 'focusin', 'focusout', 'key', or 'forced'
        if the textvariable was changed.
'%W' 	The name of the widget. 
'''

entry_1_var = tk.StringVar()
entry_1 = tk.Entry(root, textvariable=entry_1_var, justify='center', width=20,
                   validate='all', validatecommand=(validate_numbers, '%d', '%P', '%S'))

entry_2_var = tk.StringVar()
entry_2 = tk.Entry(root, textvariable=entry_2_var, justify='center', width=20,
                   validate='all', validatecommand=(validate_strings, '%d', '%S'))

entry_1.grid(row=0, column=0, sticky='nsew')
entry_2.grid(row=0, column=1, sticky='nsew')

button = tk.Button(root, text='Read Values', command=read_values)
button.grid(row=1, column=0, columnspan=2, sticky='nsew')

label = tk.Label(root, text='Values')
label.grid(row=2, column=0, columnspan=2, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()
