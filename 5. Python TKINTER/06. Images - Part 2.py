# App Imports
import tkinter as tk
from tkinter import ttk
global pil_image, my_image, label_2

######################################################################################################
root = tk.Tk()

frame_1 = tk.LabelFrame(root, text='XBM Files')
frame_1.grid(row=0, column=0)
image_1 = tk.BitmapImage(file='Images/file_new.xbm')
image_2 = tk.BitmapImage(file='Images/file_open.xbm', background='white', foreground='black')

label_1 = tk.Label(frame_1, image=image_1, text='New File', compound='top')
label_1.grid(row=0, column=0, sticky='nsew')
label_2 = tk.Label(frame_1, image=image_2, text='Open File', compound='bottom')
label_2.grid(row=0, column=1, sticky='nsew')

image_3 = tk.BitmapImage(file='Images/worldwide_icon.xbm')
button_1 = tk.Button(frame_1, text='Word Wide Web', image=image_3, compound='left')
button_1.grid(row=1, column=0)

button_2 = tk.Button(frame_1, text='Coding', bitmap='@Images/file_open.xbm', compound='right')
button_2.grid(row=1, column=1)


frame_2 = tk.LabelFrame(root, text='GIF Files')
frame_2.grid(row=0, column=1)
image_4 = tk.PhotoImage(file='Images/python_logo.gif')
button_3 = ttk.Button(frame_2, text='text', image=image_4, compound='left')
button_3.grid(row=0, column=0, sticky='nsew')

######################################################################################################
# Main Program
if __name__ == '__main__':
    root.mainloop()
