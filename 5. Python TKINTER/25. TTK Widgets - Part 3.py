# -*- coding: utf-8 -*-

# Copyright (c) Juliette Monsel 2018
# For license see LICENSE

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkwidgets.font import askfont
from ttkwidgets.color import askcolor
from ttkwidgets.autocomplete import AutocompleteCombobox
from ttkwidgets.autocomplete import AutocompleteEntry
from ttkwidgets.autocomplete import AutocompleteEntryListbox
from ttkwidgets import AutoHideScrollbar
from ttkwidgets import Calendar
from ttkwidgets import CheckboxTreeview
from ttkwidgets import DebugWindow
from ttkwidgets.font import FontSelectFrame
from ttkwidgets import ItemsCanvas
from ttkwidgets import LinkLabel
from ttkwidgets import ScaleEntry
from ttkwidgets.frames import ScrolledFrame
from ttkwidgets import ScrolledListbox
from ttkwidgets import Table
from ttkwidgets import TickScale
from ttkwidgets import TimeLine
from ttkwidgets.frames import ToggledFrame
# from ttkwidgets.frames import Tooltip


#############################################################################################
# Functions

def pick(alpha=False):
    global im  # to avoid garbage collection of image
    res = askcolor('sky blue', parent=window, title='Pick a color', alpha=alpha)
    canvas_1.delete('image')
    if res[1] is not None:
        im = ImageTk.PhotoImage(Image.new('RGBA', (120, 100), res[1]), master=window)
        canvas_1.create_image(120, 60, image=im, tags='image', anchor='center')
    print(res)


def font():
    res = askfont()
    if res[0] is not None:
        font_label.configure(font=res[0])
    print(res)


def validate():
    sel = calendar.selection
    if sel is not None:
        calendar_label.configure(text='Selected date: %s' % sel.strftime('%x'))


def update_preview(font_tuple):
    print(font_tuple)
    font = font_selection.font[0]
    if font is not None:
        font_label_2.configure(font=font)


# toggle table properties
def toggle_sort():
    table.config(sortable=sortable.get())


def toggle_drag_col():
    table.config(drag_cols=drag_col.get())


def toggle_drag_row():
    table.config(drag_rows=drag_row.get())


#############################################################################################
# Main Window
window = tk.Tk()

#############################################################################################
# Ask Color
if True:
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    ask_color_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    ask_color_frame.grid(row=0, column=0, sticky='nsew')

    canvas_1 = tk.Canvas(ask_color_frame, width=120, height=120)
    canvas_1.create_text(120, 60, text='Background', anchor='center')
    canvas_1.grid(row=0, column=0, sticky='nsew')
    button_1 = ttk.Button(ask_color_frame, text="Pick a color (No alpha channel)", command=pick)
    button_1.grid(row=1, column=0, sticky='nsew')
    button_2 = ttk.Button(ask_color_frame, text="Pick a color (With alpha channel)", command=lambda: pick(True))
    button_2.grid(row=2, column=0, sticky='nsew')

#############################################################################################
# Ask Font
if True:
    window.rowconfigure(1, weight=1)
    ask_font_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    ask_font_frame.grid(row=1, column=0, sticky='nsew')
    font_label = ttk.Label(ask_font_frame, text='Sample text rendered in the chosen font.')
    font_label.pack(padx=10, pady=10)
    ttk.Button(ask_font_frame, text="Pick a font", command=font).pack()

#############################################################################################
# Autocomplete combobox
if True:
    window.rowconfigure(2, weight=1)
    combobox_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    combobox_frame.grid(row=2, column=0, sticky='nsew')
    tk.Label(combobox_frame, text="Combobox with autocompletion for the Tk instance's methods:").pack(side='top')
    entry = AutocompleteCombobox(combobox_frame, width=20, completevalues=dir(window))
    entry.pack(side='bottom')

#############################################################################################
# Autocomplete entry
if True:
    window.rowconfigure(3, weight=1)
    entry_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    entry_frame.grid(row=3, column=0, sticky='nsew')
    tk.Label(entry_frame, text="Entry with autocompletion for the Tk instance's methods:").pack(side='top')
    entry = AutocompleteEntry(entry_frame, width=20, completevalues=dir(window))
    entry.pack(side='bottom')

#############################################################################################
# Ask Autocomplete entry listbox
if True:
    window.rowconfigure(4, weight=1)
    entry_list_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    entry_list_frame.grid(row=4, column=0, sticky='nsew')
    tk.Label(entry_list_frame, text="Entry + Listbox with autocompletion for the Tk instance's methods:").pack()
    entry = AutocompleteEntryListbox(entry_list_frame, width=20, completevalues=dir(window))
    entry.pack()

