"""Construct a scrollbar widget with the parent MASTER.

        Valid resource names: activebackground, activerelief,
        background, bd, bg, borderwidth, command, cursor,
        elementborderwidth, highlightbackground,
        highlightcolor, highlightthickness, jump, orient,
        relief, repeatdelay, repeatinterval, takefocus,
        troughcolor, width.

WIDGET METHODS:

w.activate()
w.get()
w.set()


See scroll bar on Listbox.py
"""
import tkinter as tk


def canvas_configure(event):
    width = max(event.width, 600)
    height = max(event.height, 600)
    scroll_canvas.itemconfigure(frame_id, width=width, height=height)


root = tk.Tk()
root.config(bg='black')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Frame for the scroll canvas
base_frame = tk.Frame(root, bg='gray50')
base_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
base_frame.columnconfigure(0, weight=1)
base_frame.columnconfigure(1, weight=0)
base_frame.rowconfigure(0, weight=1)
base_frame.rowconfigure(1, weight=0)

# Scroll canvas
scroll_canvas = tk.Canvas(base_frame, bg='gray70', borderwidth=0, highlightthickness=0)
scroll_canvas.grid(row=0, column=0, sticky='nsew')
scroll_canvas.bind("<Configure>", canvas_configure)

# Scroll bars
y_scroll = tk.Scrollbar(base_frame, orient='vertical', command=scroll_canvas.yview)
y_scroll.grid(row=0, column=1, sticky='nsew')
x_scroll = tk.Scrollbar(base_frame, orient='horizontal', command=scroll_canvas.xview)
x_scroll.grid(row=1, column=0, sticky='nsew')

# Local frame that will receive the widgets
w_frame = tk.Frame(scroll_canvas, bg='white')
w_frame.columnconfigure(0, weight=1)
w_frame.grid(sticky='nsew')
w_frame.bind("<Configure>",
             lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))

# Putting the frame on the canvas
frame_id = scroll_canvas.create_window((0, 0), window=w_frame, anchor='nw')
scroll_canvas.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

# Title
if True:
    w_frame.rowconfigure(0, weight=0)
    title = tk.Label(w_frame, text='Title', anchor='w', pady=5, padx=5)
    title.grid(row=0, column=0, sticky='nsew')

root.mainloop()
