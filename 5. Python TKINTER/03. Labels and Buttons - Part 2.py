# ---------------------------------------------------------------------------------------------
# App Imports
import tkinter as tk


# ---------------------------------------------------------------------------------------------
# App Buttons Functions
def action_1():
    # Get the present value with        value = w.cget('text')
    # Writes the value with             w.config(text='value')

    labels = (label_1, label_2, label_3)
    for label in labels:
        number = int(label.cget('text'))
        number += 1
        label.config(text=number)


def action_2():
    # Get the present value with        var.get()
    # Writes the value with             var.set()

    _vars = (var_4, var_5, var_6)
    for var in _vars:
        number = var.get()
        number += 1
        var.set(number)


# ---------------------------------------------------------------------------------------------
# Main Window
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# ---------------------------------------------------------------------------------------------
# Add first label frame
label_frame_1 = tk.LabelFrame(root, text='Changing with config()')
label_frame_1.grid(row=0, column=0)
label_frame_1.columnconfigure(0, weight=1)

# Add Labels
label_1 = tk.Label(label_frame_1, text='1')
label_2 = tk.Label(label_frame_1, text='2')
label_3 = tk.Label(label_frame_1, text='3')

label_1.grid(row=0, column=0, sticky='nsew')
label_2.grid(row=1, column=0, sticky='nsew')
label_3.grid(row=2, column=0, sticky='nsew')

# Add button
button_1 = tk.Button(label_frame_1, text='Change Labels', padx=10, pady=3, command=action_1)
button_1.grid(row=3, column=0, sticky='nsew')


# ---------------------------------------------------------------------------------------------
# Add second label frame
label_frame_2 = tk.LabelFrame(root, text='Changing with tk.StringVar()')
label_frame_2.grid(row=0, column=1)
label_frame_2.columnconfigure(0, weight=1)

# Add Labels
var_4 = tk.IntVar(value=1)
var_5 = tk.IntVar(value=2)
var_6 = tk.IntVar(value=3)

label_4 = tk.Label(label_frame_2, textvariable=var_4, anchor='center')
label_5 = tk.Label(label_frame_2, textvariable=var_5, anchor='center')
label_6 = tk.Label(label_frame_2, textvariable=var_6, anchor='center')

label_4.grid(row=0, column=0, sticky='nsew')
label_5.grid(row=1, column=0, sticky='nsew')
label_6.grid(row=2, column=0, sticky='nsew')

# Add button
button_2 = tk.Button(label_frame_2, text='Change Labels', padx=10, pady=3, command=action_2)
button_2.grid(row=3, column=0, sticky='nsew')


# ---------------------------------------------------------------------------------------------
if __name__ == '__main__':
    root.mainloop()

"""
Variables to control the "values" within tkinter:
    my_string = StringVar()
    my_boolean = BooleanVar()
    option = IntVar()
    volume = DoubleVar()

Use the variables when building the widgets:
    Entry(root, textvariable = my_string)
    Checkbutton(root, text="Remember Me", variable=my_boolean)
    Radiobutton(root, text="Option1", variable=option, value="option1")
    Scale(root, label="Volume Control", variable=volume, from =0, to=10)

Read / Adjust the values with the get/set methods

    my_string.set('value')              # and not my_string = 'value
    my_boolean.set(False)               # and not my_boolean = False
    option.set(3)                       # and not option = 3
    volume.set(30.0)                    # and not volume = 30.0
    
    new_string = my_string.get()        # and not new_string = my_string
    button_state = my_boolean.get()     # and not button_state = my_boolean
    new_option = option.get()           # and not new_option = option
    current_volume = volume.get()       # and not current_volume = volume
    

"""