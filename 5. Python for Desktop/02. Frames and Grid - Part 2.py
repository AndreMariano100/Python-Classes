'''
Testing relief styles with different border widths
'''
import tkinter as tk

root = tk.Tk()
frame_1 = tk.Frame(root, bg='gray20')
frame_2 = tk.Frame(root, bg='gray30')
frame_1.grid(row=0, column=0, sticky='nsew')
frame_2.grid(row=1, column=0, sticky='nsew')
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.columnconfigure(0, weight=1)
root.resizable(height=0, width=0)

for bdw in range(5):
    frame = tk.Frame(frame_1, borderwidth=bdw)
    frame.grid(row=bdw, column=0, pady=10, padx=5)
    label = tk.Label(frame, text='borderwidth = %d ' % bdw)
    label.grid(row=0, column=0, padx=2)

    relief_set = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

    for i, relief in enumerate(relief_set):
        frame = tk.Frame(frame_1, borderwidth=bdw, relief=relief)
        frame.grid(row=bdw, column=i+1, padx=5)
        label = tk.Label(frame, text=relief, width=10)
        label.grid(row=0, column=0)


for bdw in range(5):
    frame = tk.LabelFrame(frame_2, borderwidth=bdw, text='Label')
    frame.grid(row=bdw, column=0, pady=10, padx=5)
    label = tk.Label(frame, text='borderwidth = %d ' % bdw)
    label.grid(row=0, column=0)

    relief_set = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

    for i, relief in enumerate(relief_set):
        frame = tk.LabelFrame(frame_2, borderwidth=bdw, relief=relief, text='Label')
        frame.grid(row=bdw, column=i+1, padx=5)
        label = tk.Label(frame, text=relief, width=10)
        label.grid(row=0, column=0)

if __name__ == '__main__':
    root.mainloop()
