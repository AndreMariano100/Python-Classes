# App Imports ----------------------------------------------------------------------------------------------------------
import tkinter as tk

# App Configurations ---------------------------------------------------------------------------------------------------
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


# App Main Class -------------------------------------------------------------------------------------------------------
class MyApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # Configure root
        self.iconbitmap('IMAGES/engineering.ico')
        self.title('Tkinter as OOP')
        self.minsize(APP_WIDTH, APP_HEIGHT)
        self.configure(bg='gray5')
        self.columnconfigure(0, weight=1)

        # Adjust root position
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_position = (screen_width / 2) - (APP_WIDTH / 2)
        y_position = (screen_height / 2) - (APP_HEIGHT / 2)
        self.geometry('%dx%d+%d+%d' % (APP_WIDTH, APP_HEIGHT, x_position, y_position))

        # Create widgets
        for i in range(5):
            label = tk.Label(self, text=f'Label {i}', bg='gray30')
            label.grid(row=i, column=0, pady=10, padx=10, sticky='nsew')
            self.rowconfigure(i, weight=1)

        self.very_important_variable = 10
        self.method_a()
        self.method_b()

        print(self.very_important_variable)

    def method_a(self):
        self.very_important_variable += 10

    def method_b(self):
        self.very_important_variable *= 5


# Initialize the App ---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
