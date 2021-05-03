"""
Construct a scale widget with the parent MASTER.

Valid resource names:
    activebackground, background, bigincrement, bd,
    bg, borderwidth, command, cursor, digits, fg, font, foreground, from,
    highlightbackground, highlightcolor, highlightthickness, label,
    length, orient, relief, repeatdelay, repeatinterval, resolution,
    showvalue, sliderlength, sliderrelief, state, takefocus,
    tickinterval, to, troughcolor, variable, width.

WIDGET METHODS:
    w.get()
    w.set()
"""
import tkinter as tk


def show_data(event):
    print('Event:', event)
    scale_1 = v_scale.get()
    scale_2 = h_scale.get()
    print('Values:', scale_1, scale_2)


def reset_data():
    h_scale.set(0)
    v_scale.set(0)


root = tk.Tk()

v_scale = tk.Scale(root, from_=10, to=-10, command=show_data, label='Vertical Scale', relief='groove')
v_scale.grid(row=0, column=0, sticky='nsew')

h_scale = tk.Scale(root, orient='horizontal', from_=-10, to=10, command=show_data,
                   label='Horizontal Scale', relief='sunken')
h_scale.grid(row=1, column=0, sticky='nsew')

reset = tk.Button(root, text='Reset', command=reset_data)
reset.grid(row=2, column=0, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()
