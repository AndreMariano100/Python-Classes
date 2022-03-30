# App Imports ----------------------------------------------------------------------------------------------------------
import os
import tkinter as tk

# Configuration --------------------------------------------------------------------------------------------------------
if True:
    window_min_size = [300, 480]

    screen_font_1 = ('OpenSans', 10, 'bold italic')
    screen_font_2 = ('OpenSans', 12, 'italic')
    screen_font_3 = ('Arial', 30)

    button_font_bold = ('OpenSans', 12, 'bold')
    button_font_italic = ('OpenSans', 12, 'italic')
    button_font_normal = ('OpenSans', 12)

    fg_color = '#FEFEFE'
    bg_color = '#2D2C2C'

    bt_color_1 = '#232323'
    bt_color_2 = '#0A0A0A'
    eq_color = '#6F6C6C'


# Program Functions ----------------------------------------------------------------------------------------------------
def color_adjust(event):
    """ Adjust the color of the widget as the user hovers over it"""

    widget = event.widget
    current_background = widget.cget('background')
    old_hex = current_background.lstrip('#')
    rgb = tuple(int(old_hex[i:i + 2], 16) for i in (0, 2, 4))
    if str(event.type) == '7':
        new_rgb = [element + 20 for element in rgb]

    else:
        new_rgb = [element - 20 for element in rgb]
    new_hex = ('#%02x%02x%02x' % (new_rgb[0], new_rgb[1], new_rgb[2]))
    event.widget.configure(bg=new_hex)


def numbers_adjust(typed):
    """
    Responds to numerical values typed by the user
    Acceptable values:
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '⁺∕₋')

    Global Variables:
        clear =  if True erases previous values from the screen
                (an old_value has been stored, and a new value is being entered)
    """
    global clear

    if clear:
        entry_var_3.set(typed)
        clear = False

    else:
        current_screen = entry_var_3.get()
        if typed != '⁺∕₋':
            if current_screen == '0' and typed != '.':
                entry_var_3.set(typed)
            else:
                entry_var_3.set(current_screen + typed)
        else:
            if current_screen:
                if current_screen[0] != '-':
                    entry_var_3.set(f'-{current_screen}')
                else:
                    entry_var_3.set(current_screen[1:])


def del_adjust(typed):
    """
    Responds to clearing values options
    Acceptable values:
        del_operations = ('CE', 'C', 'DEL')

    Global Variables:
        old_value = if 'C' is typed, the old_value is erased
        operation = if 'C' is typed, the operation is erased
        new_value = if 'C' or 'CE' is typed, the new value is erased
    """
    global old_value, new_value, operation, halt

    if halt:
        entry_var_2.set('')
        entry_var_3.set('0')
        old_value = 0
        new_value = 0
        operation = ''
        halt = False
        return

    if typed == 'CE':
        new_value = 0
        entry_var_3.set('0')

    elif typed == 'C':
        entry_var_2.set('')
        entry_var_3.set('0')
        new_value = 0
        old_value = 0
        operation = ''

    elif typed == 'DEL':
        deleted_value = entry_var_3.get()[:-1]
        if not deleted_value:
            deleted_value = '0'
        entry_var_3.set(deleted_value)


def memory_adjust(typed):
    """
    Responds to Memory Related Operations

    Acceptable values:
        memory_operations = ('MC', 'MS', 'MR', 'M+', 'M-', 'M*')

    Global Variable:
        clear = if the user interacts with the stored memory,
                the calculator will interpret that the input number is finished
        operation = uses the opportunity to erase any operation in memory
        old_value = uses the opportunity to replace the old_value with the updated memory value
        new_value = uses the opportunity to erase the new_value

    """
    global clear, old_value, operation, new_value

    clear = True
    value = ''

    # Grab current memory and screen values
    current_memory_value = entry_var_1.get()
    current_screen_value = float(entry_var_3.get())

    if not current_memory_value:
        current_memory_value = 0
    else:
        current_memory_value = float(current_memory_value.split(':')[1])

    # Makes the applicable adjustments
    if typed == 'MC':
        value = ''

    elif typed == 'MS':
        value = current_screen_value

    elif typed == 'MR':
        entry_var_3.set(str(current_memory_value))
        old_value = value
        new_value = 0
        operation = ''
        value = current_memory_value

    elif typed == 'M+':
        value = current_screen_value + current_memory_value

    elif typed == 'M-':
        value = current_memory_value - current_screen_value

    elif typed == 'M*':
        value = current_screen_value * current_memory_value

    # Adjusts the screen with the current value
    if value:
        entry_var_1.set(f'M: {str(value)}')
    else:
        entry_var_1.set('')


