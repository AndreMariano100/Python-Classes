"""
Construct a radiobutton widget with the parent MASTER.

    Valid resource names: activebackground, activeforeground, anchor,
    background, bd, bg, bitmap, borderwidth, command, cursor,
    disabledforeground, fg, font, foreground, height,
    highlightbackground, highlightcolor, highlightthickness, image,
    indicatoron, justify, padx, pady, relief, selectcolor, selectimage,
    state, takefocus, text, textvariable, underline, value, variable,
    width, wraplength.

WIDGET METHODS:
    w.deselect()
    w.flash()
    w.invoke()
    w.select()

"""
import tkinter as tk


# App Functions
def show_option_1():
    option_1 = v_1.get()
    option_2 = v_2.get()
    option_3 = v_3.get()
    print('Button Selected:', option_1, option_2, option_3)

def function_1():
    print('Function 1')

def function_2():
    print('Function 2')

def function_3():
    print('Function 3')

def function_4():
    print('Function 4')

def show_option_2():
    option = v_5.get()
    print('Button Selected:', option)



###################
# App GUIs
root = tk.Tk()
root.rowconfigure(0, weight=1)

# Frame for the first buttons
frame_1 = tk.Frame(root, relief='ridge', bd=2)
frame_1.grid(row=0, column=0)

v_1 = tk.IntVar()
radio_11 = tk.Radiobutton(frame_1, text='Option 1', variable=v_1, value=0, command=show_option_1)
radio_11.grid(row=0, column=0)
radio_12 = tk.Radiobutton(frame_1, text='Option 2', variable=v_1, value=1, command=show_option_1)
radio_12.grid(row=1, column=0)
radio_13 = tk.Radiobutton(frame_1, text='Option 3', variable=v_1, value=2, command=show_option_1)
radio_13.grid(row=3, column=0)
v_1.set(0)

# Frame for the second set of radiobuttons
frame_2 = tk.Frame(root, relief='ridge', bd=2)
frame_2.grid(row=0, column=1)

v_2 = tk.IntVar()
radiobuttons_labels = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6']

for i in range(len(radiobuttons_labels)):
    radio = tk.Radiobutton(frame_2, text=radiobuttons_labels[i], variable=v_2, value=i+1, command=show_option_1)
    radio.grid(row=i, column=0)
v_2.set(2)

# Frame for the third set of radiobuttons
frame_3 = tk.Frame(root, relief='ridge', bd=2)
frame_3.grid(row=0, column=2)

v_3 = tk.StringVar()
radiobuttons_labels = [('Option 1', 'A'),
                       ('Option 2', 'B'),
                       ('Option 3', 'C'),
                       ('Option 4', 'D'),
                       ('Option 5', 'E'),
                       ('Option 6', 'F'),
                       ('Option 7', 'G'),
                       ]
for i in range(len(radiobuttons_labels)):
    radio = tk.Radiobutton(frame_3, text=radiobuttons_labels[i][0], variable=v_3,
                           value=radiobuttons_labels[i][1], command=show_option_1)
    radio.grid(row=i, column=0)
v_3.set('F')

# Frame for the fourth set of radiobuttons
frame_4 = tk.Frame(root, relief='ridge', bd=2)
frame_4.grid(row=0, column=3)
v_4 = tk.StringVar()
radiobuttons_data = (('Option 1', 'A', function_1),
                     ('Option 2', 'B', function_2),
                     ('Option 3', 'C', function_3),
                     ('Option 4', 'D', function_4),
                     )
for i in range(len(radiobuttons_data)):
    radio = tk.Radiobutton(frame_4, variable=v_4,
                           text=radiobuttons_data[i][0],
                           value=radiobuttons_data[i][1],
                           command=radiobuttons_data[i][2])
    radio.grid(row=i, column=0)
v_4.set('A')

# Frame for the fifth set of radiobuttons - organizing by columns
frame_5 = tk.Frame(root, relief='ridge', bd=2)
frame_5.grid(row=0, column=4)

v_5 = tk.StringVar()
radiobuttons_labels = [('Option 1', 'A'),
                       ('Option 2', 'B'),
                       ('Option 3', 'C'),
                       ('Option 4', 'D'),
                       ('Option 5', 'E'),
                       ('Option 6', 'F'),
                       ('Option 7', 'G'),
                       ('Option 8', 'H'),
                       ('Option 9', 'I'),
                       ('Option 10', 'J'),
                       ('Option 11', 'K'),
                       ('Option 12', 'L'),
                       ('Option 13', 'M'),
                       ('Option 14', 'N'),
                       ('Option 15', 'O'),
                       ]
num_col = 3
for i, (text, value) in enumerate(radiobuttons_labels):
    radio = tk.Radiobutton(frame_5, text=text, variable=v_5,
                           value=value, command=show_option_2,
                           indicatoron=0)
    radio.grid(row=i//num_col, column=i % num_col)

v_5.set('Z')

# Frame for the sixth set of radiobuttons - organizing by lines
v_6 = tk.StringVar()
frame_6 = tk.Frame(root, relief='ridge', bd=2)
frame_6.grid(row=0, column=5)
num_lines = 5
for i in range(len(radiobuttons_labels)):
    radio = tk.Radiobutton(frame_6, text=radiobuttons_labels[i][0], variable=v_6,
                           value=radiobuttons_labels[i][1], command=show_option_2)
    radio.grid(row=i % num_lines, column=i//num_lines)

v_6.set('A')

# Frame for the seventh set of radiobuttons - ttkbootstrap style
if True:
    import tkinter.ttk as ttk
    from ttkbootstrap import Style

    def show_option_7():
        print(f'Selected: {v_7.get()}')

    style = Style(theme='flatly')

    frame_7 = ttk.Frame(root, relief='ridge')
    frame_7.grid(row=0, column=6)
    labels = ('Radio Button 1', 'Radio Button 2', 'Radio Button 3')
    v_7 = tk.IntVar()
    for i, text in enumerate(labels):
        ttk.Radiobutton(frame_7, text=text, variable=v_7, value=i, command=show_option_7)\
            .grid(row=i, column=0, sticky='nsew', pady=5, padx=10)
    v_7.set(0)

    for i, text in enumerate(labels):
        ttk.Radiobutton(frame_7, text=text, variable=v_7, value=i+3, command=show_option_7, style='primary.Toolbutton')\
            .grid(row=i+3, column=0, sticky='nsew', pady=5, padx=10)

    for i, text in enumerate(labels):
        ttk.Radiobutton(frame_7, text=text, variable=v_7, value=i+6, command=show_option_7,
                        style='primary.Outline.Toolbutton').grid(row=i+6, column=0, sticky='nsew', pady=5, padx=10)

#####################
# Run the App
if __name__ == "__main__":
    root.mainloop()
