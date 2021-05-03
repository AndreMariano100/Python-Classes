'''
Construct a spinbox widget with the parent MASTER.

    STANDARD OPTIONS

        activebackground, background, borderwidth,
        cursor, exportselection, font, foreground,
        highlightbackground, highlightcolor,
        highlightthickness, insertbackground,
        insertborderwidth, insertofftime,
        insertontime, insertwidth, justify, relief,
        repeatdelay, repeatinterval,
        selectbackground, selectborderwidth
        selectforeground, takefocus, textvariable
        xscrollcommand.

    WIDGET-SPECIFIC OPTIONS

        buttonbackground, buttoncursor,
        buttondownrelief, buttonuprelief,
        command, disabledbackground,
        disabledforeground, format, from,
        invalidcommand, increment,
        readonlybackground, state, to,
        validate, validatecommand values,
        width, wrap,

'''
import tkinter as tk


def adjust_color():
    red = int(red_spinbox.get())
    green = int(green_spinbox.get())
    blue = int(blue_spinbox.get())
    print(red, green, blue)
    color = "#%02x%02x%02x" % (red, green, blue)
    color_canvas.configure(bg=color)
    hex_label_2.configure(text=color)


root = tk.Tk()

# Create a left frame for the spinbox
left_frame = tk.LabelFrame(root, text='RGB Colors')
left_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
left_frame.columnconfigure(0, weight=0)
left_frame.columnconfigure(1, weight=0)

red_label = tk.Label(left_frame, text='RED:', justify='right')
red_label.grid(row=0, column=0, sticky='nsew')
red_spinbox = tk.Spinbox(left_frame, from_=0, to_=255, increment=1, justify='center',
                         width=5, command=adjust_color)
red_spinbox.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

green_label = tk.Label(left_frame, text='GREEN:')
green_label.grid(row=1, column=0, sticky='nsew')
green_spinbox = tk.Spinbox(left_frame, from_=0, to_=255, increment=1, justify='center',
                           command=adjust_color, width=5)
green_spinbox.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

blue_label = tk.Label(left_frame, text='BLUE:')
blue_label.grid(row=2, column=0, sticky='nsew')
blue_spinbox = tk.Spinbox(left_frame, from_=0, to_=255, increment=1, justify='center',
                          width=5, command=adjust_color)
blue_spinbox.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)

hex_label_1 = tk.Label(left_frame, text='Hexadecimal Equivalent:')
hex_label_2 = tk.Label(left_frame, text='')
hex_label_1.grid(row=3, column=0)
hex_label_2.grid(row=3, column=1)

# Create a frame on the right to show a canvas
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=5, pady=5)
color_canvas = tk.Canvas(right_frame, bg='black')
color_canvas.grid()

if __name__ == "__main__":
    root.mainloop()
