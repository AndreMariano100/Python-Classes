"""
Construct a checkbutton widget with the parent MASTER.

Valid resource names:
    activebackground, activeforeground, anchor,
    background, bd, bg, bitmap, borderwidth, command, cursor,
    disabledforeground, fg, font, foreground, height,
    highlightbackground, highlightcolor, highlightthickness, image,
    indicatoron, justify, offvalue, onvalue, padx, pady, relief,
    selectcolor, selectimage, state, takefocus, text, textvariable,
    underline, variable, width, wraplength.

WIDGET METHODS
    w.deselect()
    w.flash()
    w.invoke()
    w.select()
    w.toggle()
"""
import tkinter as tk


def show_values():
    print('Values:', var_1.get(), var_2.get(), var_3.get())

def activate():
    print(check_box_1.cget('state'))
    if check_box_1.cget('state') == 'normal':
        check_box_1.configure(state='disabled')
        check_box_2.configure(state='disabled')
        check_box_3.configure(state='disabled')
    else:
        check_box_1.configure(state='normal')
        check_box_2.configure(state='normal')
        check_box_3.configure(state='normal')

def do_other_stuff():
    # check_box_1.deselect()
    # check_box_2.flash()
    # check_box_3.invoke()
    check_box_1.toggle()
    check_box_2.toggle()
    check_box_3.toggle()


def change_type():
    if check_box_1.cget('indicatoron'):
        check_box_1.config(indicatoron=0)
        check_box_2.config(indicatoron=0)
        check_box_3.config(indicatoron=0)
    else:
        check_box_1.config(indicatoron=1)
        check_box_2.config(indicatoron=1)
        check_box_3.config(indicatoron=1)


def two_variables():
    print(f'Value: {var_4.get()}')
    text = var_5.get()
    if 'original' in text.lower():
        var_5.set('New Text')
    else:
        var_5.set('Original Button Text')


master = tk.Tk()
master.columnconfigure(0, weight=1)

var_1 = tk.StringVar(value='0')
check_box_1 = tk.Checkbutton(master, text='Check 1', variable=var_1, command=show_values)
check_box_1.grid(row=0, column=0)

# check_box_1.config(onvalue='RGB', offvalue='BW')

var_2 = tk.StringVar(value='0')
check_box_2 = tk.Checkbutton(master, text='Check 2', variable=var_2, command=show_values, selectcolor='red')
check_box_2.grid(row=1, column=0)
# selectcolor='red'

var_3 = tk.StringVar(value='0')
check_box_3 = tk.Checkbutton(master, text='Check 3', variable=var_3, command=show_values)
check_box_3.grid(row=2, column=0)

activate_button = tk.Button(master, text='De Activate', command=activate)
activate_button.grid(row=3, column=0)

other_button = tk.Button(master, text='Something else', command=do_other_stuff)
other_button.grid(row=4, column=0)

another_button = tk.Button(master, text='Change them', command=change_type)
another_button.grid(row=5, column=0)

var_4 = tk.StringVar(value='0')
var_5 = tk.StringVar(value='Original Button Text')
check_box_4 = tk.Checkbutton(master, textvariable=var_5, variable=var_4, command=two_variables)
check_box_4.grid(row=6, column=0)


if __name__ == '__main__':
    master.mainloop()
