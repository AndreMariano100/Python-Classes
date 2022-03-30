import tkinter as tk

root = tk.Tk()
root.title("Options Data Base")
root.columnconfigure(0, weight=1)
root.option_readfile('IMAGES/options_db.txt')

label = tk.Label(root, width=50, text='a label')
label.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

button = tk.Button(root, text='a button')
button.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)

if __name__ == '__main__':
    root.mainloop()
