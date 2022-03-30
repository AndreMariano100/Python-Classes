"""
Construct a toplevel widget with the parent MASTER.

Valid resource names:
    background, bd, bg, borderwidth, class,
    colormap, container, cursor, height, highlightbackground,
    highlightcolor, highlightthickness, menu, relief, screen, takefocus,
    use, visual, width.

"""

import tkinter as tk


def open_window():
    new = tk.Toplevel()
    label = tk.Label(new, text='New Window')
    label.grid(row=0, column=0)
    quit_button = tk.Button(new, text='Quit', command=new.destroy, width=30)
    quit_button.grid(row=1, column=0, padx=10, pady=10)
    new.grab_set()


root = tk.Tk()
button = tk.Button(root, text='Open new window', command=open_window, width=30)
button.grid(row=0, column=0)

#####################
# Run the App
if __name__ == "__main__":
    root.mainloop()

