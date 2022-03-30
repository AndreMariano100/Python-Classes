"""
https://kivy.org/doc/stable/guide/widgets.html

Organize with Layouts

    layout is a special kind of widget that controls the size and position of its children. There are different
    kinds of layouts, allowing for different automatic organization of their children.

    Layouts use size_hint and pos_hint properties to determine the size and pos of their children.

BoxLayout
    Arranges widgets in an adjacent manner (either vertically or horizontally) manner, to fill all the space.
    The size_hint property of children can be used to change proportions allowed to each child, or set fixed size
    for some of them.

GridLayout
    Arranges widgets in a grid. You must specify at least one dimension of the grid so kivy can compute the size
    of the elements and how to arrange them.

StackLayout
    Arranges widgets adjacent to one another, but with a set size in one of the dimensions, without trying to make
    them fit within the entire space. This is useful to display children of the same predefined size.

AnchorLayout
    A simple layout only caring about children positions. It allows putting the children at a position relative
    to a border of the layout. size_hint is not honored.

FloatLayout
    Allows placing children with arbitrary locations and size, either absolute or relative to the layout size.
    Default size_hint (1, 1) will make every child the same size as the whole layout, so you probably want to change
    this value if you have more than one child.
    You can set size_hint to (None, None) to use absolute size with size.
    This widget honors pos_hint also, which as a dict setting position relative to layout position.

RelativeLayout
    Behaves just like FloatLayout, except children positions are relative to layout position, not the screen.
"""