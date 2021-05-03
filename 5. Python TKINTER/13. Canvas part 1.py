import tkinter as tk

root = tk.Tk()

# Create Canvas ---------------------------------------------------------------------------------
if True:
    x_dimension = 300
    y_dimension = 300
    c = tk.Canvas(root, width=x_dimension, height=y_dimension, bg='white')
    c.grid(row=0, column=0, sticky='nsew')

# Create Line -----------------------------------------------------------------------------------
if True:
    pass
    # # create_line(x0, y0, x1, y1, ..., xn, yn, options...) ⇒ id
    # y_start = 10, y_dimension - 10
    # y_finish = 10, 10
    # x_start = y_start
    # x_finish = x_dimension-10, y_dimension - 10
    # graph_line_start = y_start
    # graph_line_end = x_dimension-20, 20
    #
    # y_axe = c.create_line(*y_start, *y_finish, arrow='last')
    # x_axe = c.create_line(*x_start, *x_finish, arrow='last')
    # graph = c.create_line(*graph_line_start, *graph_line_end, width=7, fill='red', capstyle='butt')
    #
    # width=2, fill='red'
    # arrow='last' # 'first', 'last', 'both'
    # arrowshape=(10, 10, 5)
    # capstyle='round' # 'butt', 'projecting', 'round'
    #
    # # Multiple lines
    # p_1 = y_start
    # p_2 = 50, 40
    # p_3 = 100, y_dimension - 30
    # p_4 = 200, y_dimension - 250
    # p_5 = graph_line_end
    # graph_2 = c.create_line(*p_1, *p_2, *p_3, *p_4, *p_5, fill='blue', width=5)

    # smooth=1
    # splinesteps=12

# Create Oval -----------------------------------------------------------------------------------
if True:
    pass
    # create_oval(x0, y0, options...) ⇒ id
    # oval_box = (10, y_dimension/3, x_dimension-10, 2*y_dimension/3)
    # c.create_oval(oval_box, fill='black', outline='red', width=2)

# Create Arc ------------------------------------------------------------------------------------
if True:
    # create_arc(x0, y0, x1, y1, options...) ⇒ id
    # create_arc(box, options...) ⇒ id

    border = 10
    # coordinates = (border, border, x_dimension - border, y_dimension - border)
    # id_1 = c.create_arc(coordinates, start=0, extent=270, fill='green')
    # id_2 = c.create_arc(coordinates, start=270, extent=60, fill='dark green')
    # id_3 = c.create_arc(coordinates, start=330, extent=30, fill='light green')

    # Arc Options
    # c.delete(id_2)
    # c.delete(id_3)
    # new_coords = (i+5 for i in coordinates)
    # c.coords(id_3, *new_coords)
    # c.itemconfigure(id_1, style='arc')  # delete other parts: pieslice, chord, arc
    # c.itemconfigure(id_1, outline='red', width=3)

# Other objects ---------------------------------------------------------------------------------
# Polygon:  create_polygon(xy, options...) ⇒ id
#           create_polygon(x0, y0, x1, y1, x2, y2, ..., xn, yn, options...) ⇒ id
# Rectangle: create_rectangle(x0, y0, x1, y1, options...) ⇒ id
# Text: create_text(x0, y0, options...) ⇒ id
#        -> text, font, justify

if __name__ == '__main__':
    root.mainloop()
