#################################################################################################
import tkinter as tk

root = tk.Tk()

'''
You may get the keys to the available properties of the root with: print(root.keys())
['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 'background', 'bg',
 'colormap', 'container', 'cursor', 'height', 'highlightbackground', 'highlightcolor', 
 'highlightthickness', 'padx', 'pady', 'takefocus', 'visual', 'width']

'''

# And you may sets properties and configuration
# Examples
root.configure(bg="black", bd=5)  # same as (background='black", borderwidth=3)
root.configure(relief='sunken')  # Other reliefs: plain, raised, groove, ridge
root.configure(highlightbackground='yellow', highlightcolor='red', highlightthickness=3)
root.configure(height=300, width=600)

new_window = tk.Toplevel()
new_window.configure(bg='green')
new_window.configure(height=200, width=300)

# And you may get the properties with: root.cget(key)
bg_color = root.cget('background')
border = root.cget('borderwidth')
print(f'Background color: {bg_color}. Border: {border}')

##################################################################################################
if __name__ == '__main__':
    root.mainloop()
