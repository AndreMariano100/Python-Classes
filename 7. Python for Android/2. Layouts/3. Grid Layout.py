"""
The GridLayout arranges children in a matrix. It takes the available space and divides it into columns and rows,
then adds widgets to the resulting “cells”.

Background

    Unlike many other toolkits, you cannot explicitly place a widget in a specific column/row.
    Each child is automatically assigned a position determined by the layout configuration and the child’s index
    in the children list.

    A GridLayout must always have at least one input constraint: GridLayout.cols or GridLayout.rows.
    If you do not specify cols or rows, the Layout will throw an exception.

Column Width and Row Height

    The column width/row height are determined in 3 steps:

        The initial size is given by the col_default_width and row_default_height properties.
        To customize the size of a single column or row, use cols_minimum or rows_minimum.

        The size_hint_x/size_hint_y of the children are taken into account.
        If no widgets have a size hint, the maximum size is used for all children.

        You can force the default size by setting the col_force_default or row_force_default property.
        This will force the layout to ignore the width and size_hint properties of children and use the default size.

Using a GridLayout

In the example below, all widgets will have an equal size. By default, the size_hint is (1, 1), so a Widget will
take the full size of the parent:

layout = GridLayout(cols=2)
layout.add_widget(Button(text='Hello 1'))
layout.add_widget(Button(text='World 1'))
layout.add_widget(Button(text='Hello 2'))
layout.add_widget(Button(text='World 2'))


Now, let’s fix the size of Hello buttons to 100px instead of using size_hint_x=1:

layout = GridLayout(cols=2)
layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
layout.add_widget(Button(text='World 1'))
layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
layout.add_widget(Button(text='World 2'))


Next, let’s fix the row height to a specific size:

layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
layout.add_widget(Button(text='World 1'))
layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
layout.add_widget(Button(text='World 2'))


"""