def regular_operations_adjust(typed):
    """
    Responds to regular operations
        regular_operations = ('÷', 'x', '-', '+')

    If an operation is already selected, replaces it.
    If a full sentence is already selected, calculate the result and prepares the next calculation.
    Global Variables:
        old_value = first value of the calculation (in memory)
        operation = operation to be performed. If in memory, replaces it
        new_value = second value of the operation (on screen)
        clear = flag that shows that the next input clears the current screen

    """
    global old_value, new_value, operation, clear

    regular_operations = {'÷': '/', 'x': '*', '-': '-', '+': '+'}

    if not operation:
        old_value = float(entry_var_3.get())
        new_value = 0
        operation = regular_operations.get(typed)
        clear = True

    elif operation and clear:
        operation = regular_operations.get(typed)

    elif old_value and operation:
        equal_sign_adjust()
        new_value = 0
        operation = regular_operations.get(typed)
        clear = True

    entry_var_2.set(f'{old_value} {operation}')


def special_operations_adjust(typed):
    """
    Responds to Special Operations:
        special_operations = ('%', '1/X', 'x²', '√X')

    Global Variables:
        old_value = used to calculate percentages
        new_value = used to apply the special operation
    """

    global old_value, new_value, clear
    new_value = float(entry_var_3.get())

    if typed == 'x²':
        new_value = new_value**2

    elif typed == '1/x':
        if new_value == 0:
            entry_var_2.set('Error - Division by Zero')
            new_value = 0
        else:
            new_value = 1/new_value

    elif typed == '√x':
        if new_value < 0:
            entry_var_2.set('Error - Square root of a negative number')
            new_value = 0
        else:
            new_value = new_value**0.5

    elif typed == '%':
        if not old_value:
            new_value = 0
        else:
            new_value = old_value * new_value/100

    clear = True
    entry_var_3.set(str(new_value))


def equal_sign_adjust():
    """
    Responds to the user selecting the '=' button.
    If the user selects an ordinary operation (+, -, /, *) with and operation
    already in memory it executes the same way.
    Global Variables:
        old_value = first value of the operation (in memory)
        new_value = second value of the operation (on screen)
        operation = operation to be performed (in memory)
        clear = flag that shows that the next input clears the current screen
    """
    global old_value, new_value, operation, clear

    if old_value and operation:
        new_value = float(entry_var_3.get())
        string = f'{old_value}{operation}{new_value}'
        try:
            result = eval(string)
        except ZeroDivisionError:
            entry_var_2.set('Error - Division by Zero')
            entry_var_3.set(0)
        else:
            entry_var_2.set(f'{string}=')
            entry_var_3.set(str(result))
            clear = True
            old_value = result


def main_action(event):
    global clear, old_value, new_value, memory, halt
    global entry_var_1, entry_var_2, entry_var_3

    typed = event.widget.cget('text')

    if 'error' in str(entry_var_2.get()).lower():
        halt = True

    # Responds to numerical values entry by the user
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '⁺∕₋')
    if typed in numbers and not halt:
        numbers_adjust(typed)

    # Responds to CE/C/Del Operations
    del_operations = ('CE', 'C', 'DEL')
    if typed in del_operations:
        del_adjust(typed)

    # Responds to Memory Related Buttons
    memory_operations = ('MC', 'MS', 'MR', 'M+', 'M-', 'M*')
    if typed in memory_operations and not halt:
        memory_adjust(typed)

    # Responds to Regular Operations
    regular_operations = ('÷', 'x', '-', '+')
    if typed in regular_operations and not halt:
        regular_operations_adjust(typed)

    # Responds to Special Operations
    special_operations = ('%', '1/x', 'x²', '√x')
    if typed in special_operations and not halt:
        special_operations_adjust(typed)

    # Responds to the Equal Sign
    if typed == '=' and not halt:
        equal_sign_adjust()


