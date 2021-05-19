# App Imports
import tkinter as tk
from PIL import ImageTk, Image

global pil_image, my_image, label_2


######################################################################################################
def resize(event):
    global pil_image, my_image, label_2

    # New window size
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    print('Window size:', new_width, new_height)

    # Scale Factors
    original_width, original_height = pil_image.size
    print('Image size:', original_width, original_height)
    factor_width = original_width / new_width
    factor_height = original_height / (new_height-label_height)
    scale_factor = max(factor_width, factor_height)

    # Final Size
    final_width = int(original_width / scale_factor)
    final_height = int(original_height / scale_factor)
    new_image = pil_image.resize((final_width, final_height), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(new_image)
    label_2.configure(image=my_image)


######################################################################################################
# Constructs the Main Window
root = tk.Tk()
image_size = (800, 400)
label_height = 50
root.geometry(f'{image_size[0]}x{image_size[1]+label_height}')
root.configure(bg='gray30')
root.columnconfigure(0, weight=1, minsize=image_size[0])
root.rowconfigure(0, weight=0, minsize=label_height)
root.rowconfigure(1, weight=1, minsize=image_size[1])

label_1 = tk.Label(root, text='User Image', bg='white')
label_1.grid(row=0, column=0, sticky='nsew', pady=10)

# No resizing
# my_image = ImageTk.PhotoImage(Image.open('Images/logo.jpg'))
# label_2 = tk.Label(root, image=my_image)
# label_2.grid(row=1, column=0, sticky='nsew')

# # Resizing
# im_width = 600
# im_height = 400
#
# image_file = 'Images/logo.jpg'
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

# Dinamically Resize Window
image_file = 'Images/logo.jpg'
pil_image = Image.open(image_file)
original_width, original_height = pil_image.size
factor_width = original_width / image_size[0]
factor_height = original_height / image_size[1]
scale_factor = max(factor_width, factor_height)
final_width = int(original_width / scale_factor)
final_height = int(original_height / scale_factor)
pil_image = pil_image.resize((final_width, final_height), Image.ANTIALIAS)

my_image = ImageTk.PhotoImage(pil_image)
label_2 = tk.Label(root, image=my_image)
label_2.grid(row=1, column=0, sticky='nsew')
root.update_idletasks()
root.bind('<Configure>', resize)

######################################################################################################
# Main Program
if __name__ == '__main__':
    root.mainloop()
