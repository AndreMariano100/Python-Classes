import tkinter as tk

def change_color(sign):
    global my_label, white, black

    # Convert to RGB
    old_hex_code = my_label.cget('bg').lstrip('#')
    red = int(old_hex_code[0:2], 16)
    green = int(old_hex_code[2:4], 16)
    blue = int(old_hex_code[4:6], 16)
    new_rgb_code = [red, green, blue]

    for i, color in enumerate(new_rgb_code):
        new_rgb_code[i] = max(0, min(color + sign*10, 255))

    if new_rgb_code[0] < 100:
        fg = 'white'
    else:
        fg = 'black'

    new_hex = "#{:02x}{:02x}{:02x}".format(new_rgb_code[0], new_rgb_code[1], new_rgb_code[2])
    my_label.config(fg=fg, bg=new_hex, text=f'{str(new_hex)} / {str(new_rgb_code)}')

# HEX Colors
# #RRGGBB
# RR = hexadecimal conversion of the red value: from 0 to 255

# Main colors ----------------------------------------------------------------------------------------------------------
white = '#ffffff'
black = '#000000'
red = '#FF0000'
green = '#00FF00'
blue = '#0000FF'
silver = '#C0C0C0'

# Root -----------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.config(bg='seagreen')
root.title("HEX COLORS")
root.columnconfigure(0, weight=1)

my_colors = (white, black, red, green, blue, silver)

for i, value in enumerate(my_colors):
    if value == black:
        fg = white
    else:
        fg = black
    if value == silver:
        width = 40
        height = 3
        padx = 30
    else:
        width = 50
        height = 1
        padx = 10
    label = tk.Label(root, width=width, height=height, text=value, bg=value, fg=fg)
    label.grid(column=0, row=i, sticky='nsew', padx=padx, pady=10)

    if value == silver:
        my_label = label

button_1 = tk.Button(root, text='Darker', width=40, command=lambda: change_color(-1))
button_1.grid(row=i+1, column=0, pady=10)

button_2 = tk.Button(root, text='Lighter', width=40, command=lambda: change_color(+1))
button_2.grid(row=i+2, column=0, pady=10)

if __name__ == '__main__':
    root.mainloop()