# Constructs and Configures the Main Window ----------------------------------------------------------------------------
if True:
    root = tk.Tk()
    root.iconbitmap(os.path.join(os.getcwd(), 'Images', 'Calculator.ico'))
    root.title('My Calculator')

    root.minsize(window_min_size[0], window_min_size[1])
    root.configure(bg=bg_color)
    root.resizable(height=0, width=0)
    for i in range(4):
        root.columnconfigure(i, weight=1)
    for i in range(10):
        root.rowconfigure(i, weight=1)

    # Get Screen width and height
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

    # Position the program window centered on screen
    x_position = int((screen_width / 2) - (window_min_size[0] / 2))
    y_position = int((screen_height / 2) - (window_min_size[1] / 2))
    root.geometry(f'{window_min_size[0]}x{window_min_size[1]}+{x_position}+{y_position}')

# Creates the calculator screen ----------------------------------------------------------------------------------------
if True:
    entry_var_1 = tk.StringVar(value='')
    entry_var_2 = tk.StringVar(value='')
    entry_var_3 = tk.StringVar(value='0')
    entry_1 = tk.Entry(root, justify='left', font=screen_font_1, textvariable=entry_var_1, relief='flat',
                       state='disabled', disabledbackground=bg_color, disabledforeground='gray55')
    entry_2 = tk.Entry(root, justify='right', font=screen_font_2, textvariable=entry_var_2, relief='flat',
                       state='disabled', disabledbackground=bg_color, disabledforeground='gray55')
    entry_3 = tk.Entry(root, justify='right', font=screen_font_3, textvariable=entry_var_3, relief='flat',
                       state='disabled', disabledbackground=bg_color, disabledforeground=fg_color)
    entry_1.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=2)
    entry_2.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=10, pady=2)
    entry_3.grid(row=2, column=0, columnspan=4, sticky='nsew', padx=10, pady=2)

# Creates the remaining buttons ----------------------------------------------------------------------------------------
if True:
    # Memory related buttons
    frame = tk.Frame(root, bg=bg_color)
    frame.grid(row=3, column=0, columnspan=4, sticky='nsew')
    for i in range(6):
        frame.columnconfigure(i, weight=1)
    frame.rowconfigure(0, weight=1)
    labels = ('MC', 'MS', 'MR', 'M+', 'M-', 'M*')

    for i, label in enumerate(labels):
        button = tk.Label(frame, text=label, bg=bg_color, fg=fg_color, font=button_font_normal)
        button.grid(row=0, column=i, sticky='nsew', padx=1, pady=1)
        button.bind('<Button-1>', main_action)
        button.bind("<Enter>", color_adjust)
        button.bind("<Leave>", color_adjust)

    # Remaining buttons
    labels = ('%', 'CE', 'C', 'DEL',
              '1/x', 'x²', '√x', '÷',
              '7', '8', '9', 'x',
              '4', '5', '6', '-',
              '1', '2', '3', '+',
              '⁺∕₋', '0', '.', '=')
    dark_labels = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '⁺∕₋', '0', '.')
    special_labels = ('1/x', 'x²', '√x')

    row = 4
    column = 0
    for i, label in enumerate(labels):
        if label in dark_labels:
            bg = bt_color_2
            font = button_font_bold
        elif label in special_labels:
            bg = bt_color_1
            font = button_font_italic
        elif label == '=':
            bg = eq_color
            font = button_font_normal
        else:
            bg = bt_color_1
            font = button_font_normal

        if column == 4:
            column = 0
            row += 1

        button = tk.Label(root, text=label, bg=bg, fg=fg_color, font=font, pady=4)
        button.grid(row=row, column=column, sticky='nsew', padx=1, pady=1)
        button.bind('<Button-1>', main_action)
        button.bind("<Enter>", color_adjust)
        button.bind("<Leave>", color_adjust)
        column += 1

# Main Program set to run ----------------------------------------------------------------------------------------------
if __name__ == '__main__':
    clear = False
    old_value = 0
    operation = ''
    new_value = 0
    memory = 0
    halt = False
    root.mainloop()
