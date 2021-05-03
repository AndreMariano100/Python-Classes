'''
FRAME STANDARD OPTIONS:
    background, bd, bg, borderwidth, class, padx, pady,
    colormap, container, cursor, height,
    highlightbackground, highlightcolor, highlightthickness,
    relief, takefocus, visual, width.

    --> relief styles: flat, raised, sunken, groove, ridge

LABEL FRAME STANDARD OPTIONS:
    same as FRAME

LABEL FRAME-SPECIFIC OPTIONS
    text, font, foreground, labelanchor, labelwidget
'''

import tkinter as tk

# Create the Main Window
root = tk.Tk()
root.iconbitmap('Images\Python.ico')
root.title('TKINTER Frames')
# root.minsize(500, 200)

# Configure the root for the upcoming frames.
# Creating two frames on the first row, and a third
# frame on the second row crossing two columns
root.columnconfigure(0, weight=1, minsize=200)
root.columnconfigure(1, weight=4, minsize=300)
root.rowconfigure(0, weight=1, minsize=150)
root.rowconfigure(1, weight=0, minsize=50)

# Build the frames into the root
# When creating frames and widgets you shall always first include the base widget to which
# they will be applied to (in this case the root window). The other keyword arguments
# may be passed in any order.
frame_1 = tk.Frame(root, bg='red', bd=2, relief='sunken')
frame_1.grid(row=0, column=0, sticky='nsew')

frame_2 = tk.LabelFrame(root, bg='blue', bd=2, relief='raised', text='Blue Frame')
frame_2.grid(row=0, column=1, sticky='nsew')

frame_3 = tk.Frame(root, bg='gray', bd=2, relief='groove')
frame_3.grid(row=1, column=0, columnspan=2, sticky='nsew')

if __name__ == '__main__':
    root.mainloop()

'''
Grid Geometry Manager Options:
    w.grid(column=0, row=0, columnspan=2, rowspan=2, ipadx=1, ipady=3, padx=2, pady=2, sticky='nsew')
    
    column = number     - use cell identified with given column (starting with 0)
    row = number        - use cell identified with given row (starting with 0)
    columnspan = number - this widget will span several columns
    rowspan = number    - this widget will span several rows
    ipadx = amount      - add internal padding in x direction
    ipady = amount      - add internal padding in y direction
    padx = amount       - add padding in x direction
    pady = amount       - add padding in y direction
    sticky = NSEW       - if cell is larger on which sides will this widget stick to the cell boundary
    

Other Grid Options
    w.grid(option=value)            - standard grid method
    w.grid_configure(option=value)  - adjusts the options
    w.grid_forget()        - unmap the widget
    w.grid_remove()        - unmap the widget, but remember the grid options
    w.grid_info()          - returns information about the grid option
    w.grid_propagate(0)    - não permite redimensionar

Configuring Columns and Rows
    w.columnconfigure(columns_number, weight=1, minsize=50, pad=5)
    w.rowconfigure(row_number, weight=1, minsize=50, pad=5)

The PACK option:
    w.pack(side='left', anchow='nw', fill='y', expand='yes')

    side    -> left, right, up, down
    fill    -> x, y, both
    anchor  -> n, s, e, w, ne, nw, se, sw, center   
'''
