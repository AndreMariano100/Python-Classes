# App Imports
import tkinter as tk
from PIL import ImageTk, Image

global pil_image, my_image, label_2


######################################################################################################
def resize(event):
    global pil_image, my_image, label_2
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    print('Window size:', new_width, new_height)

    original_width, original_height = pil_image.size
    print('Image Size:', original_width, original_height)

    factor_width = original_width / new_width
    factor_height = original_height / new_height
    scale_factor = max(factor_width, factor_height)
    print('Scale Factor:', scale_factor)

    final_width = int(original_width / scale_factor)
    final_height = int(original_height / scale_factor)
    print('New Image Size:', final_width, final_height)
    new_image = pil_image.resize((final_width, final_height), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(new_image)
    label_2.configure(image=my_image)


######################################################################################################
# Constructs the Main Window
root = tk.Tk()

label_1 = tk.Label(root, text='User Image', bg='white')
label_1.grid(row=0, column=0, sticky='nsew', pady=(10, 5))

# No resizing
my_image = ImageTk.PhotoImage(Image.open('Images/logo.jpg'))
label_2 = tk.Label(root, image=my_image)
label_2.grid(row=1, column=0, sticky='nsew')

# # Resizing
# im_width = 600
# im_height = 400
#
# image_file = 'logo.jpg'
# pil_image = Image.open(image_file)
# original_width, original_height = pil_image.size
# factor_width = original_width / im_width
# factor_height = original_height / im_height
# scale_factor = max(factor_width, factor_height)
# final_width = int(original_width / scale_factor)
# final_height = int(original_height / scale_factor)
# new_pil_image = pil_image.resize((final_width, final_height), Image.ANTIALIAS)
#
# my_image = ImageTk.PhotoImage(new_pil_image)
# image_label = tk.Label(root, image=my_image, anchor='center')
# image_label.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
#
# # Dinamically Resize
# root.bind('<Configure>', resize)
# image_file = 'logo.jpg'
# pil_image = Image.open(image_file)
# my_image = ImageTk.PhotoImage(pil_image)
# label_2 = tk.Label(root, image=my_image)
# label_2.grid(row=1, column=0, sticky='nsew')


######################################################################################################
# Main Program
if __name__ == '__main__':
    root.mainloop()
