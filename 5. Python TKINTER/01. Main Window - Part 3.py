"""
Some Valid Property Methods: w stands for the widget name

    w.geometry()     - Sets or gets the window geometry. Uses the following format:
                          "%dx%d%+d%+d" % (width, height, xoffset, yoffset)
    w.iconbitmap()   - Sets or gets the icon bitmap
    w.title()        - Sets or gets the title for the window
    w.configure()    - Sets any of the window resources (color, font, state, etc)
    w.maxsize()      - Maximum window size
    w.minsize()      - Minimum window size
    w.resizable(height=0, width=0) - Controls the resize flags
    w.winfo_width       - Return width of this widget
    w.winfo_height      - Return height of this widget
    w.winfo_children    - Return a list of all widgets which are children of this widget.
    w.winfo_exists()    - Return true if this widget exists.
    w.winfo_geometry    - Return geometry string for this widget in the form "widthxheight+X+Y"
    w.winfo_screenwidth()    - screen width
    w.winfo_screenheight()   - screen height
    w.columnconfigure(num, weight=value, minsize=num)
    w.rowconfigure(num, weight=value, minsize=num)

Valid action methods
    w.iconify()      - Minimizes the window to system tray
    w.deiconify()    - Displays the window (use only after iconify())
    w.withdrawn()    - Removes the window from the screen (use deiconify() to show again)
    w.mainloop()     - Runs the application
    w.destroy()      - Terminates the mainloop()
    w.quit()         - Terminates the mainloop() and destroys all widgets.
    w.cget(key)      - Returns the current value for an option
    w.keys()         - Returns available options

"""

#################################################################################################
# General sequence for creation
import tkinter as tk

root = tk.Tk()  # root is only the name of the widget
"""
print(root.keys())
['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 'background', 'bg', 'colormap', 'container', 
 'cursor', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 'pady', 'takefocus', 
 'visual', 'width']
"""

# Sets the top level main properties
root.iconbitmap('IMAGES\python.ico')
root.title('My title here')

# Set the size
root_width = 300
root_height = 150
root.minsize(root_width, root_height)
# root.maxsize(3*root_width, 3*root_height)

# Alternative you may forbid the resizing of window
# root.resizable(height=0, width=0)

# Also you may define that the window starts at full screen size
# root.state("zoomed")

# Set the position of the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set initial position
x_pos = int((screen_width / 2) - root_width/2)
y_pos = int((screen_height / 2) - root_height/2)
root.geometry(f'{root_width}x{root_height}+{x_pos}+{y_pos}')
# f"{largura}x{altura}+{posição x}+{posição y}"

# You may also remove the windows bar
# root.overrideredirect(1)

# Finally add some widgets
my_label = tk.Label(root, text="I am a label widget")
my_button = tk.Button(root, text="I am a button", command=root.destroy)
my_label.grid()
my_button.grid()
# Alternative
# tk.Label(root, text="I am a label widget").grid()
# tk.Button(root, text="I am a button").grid()

# #################################################################################################

if __name__ == '__main__':
    root.mainloop()
