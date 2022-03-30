import tkinter as tk
from PIL import Image, ImageTk


def show_hide_frame():
    if c.itemcget(second_window_id, 'state') == 'normal':
        c.itemconfig(second_window_id, state='hidden')
    else:
        c.itemconfig(second_window_id, state='normal')


root = tk.Tk()

# Create Canvas ---------------------------------------------------------------------------------
if True:
    x_dimension = 850
    y_dimension = 600
    c = tk.Canvas(root, width=x_dimension, height=y_dimension, bg='white', highlightthickness=0)
    c.grid(row=0, column=0, sticky='nsew')

# Create Image -----------------------------------------------------------------------------------
if True:

    # Reads the image
    file_name = 'IMAGES/background.png'
    pil_image = Image.open(file_name)

    # Resize the image to the window size
    w, h = pil_image.size
    final_scale = min(h / y_dimension, w / x_dimension)
    width_final = int(w / final_scale)
    height_final = int(h / final_scale)
    final_pil_image = pil_image.resize((width_final, height_final), Image.ANTIALIAS)

    # Creates a Tk Image
    tk_image = ImageTk.PhotoImage(final_pil_image)

    # Creates a Canvas Image
    c.create_image(x_dimension / 2, y_dimension / 2, anchor='center', image=tk_image)
    c.image = tk_image

# Creates "windows" ------------------------------------------------------------------------------
if True:
    frame_1 = tk.Frame(root, bg='black')
    frame_1.grid(sticky='nsew')
    frame_1.rowconfigure(0, weight=1)
    frame_1.columnconfigure(0, weight=1)

    button = tk.Button(frame_1, bg='dark gray', text='Show / Hide\n The Other Frame', command=show_hide_frame)
    button.grid(sticky='nsew', row=0, column=0, padx=(0, 2), pady=(0, 2))

    frame_2 = tk.Frame(root, bg='black')
    frame_2.grid(sticky='nsew')
    frame_2.rowconfigure(0, weight=1)
    frame_2.columnconfigure(0, weight=1)

    label = tk.Label(frame_2, text='I am the other frame', bg='dark gray')
    label.grid(sticky='nsew', row=0, column=0, padx=(0, 2), pady=(0, 2))

    c.create_window(10, 10, anchor='nw', window=frame_1, height=100, width=200)

    second_window_id = c.create_window(220, 10, anchor='nw', window=frame_2,
                                       height=y_dimension-20, width=x_dimension-230,
                                       state='hidden')


if __name__ == '__main__':
    root.mainloop()
