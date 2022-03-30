import tkinter as tk
from tkinter import ttk

####################################################################################################
# Main Window
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

####################################################################################################
# Frame 1 - tkinter widgets
frame_1 = tk.Frame(root)
frame_1.grid(row=0, column=0, sticky='nsew', ipadx=5, ipady=5)
frame_1.columnconfigure(0, weight=1)

################
# Buttons
for i in range(3):
    button = tk.Button(frame_1, text=f'Button {i}')
    button.grid(row=i, column=0, sticky='nsew')
###############
# labels
for i in range(3):
    label = tk.Label(frame_1, text=f'Label {i}', anchor='center')
    label.grid(row=i+3, column=0, sticky='nsew')
###############
# Entry
for i in range(3):
    entry = tk.Entry(frame_1, justify='center')
    entry.grid(row=i+6, column=0, sticky='nsew')
###############
# Check Buttons
for i in range(3):
    var = tk.IntVar()
    checkbutton = tk.Checkbutton(frame_1, variable=var, text=f'Check Button {i}')
    checkbutton.grid(row=i+9, column=0, sticky='nsew')
###############
# Radiobutton
var = tk.IntVar()
for i in range(3):
    radio_button = tk.Radiobutton(frame_1, text=f'Radio Button {i}', value=i, variable=var)
    radio_button.grid(row=i+12, column=0, sticky='nsew')
################
# Scale
h_scale = tk.Scale(frame_1, from_=-10, to=10, orient='horizontal')
h_scale.grid(row=15, column=0, sticky='nsew', padx=10)


####################################################################################################
# Frame 2 - TTK widgets
frame_2 = ttk.Frame(root, padding=10)
frame_2.grid(row=0, column=1, sticky='nsew')
frame_2.columnconfigure(0, weight=1)

################
# Buttons
for i in range(3):
    button = ttk.Button(frame_2, text=f'Button {i}')
    button.grid(row=i, column=0, sticky='nsew')
###############
# labels
for i in range(3):
    label = ttk.Label(frame_2, text=f'Label {i}', anchor='center')
    label.grid(row=i+3, column=0, sticky='nsew')
###############
# Entry
for i in range(3):
    entry = ttk.Entry(frame_2, justify='center')
    entry.grid(row=i+6, column=0, sticky='nsew')
###############
# Check Buttons
for i in range(3):
    var = tk.IntVar()
    checkbutton = ttk.Checkbutton(frame_2, variable=var, text=f'Check Button {i}')
    checkbutton.grid(row=i+9, column=0, sticky='nsew')
###############
# Radiobutton
var = tk.IntVar()
for i in range(3):
    radio_button = ttk.Radiobutton(frame_2, text=f'Radio Button {i}', value=i, variable=var)
    radio_button.grid(row=i+12, column=0, sticky='nsew')
################
# Scale
h_scale = ttk.Scale(frame_2, from_=-10, to=10, orient='horizontal')
h_scale.grid(row=15, column=0, sticky='nsew', padx=10)

if __name__ == '__main__':
    root.mainloop()
