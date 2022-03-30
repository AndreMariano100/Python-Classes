"""
Construct a text widget with the parent MASTER.

STANDARD OPTIONS

    background, borderwidth, cursor,
    exportselection, font, foreground,
    highlightbackground, highlightcolor,
    highlightthickness, insertbackground,
    insertborderwidth, insertofftime,
    insertontime, insertwidth, padx, pady,
    relief, selectbackground,
    selectborderwidth, selectforeground,
    setgrid, takefocus,
    xscrollcommand, yscrollcommand,

WIDGET-SPECIFIC OPTIONS

    autoseparators, height, maxundo,
    spacing1, spacing2, spacing3,
    state, tabs, undo, width, wrap,

WIDGET METHODS:
    w.get(index1, index2)
    w.insert(index, chars)
"""

import tkinter as tk


def print_text():
    text = my_text.get('1.0', tk.END)
    print(text)


def clear_text():
    my_text.delete('1.2', tk.END)


my_font = ('Arial', 16, 'italic')
master = tk.Tk()
master.columnconfigure(0, weight=1)

my_text = tk.Text(master, bg='gray10', fg='white', font=my_font, width=40, height=6)
my_text.grid(row=0, column=0)

save_button = tk.Button(text='Print Text', command=print_text)
clear_button = tk.Button(text='Clear Text', command=clear_text)
save_button.grid(row=1, column=0, sticky='nsew')
clear_button.grid(row=2, column=0, sticky='nsew')


if __name__ == '__main__':
    master.mainloop()
