# App Imports -----------------------------------------------------------------------------------------
import tkinter as tk

# App Configurations ----------------------------------------------------------------------------------
if True:
    # Fonts
    LARGE_FONT = ("SansSerif", 12, 'bold')
    MEDIUM_FONT = ("SansSerif", 11)
    SMALL_FONT = ("SansSerif", 9)

    # Colors
    BG_COLOR = "#FFFFFF"  # White Background
    FG_COLOR = "#E0E0E0"  # Light Gray Foreground

    # App initial window size
    APP_WIDTH = 600
    APP_HEIGHT = 400

# Global Variables ------------------------------------------------------------------------------------
global very_important_variable


# App Methods -----------------------------------------------------------------------------------------
def configure_root(root):
    root.iconbitmap('IMAGES\engineering.ico')
    root.title('Tkinter as Non OOP')
    root.minsize(APP_WIDTH, APP_HEIGHT)
    root.configure(bg='gray5')
    root.columnconfigure(0, weight=1)


def adjust_root_position(root):
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x_position = (screen_width / 2) - (APP_WIDTH / 2)
    y_position = (screen_height / 2) - (APP_HEIGHT / 2)
    root.geometry('%dx%d+%d+%d' % (APP_WIDTH, APP_HEIGHT, x_position, y_position))


def method_a():
    global very_important_variable
    very_important_variable += 10


def method_b():
    global very_important_variable
    very_important_variable *= 5


def create_widgets(root):
    global very_important_variable

    for i in range(5):
        label = tk.Label(root, text=f'Label {i}', bg='gray30')
        label.grid(row=i, column=0, pady=10, padx=10, sticky='nsew')
        root.rowconfigure(i, weight=1)

    very_important_variable = 10

    method_a()
    method_b()
    print(very_important_variable)


# App Main Program -----------------------------------------------------------------------------------
if True:
    master = tk.Tk()
    configure_root(master)
    adjust_root_position(master)
    create_widgets(master)

if __name__ == '__main__':
    master.mainloop()