#############################################################################################
# Auto hide scrollbar
if True:
    window.columnconfigure(1, weight=1)
    scrollbar_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    scrollbar_frame.grid(row=0, column=1, sticky='nsew')
    listbox = tk.Listbox(scrollbar_frame, height=5)
    scrollbar = AutoHideScrollbar(scrollbar_frame, command=listbox.yview)
    listbox.configure(yscrollcommand=scrollbar.set)

    for i in range(10):
        listbox.insert('end', 'item %i' % i)

    tk.Label(scrollbar_frame, text="Increase the window's height\nto make the scrollbar vanish.").pack(side='top', padx=4, pady=4)
    scrollbar.pack(side='right', fill='y')
    listbox.pack(side='left', fill='both', expand=True)

#############################################################################################
# Calendar
if True:
    calendar_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    calendar_frame.grid(row=1, rowspan=3, column=1, sticky='nsew')
    calendar = Calendar(calendar_frame, year=2020, month=3, selectforeground='white',
                        selectbackground='red')
    calendar.pack()

    tk.Button(calendar_frame, text='Select', command=validate).pack()
    calendar_label = tk.Label(calendar_frame, text='Selected date:')
    calendar_label.pack()

#############################################################################################
# CheckboxTreeview
if True:
    tree_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    tree_frame.grid(row=4, column=1, sticky='nsew')
    tree = CheckboxTreeview(tree_frame)
    tree.pack()
    tree.insert("", "end", "1", text="1")
    tree.insert("1", "end", "11", text="11")
    tree.insert("1", "end", "12",  text="12")
    tree.insert("1", "end", "13", text="13")
    tree.insert("11", "end", "111", text="111")
    tree.insert("11", "end", "112", text="112")
    tree.insert("", "end", "2", text="2")
    tree.insert("", "end", "3", text="3")

#############################################################################################
# DebugWindow
if True:
    window.columnconfigure(2, weight=1)
    debug_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    debug_frame.grid(row=0, column=2, sticky='nsew')
    ttk.Button(debug_frame, text="Print ok", command=lambda: print('ok')).pack()
    DebugWindow(debug_frame)


#############################################################################################
# FontSelectFrame
if True:
    font_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    font_frame.grid(row=1, column=2, sticky='nsew')
    font_label_2 = ttk.Label(font_frame, text='Sample text rendered in the chosen font.')
    font_label_2.pack(padx=10, pady=10)
    font_selection = FontSelectFrame(font_frame, callback=update_preview)
    font_selection.pack()


#############################################################################################
# ItemsCanvas
if True:
    canvas_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    canvas_frame.grid(row=2, column=2, sticky='nsew')
    canvas = ItemsCanvas(canvas_frame, canvasheight=20, canvaswidth=50)
    canvas.pack()
    canvas.add_item("Example", font=("default", 13, "italic"), backgroundcolor="green", textcolor="darkblue",
                    highlightcolor="blue")

#############################################################################################
# LinkLabel
if True:
    link_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    link_frame.grid(row=3, column=2, sticky='nsew')
    LinkLabel(link_frame, text="ttkwidgets repository",
              link="https://github.com/RedFantom/ttkwidgets",
              normal_color='royal blue',
              hover_color='blue',
              clicked_color='purple').pack()

#############################################################################################
# ScaleEntry
if True:
    scale_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    scale_frame.grid(row=4, column=2, sticky='nsew')
    scaleentry = ScaleEntry(scale_frame, scalewidth=200, entrywidth=3, from_=0, to=20)
    scaleentry.config_entry(justify='center')
    scaleentry.pack()

#############################################################################################
# ScrolledFrame
if True:
    window.columnconfigure(3, weight=1)
    scrolled_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    scrolled_frame.grid(row=0, column=3, sticky='nsew')
    frame = ScrolledFrame(scrolled_frame, compound=tk.RIGHT, canvasheight=200)
    frame.pack(fill='both', expand=True)

    for i in range(10):
        ttk.Label(frame.interior, text='Label %i' % i).pack()

#############################################################################################
# ScrolledListbox
if True:
    listbox_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    listbox_frame.grid(row=1, column=3, sticky='nsew')
    listbox = ScrolledListbox(listbox_frame, height=5)
    for i in range(10):
        listbox.listbox.insert('end', 'item {}'.format(i))

    listbox.pack(fill='both', expand=True)

