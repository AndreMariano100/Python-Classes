import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


def change_theme():
    selection = themes.get()
    my_style.set_theme(selection)
    '''
    imported_themes = ['aquativo', 'arc', 'black', 'blue', 'breeze', 'clearlooks',
                       'elegance', 'equilux', 'itft1', 'keramik', 'kroc', 'plastik',
                       'radiance', 'scidblue', 'scidgreen', 'scidgrey', 'scidmint',
                       'scidpink', 'scidpurple', 'scidsand', 'smog', 'ubuntu', 'winxpblue',
                       'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative']
    '''


####################################################################################################
# Main Window
root = tk.Tk()
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

####################################################################################################
# Frame 1
frame_1 = ttk.Frame(root, padding=10)
frame_1.grid(row=0, column=0, sticky='nsew')
frame_1.columnconfigure(0, weight=1)

################
# Buttons
for i in range(3):
    button = ttk.Button(frame_1, text=f'Button {i}')
    button.grid(row=i, column=0, sticky='nsew')
###############
# labels
for i in range(3):
    label = ttk.Label(frame_1, text=f'Label {i}', anchor='center')
    label.grid(row=i+4, column=0, sticky='nsew')
###############
# Entry
for i in range(3):
    entry = ttk.Entry(frame_1, justify='center')
    entry.grid(row=i+8, column=0, sticky='nsew')
###############
# Check Buttons
for i in range(3):
    var = tk.IntVar()
    checkbutton = ttk.Checkbutton(frame_1, variable=var, text=f'Check Button {i}')
    checkbutton.grid(row=i+12, column=0, sticky='nsew')

####################################################################################################
# Frame 2
frame_2 = ttk.Frame(root, padding=10)
frame_2.grid(row=0, column=1, sticky='nsew')
frame_2.columnconfigure(0, weight=1)

###############
# Menu Buttons
menu_button = ttk.Menubutton(frame_2, text=f'Menu Button')
drop = tk.Menu(menu_button, tearoff=False)
for i in range(4):
    drop.add_command(label=f'option{i}')
    menu_button['menu'] = drop
menu_button.grid(row=0, column=0, sticky='nsew', pady=10)

##############
# Notebook
note_book = ttk.Notebook(frame_2)
note_book.grid(row=1, column=0, sticky='nsew', pady=10)
for i in range(4):
    frame = ttk.Frame(note_book)
    note_book.add(frame, text=f'Page{i}')
    label = ttk.Label(frame, text='Sample text\nto fill the\n notebook.\n'
                                  f'This is page {i}', anchor='center')
    label.grid(row=0, column=0, sticky='nsew')

###############
# Radiobutton
var = tk.IntVar()
for i in range(4):
    radio_button = ttk.Radiobutton(frame_2, text=f'Radio Button {i}', value=i, variable=var)
    radio_button.grid(row=2+i, column=0, sticky='nsew')

################
# Scale
h_scale = ttk.Scale(frame_2, from_=-10, to=10, orient='horizontal')
h_scale.grid(row=7, column=0, sticky='nsew', padx=10)

###############
# Setting the style / theme
my_style = ThemedStyle()
imported_themes = list(my_style.theme_names())
print(imported_themes)

themes = ttk.Combobox(root, values=imported_themes)
themes.bind('<<ComboboxSelected>>', lambda e: change_theme())
themes.grid(row=1, column=0, columnspan=2, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()
