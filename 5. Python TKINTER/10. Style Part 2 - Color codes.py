import tkinter as tk

def change_color(sign):
    global my_label, white, black
    # Convert to RGB
    old_hex_code = my_label.cget('bg').lstrip('#')
    rgb = tuple(int(old_hex_code[i:i + 2], 16) for i in (0, 2, 4))
    new_rgb_code = [element + sign * 10 for element in rgb]
    new_hex = f'#{new_rgb_code[0]:x}{new_rgb_code[1]:x}{new_rgb_code[1]:x}'

    for color in new_rgb_code:
        if color > 255:
            color = 255

    if new_rgb_code[0] < 100:
        fg = 'white'
    else:
        fg = 'black'
    my_label.config(fg=fg, bg=new_hex, text=f'{str(new_hex)} / {str(new_rgb_code)}')

# HEX Colors
# #RRGGBB
# RR = hexadecimal conversion of the red value: from 0 to 255

white = '#ffffff'
black = '#000000'
red = '#FF0000'
green = '#00FF00'
blue = '#0000FF'
silver = '#C0C0C0'

root = tk.Tk()
root.title("HEX COLORS")
root.columnconfigure(0, weight=1)

my_colors = (white, black, red, green, blue, silver)

for i, value in enumerate(my_colors):
    label = tk.Label(root, width=50, text=str(value), bg=value)
    label.grid(column=0, row=i, sticky='nsew')

    if value == silver:
        my_label = label

button_1 = tk.Button(root, text='Darker', command=lambda: change_color(-1))
button_1.grid(row=i+1, column=0)

button_2 = tk.Button(root, text='Lighter', command=lambda: change_color(+1))
button_2.grid(row=i+2, column=0)

if __name__ == '__main__':
    root.mainloop()
