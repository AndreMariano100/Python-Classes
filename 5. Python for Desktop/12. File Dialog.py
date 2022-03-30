"""
File selection dialog classes.

Classes:

- FileDialog
- LoadFileDialog
- SaveFileDialog

This module also presents tk common file dialogues, it provides interfaces
to the native file dialogues available in Tk 4.2 and newer, and the
directory dialogue available in Tk 8.3 and newer.
These interfaces were written by Fredrik Lundh, May 1997.
"""

import tkinter as tk
from tkinter import filedialog

def open_file(option):
    filename = filedialog.askopenfilename(title="Select file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

    try:
        if option == 'r':
            print('Read Only')
            file = open(filename, 'r')
            data = []
            for line in file:
                if line:
                    data.append(line)
            print('Arquivo lido com sucesso')
            print('Data:', data)

        if option == 'a':
            print('Append')
            file = open(filename, 'a')
            file.writelines('A new line to the file\n')
            file.close()
            file = open(filename, 'r')
            data = []
            for line in file:
                if line:
                    data.append(line)
            print('Data:', data)

        elif option == 'w':
            print('Rewrite')
            file = open(filename, 'w')
            file.write('A new file has been started\n')
            file.close()
            file = open(filename, 'r')
            data = []
            for line in file:
                if line:
                    data.append(line)
            print('Data:', data)

    except FileNotFoundError:
        print('File not found')

    finally:
        file.close()


def save_file():

    exported_data = ['This is a text file',
                     'It contains several lines',
                     'They are separated as in a list',
                     'And each item will be written to a separate line']

    filename = filedialog.asksaveasfilename(title="Select file",
                                            filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    try:
        if '.txt' not in filename:
            filename = filename + '.txt'
        file = open(filename, 'w')
        for i, item in enumerate(exported_data):
            file.write(item+'\n')
        file.close()
        print('Arquivo salvo com sucesso')
    except FileNotFoundError:
        print('File not found')


################################################################################################
root = tk.Tk()

button_read = tk.Button(root, text='Read Only', command=lambda: open_file('r'))
button_read.grid(row=0, column=0, sticky='nsew')

button_append = tk.Button(root, text='Append', command=lambda: open_file('a'))
button_append.grid(row=1, column=0, sticky='nsew')

button_overwrite = tk.Button(root, text='Overwrite', command=lambda: open_file('w'))
button_overwrite.grid(row=2, column=0, sticky='nsew')

button_save = tk.Button(root, text='Save', command=save_file)
button_save.grid(row=3, column=0, sticky='nsew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

#####################
# Run the App
if __name__ == "__main__":
    root.mainloop()