#############################################################################################
# Table
if True:
    table_frame = ttk.Frame(window, relief='ridge', borderwidth=2)
    table_frame.grid(row=2, rowspan=3, column=3, sticky='nsew')
    table_frame.columnconfigure(0, weight=1)
    table_frame.rowconfigure(0, weight=1)

    # style = ttk.Style(table_frame)
    # style.theme_use('classic')
    sortable = tk.BooleanVar(table_frame, False)
    drag_row = tk.BooleanVar(table_frame, False)
    drag_col = tk.BooleanVar(table_frame, False)

    columns = ["A", "B", "C", "D", "E", "F", "G"]
    table = Table(table_frame, columns=columns, sortable=sortable.get(), drag_cols=drag_col.get(),
                  drag_rows=drag_row.get(), height=6)
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, stretch=False)

    # sort column A content as int instead of strings
    table.column('A', type=int)

    for i in range(12):
        table.insert('', 'end', iid=i,
                     values=(i, i) + tuple(i + 10 * j for j in range(2, 7)))

    # add scrollbars
    sx = tk.Scrollbar(table_frame, orient='horizontal', command=table.xview)
    sy = tk.Scrollbar(table_frame, orient='vertical', command=table.yview)
    table.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

    table.grid(sticky='ewns')
    sx.grid(row=1, column=0, sticky='ew')
    sy.grid(row=0, column=1, sticky='ns')
    table_frame.update_idletasks()

    frame = tk.Frame(table_frame)
    tk.Checkbutton(frame, text='sortable', variable=sortable, command=toggle_sort).pack(side='left')
    tk.Checkbutton(frame, text='drag columns', variable=drag_col, command=toggle_drag_col).pack(side='left')
    tk.Checkbutton(frame, text='drag rows', variable=drag_row, command=toggle_drag_row).pack(side='left')
    frame.grid()

    # #############################################################################################
    # # TickScale
    #
    # style = ttk.Style(window)
    # style.theme_use('clam')
    # style.configure('my.Vertical.TScale', sliderlength=50, background='white',
    #                 foreground='red')
    # style.configure('my.Horizontal.TScale', sliderlength=10,
    #                 font='TkDefaultFont 20 italic')
    # s1 = TickScale(root, orient='vertical', style='my.Vertical.TScale',
    #                tickinterval=0.2, from_=-1, to=1, showvalue=True, digits=2,
    #                length=400, labelpos='e')
    # s2 = TickScale(root, orient='horizontal', style='my.Horizontal.TScale',
    #                from_=0, to=10, tickinterval=2, resolution=1,
    #                showvalue=True, length=400)
    # s3 = TickScale(root, orient='horizontal', from_=0.25, to=1, tickinterval=0.1,
    #                resolution=0.1)
    #
    # s1.pack(fill='y')
    # s2.pack(fill='x')
    # s3.pack(fill='x')
    #
    # #############################################################################################
    # # Timeline
    #
    # timeline = TimeLine(
    #     window,
    #     categories={str(key): {"text": "Category {}".format(key)} for key in range(0, 5)},
    #     height=100, extend=True
    # )
    # menu = tk.Menu(window, tearoff=False)
    # menu.add_command(label="Some Action", command=lambda: print("Command Executed"))
    # timeline.tag_configure("1", right_callback=lambda *args: print(args), menu=menu, foreground="green",
    #                        active_background="yellow", hover_border=2, move_callback=lambda *args: print(args))
    # timeline.create_marker("1", 1.0, 2.0, background="white", text="Change Color", tags=("1",), iid="1")
    # timeline.create_marker("2", 2.0, 3.0, background="green", text="Change Category", foreground="white", iid="2",
    #                        change_category=True)
    # timeline.create_marker("3", 1.0, 2.0, text="Show Menu", tags=("1",))
    # timeline.create_marker("4", 4.0, 5.0, text="Do nothing", move=False)
    # timeline.draw_timeline()
    # timeline.grid()
    # window.after(2500, lambda: timeline.configure(marker_background="cyan"))
    # window.after(5000, lambda: timeline.update_marker("1", background="red"))
    # window.after(5000, lambda: print(timeline.time))
    #
    # #############################################################################################
    # #ToggledFrame
    # frame = ToggledFrame(window, text="Value", width=10)
    # frame.pack()
    # button = ttk.Button(frame.interior, text="Button", command=window.destroy)
    # button.grid()
    # frame.toggle()
    #
    # #############################################################################################
    # # Tooltip
    # button = tk.Button(window, text="Button", command=window.destroy)
    # button.pack()
    # balloon = Tooltip(button)

#############################################################################################

if __name__ == '__main__':
    window.mainloop()


