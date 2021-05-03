"""
Construct a listbox widget with the parent MASTER.

Valid resource names:
    background, bd, bg, borderwidth, cursor,
    exportselection, fg, font, foreground, height, highlightbackground,
    highlightcolor, highlightthickness, relief, selectbackground,
    selectborderwidth, selectforeground, selectmode, setgrid, takefocus,
    width, xscrollcommand, yscrollcommand, listvariable.

WIDGET METHODS
    w.curselection()
    w.delete(first, last)
    w.get(first, last)
    w.insert(index, *elements)
    w.size()
"""

import tkinter as tk

def get_selection():
    line = list_box.curselection()
    item = list_box.get(line)
    print('Selection:', line)
    print('Item:', item)

root = tk.Tk()
root.columnconfigure(0, weight=1)

# Add a scroll
my_y_scroll = tk.Scrollbar(root, orient='vertical')
my_y_scroll.grid(row=0, column=1, sticky='ns')
my_x_scroll = tk.Scrollbar(root, orient='horizontal')
my_x_scroll.grid(row=1, column=0, sticky='ew')

list_var = tk.StringVar()
my_list = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5', 'Value 6 may be longer then the others']
list_var.set(my_list)
list_box = tk.Listbox(root, listvariable=list_var, height=4,
                      xscrollcommand=my_x_scroll.set, yscrollcommand=my_y_scroll.set)
list_box.grid(row=0, column=0, sticky='nsew')

my_x_scroll['command'] = list_box.xview
my_y_scroll['command'] = list_box.yview

button = tk.Button(root, text='Get Selection', command=get_selection)
button.grid(row=2, column=0, columnspan=2, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()
