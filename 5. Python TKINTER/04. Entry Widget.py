'''
Creates and entry type widget

Valid resource names:
    background, bd, bg, borderwidth, cursor,
    exportselection, fg, font, foreground, highlightbackground,
    highlightcolor, highlightthickness, insertbackground,
    insertborderwidth, insertofftime, insertontime, insertwidth,
    invalidcommand, invcmd, justify, relief, selectbackground,
    selectborderwidth, selectforeground, show, state, takefocus,
    textvariable, validate, validatecommand, vcmd, width,
    xscrollcommand.

WIDGET METHODS:
    w.get()
    w.insert(index, 'string')
    w.delete(first, last)
    w.delete(index)
    w.icursor(index)
'''

# App Imports
import tkinter as tk


######################################################################################################
# Program Functions
def calculate():
    var_1 = entry_101.get()
    var_2 = entry_102.get()
    result = float(var_1) + float(var_2)
    entry_103.delete(0, tk.END)
    entry_103.insert(0, result)

def delete_all():
    entry_101.delete(0, tk.END)
    entry_102.delete(0, tk.END)
    entry_103.delete(0, tk.END)
    entry_101.insert(0, '0')
    entry_102.insert(0, '0')
    entry_103.insert(0, '0')

def calculate_2():
    result_1.set(float(data_1.get()) + float(data_2.get()))

def delete_all_2():
    data_1.set(0)
    data_2.set(0)
    result_1.set(0)


######################################################################################################
# Constructs the Main Window
root = tk.Tk()

######################################################################################################
# Add the Frames to the Main Window
frame_1 = tk.LabelFrame(root, text='Reading from the widget')
frame_1.grid(row=0, column=0, sticky='nsew')
frame_2 = tk.LabelFrame(root, text='Using tk.StringVar()')
frame_2.grid(row=0, column=1, sticky='nsew')

######################################################################################################
# Configure and add widgets to the left frame
if True:
    label_100 = tk.Label(frame_1, text='User Main Data')
    label_100.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(10, 5))

    label_101 = tk.Label(frame_1, text='User Data 1:', anchor='e')
    label_101.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
    entry_101 = tk.Entry(frame_1, justify='center')
    entry_101.grid(row=1, column=1, sticky='nsew', padx=5)
    entry_101.insert(0, '0')

    label_102 = tk.Label(frame_1, text='User Data 2:', anchor='e')
    label_102.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
    entry_102 = tk.Entry(frame_1, justify='center')
    entry_102.grid(row=2, column=1, sticky='nsew', padx=5)
    entry_102.insert(0, '0')

    button_100 = tk.Button(frame_1, text='Calculate Sum', command=calculate)
    button_100.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)

    entry_103 = tk.Entry(frame_1, bg='white', justify='center', relief='flat')
    entry_103.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)
    entry_103.insert(0, '0')

    button_101 = tk.Button(frame_1, text='Delete All', command=delete_all)
    button_101.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)

######################################################################################################
# Configure and add widgets to the right frame
if True:
    label_200 = tk.Label(frame_2, text='User Main Data')
    label_200.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(10, 5))

    data_1 = tk.DoubleVar(value=0)
    label_201 = tk.Label(frame_2, text='User Data 1:', anchor='e')
    label_201.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
    entry_201 = tk.Entry(frame_2, justify='center', textvariable=data_1)
    entry_201.grid(row=1, column=1, sticky='nsew', padx=5)

    data_2 = tk.DoubleVar(value=0)
    label_202 = tk.Label(frame_2, text='User Data 2:', anchor='e')
    label_202.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
    entry_202 = tk.Entry(frame_2, justify='center', textvariable=data_2)
    entry_202.grid(row=2, column=1, sticky='nsew', padx=5)

    button_200 = tk.Button(frame_2, text='Calculate Sum', command=calculate_2)
    button_200.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)

    result_1 = tk.DoubleVar(value=0)
    label_203 = tk.Label(frame_2, textvariable=result_1, anchor='center', bg='white')
    label_203.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=2, pady=2)

    button_201 = tk.Button(frame_2, text='Delete All', command=delete_all_2)
    button_201.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=1, pady=1)

######################################################################################################
# Main Program
if __name__ == '__main__':
    root.mainloop()
