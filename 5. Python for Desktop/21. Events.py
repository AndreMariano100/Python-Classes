'''

Instances of this type are generated if one of the following events occurs:

    KeyPress, KeyRelease - for keyboard events
    ButtonPress, ButtonRelease, Motion, Enter, Leave, MouseWheel - for mouse events
    Visibility, Unmap, Map, Expose, FocusIn, FocusOut, Circulate, Colormap, Gravity, Reparent,
    Property, Destroy, Activate, Deactivate - for window events.

More usual events:

    ->  widget.bind(<event>, callback)

    Mouse Events
        <Button-1> == <ButtonPress-1> == <1>        - <2> / <3>
        <Button-4>                                  - Scroll Up
        <Button-5>                                  - Scroll Down
        <B1-Motion>                                 - <2> / <3>
        <ButtonRelease-1>                           - <2> / <3>
        <Double-Button-1>                           - <2> / <3>
        <Enter>                                     - Mouse Pointer
        <Leave>                                     - Mouse Pointer

    Keyboard Events
        <FocusIn>                                   - Keyboard Focus
        <FocusOut>                                  - Keyboard Focus
        <Return>                                    - Keyboard 'Enter' Key
            Cancel, BackSpace, Tab, Return, Shift_L, Control_L, Alt_L,
            Pause, Caps_Lock, Escape, Prior (page up), Next (page down),
            End, Home, Left, Up, Right, Down, Print, Insert, Delete,
            F1 ~ F12, Num_Lock, Scroll_Lock

        <Key>                                       - Any key from the keyboard
        letter                                      - 'letter' means any letter from the keyboard

    Window Event
        <Configure>                                 - Change size or location of the widget



If a callback function for one of these events is registered
using bind, bind_all, bind_class, or tag_bind, the callback is
called with an Event as first argument. It will have the
following attributes (in braces are the event types for which
the attribute is valid):

Help on Event in module tkinter object:

class Event(builtins.object)
 |  serial, num - mouse button pressed          (ButtonPress, ButtonRelease)
 |  focus - whether the window has the focus    (Enter, Leave)
 |  height - height of the exposed window       (Configure, Expose)
 |  width - width of the exposed window         (Configure, Expose)
 |  keycode - keycode of the pressed key        (KeyPress, KeyRelease)
 |  state - state of the event as a number      (ButtonPress, ButtonRelease, Enter, KeyPress, KeyRelease, Leave, Motion)
 |  state - state as a string                   (Visibility)
 |  time - when the event occurred
 |  x - x-position of the mouse
 |  y - y-position of the mouse
 |  x_root - x-position of the mouse on the screen      (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
 |  y_root - y-position of the mouse on the screen      (ButtonPress, ButtonRelease, KeyPress, KeyRelease, Motion)
 |  char - pressed character                            (KeyPress, KeyRelease)
 |  send_event - see X/Windows documentation
 |  keysym - keysym of the event as a string            (KeyPress, KeyRelease)
 |  keysym_num - keysym of the event as a number        (KeyPress, KeyRelease)
 |  type - type of the event as a number
 |  widget - widget in which the event occurred
 |  delta - delta of wheel movement                     (MouseWheel)

    For portability reasons, you should stick to char, height, width, x, y, x_root, y_root, and widget
    unless you know exactly what you're doing.

'''

import tkinter as tk


def show_mouse_events(event):
    print('Mouse event')
    """
    print(dir(event))
    ['char', 'delta', 'focus', 'height', 'keycode', 'keysym', 'keysym_num', 'num', 'send_event', 
     'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']
    """
    print(event.serial, end='/')
    print(event.num, end='/')
    print(event.x, end='/')
    print(event.y, end='/')
    print(event.x_root, end='/')
    print(event.y_root, end='/')
    print(event.type)

def show_keyboard_event(event):
    print('Keyboard')
    """
    print(dir(event))
    ['char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num', 
     'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']

    """
    print(event.char, end='/')
    print(event.type, end='/')
    print(event.widget)

def show_window_event(event):
    print('Window event')

    """
    print(dir(event))
    ['char', 'delta', 'height', 'keycode', 'keysym', 'keysym_num', 'num', 'send_event', 
     'serial', 'state', 'time', 'type', 'widget', 'width', 'x', 'x_root', 'y', 'y_root']
    """
    print(event.height, ' /', event.width)


###################################################
# Create the widgets
root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

button = tk.Button(root, text='Mouse Event Generator')
button.grid(row=0, column=0, sticky='nsew')

my_text = tk.StringVar(value='Keyboard event generator')
entry = tk.Entry(root, width=50, textvar=my_text)
entry.grid(row=1, column=0, sticky='nsew')

###################################################
# Bind the mouse events
button.bind("<Button-1>", show_mouse_events)
button.bind("<Button-2>", show_mouse_events)
button.bind("<Button-3>", show_mouse_events)
button.bind("<Button-4>", show_mouse_events)
button.bind("<Button-5>", show_mouse_events)
button.bind("<B1-Motion>", show_mouse_events)
button.bind("<ButtonRelease>", show_mouse_events)
button.bind("<Double-Button-1>", show_mouse_events)
button.bind("<Enter>", show_mouse_events)
button.bind("<Leave>", show_mouse_events)

###################################################
# Bind the keyboard events
entry.bind("<Key>", show_keyboard_event)
entry.bind("<FocusIn>", show_keyboard_event)
entry.bind("<FocusOut>", show_keyboard_event)
entry.bind("<Return>", show_keyboard_event)
entry.bind("<BackSpace>", show_keyboard_event)

###################################################
# Bind the window event
root.bind("<Configure>", show_window_event)

"""
Bind to a specific class:

First create a local class, inheriting from the original class:

class MyButton(tk.Button):
    def __init__(self, master, **kw):
        apply(tk.Button.__init__, (self, master), kw)
        self.bind(<event>, callback)

"""

if __name__ == '__main__':
    root.mainloop()

'''
Basic Widget Methods

The following methods are provided by all widgets (including the root window).

The root window and other Toplevel windows provide additional methods. 
See the Window Methods section for more information.
    mainloop()
    w.mainloop()
    w.quit()
    w.wait_variable(var)
    w.wait_visibility(window)
    w.wait_window(window)
    w.update()
    w.update_idletasks()

Event callbacks

w.bind(event, callback)
w.unbind(event)
w.bind_class(event, callback)
w.bindtags()
w.bindtags(tags)

Alarm handlers and other non-event callbacks

id = w.after(time, callback)
id = w.after_idle(callback)
w.after_cancel(id)

Window management

w.lift()
w.lower()

Window-related information

w.winfo_width(), w.winfo_height()
w.winfo_reqwidth(), w.winfo_reqheight()
w.winfo_id()

The option database

w.option_add(pattern, value)
w.option_get(name, class)

Reference

Widget (class) [#]

    Widget implementation class. This class is used as a mixin by all widget classes.

after(delay_ms, callback=None, *args) [#]

    Registers an alarm callback that is called after a given time.
    This method registers a callback function that will be called after a given number of milliseconds. 
    Tkinter only guarantees that the callback will not be called earlier than that; if the system is busy, 
    the actual delay may be much longer.

    The callback is only called once for each call to this method. To keep calling the callback, 
    you need to reregister the callback inside itself:

    class App:
        def __init__(self, master):
            self.master = master
            self.poll() # start polling

        def poll(self):
            ... do something ...
            self.master.after(100, self.poll)

    after_cancel to cancel the callback.

    You can also omit the callback. If you do, this method simply waits for the given number of milliseconds, without serving any events (same as time.sleep(delay_ms*0.001)).

    delay_ms
        Delay, in milliseconds.
    callback
        The callback. This can be any callable object.
    *args
        Optional arguments that are passed to the callback.
    Returns:
        An alarm identifier.


after_cancel(id) [#]
    Cancels an alarm callback.
    id
        Alarm identifier.


after_idle(callback, *args) [#]
    Registers a callback that is called when the system is idle. 
    The callback will be called there are no more events to process in the mainloop. 
    The callback is only called once for each call to after_idle.

    callback
        The callback. This can be any callable object.
    *args
        Optional arguments that are passed to the callback.
    Returns:
        An alarm identifier.


bbox(column=None, row=None, col2=None, row2=None) [#]
    The bbox method.
    column
    row
    col2
    row2


bell(displayof=0) [#]
    Generate a system-dependent sound (typically a short beep).
    displayof

bind(sequence=None, func=None, add=None) [#]
    Adds an event binding to this widget. Usually, the new binding replaces any existing binding for the same 
    event sequence. By passing in �+� as the third argument, the new callback is added to the existing binding.

bind_all(sequence=None, func=None, add=None) [#]
    Adds an event binding to the application level. Usually, the new binding replaces any existing binding for the 
    same event sequence. By passing in �+� as the third argument, the new function is added to the existing binding.

bind_class(className, sequence=None, func=None, add=None) [#]
    Adds an event binding to the given widget class. Usually, the new binding replaces any existing binding for the 
    same event sequence. By passing in �+� as the third argument, the new function is added to the existing binding.

bindtags(tagList=None) [#]
    Sets or gets the binding search order for this widget.

    If called without an argument, this method returns a tuple containing the binding search order used for this widget.
    By default, this tuple contains the widget�s name (str(self)), the widget class (e.g. Button), 
    the root window�s name, and finally the special name all which refers to the application level. 

cget(key) [#]
    Returns the current value for an option.

    Note that option values are always returned as strings (also if you gave a nonstring value when you configured the widget). Use int and float where appropriate. 

clipboard_append(string, **options) [#]
    Adds text to the clipboard.
    string
        The text to add.
    **options


clipboard_clear(**options) [#]
    Clears the clipboard.
    **options

colormodel(value=None) [#]
    The colormodel method.
    value

columnconfigure(index, cnf={}, **kw) [#]
    The columnconfigure method.
    index
    cnf
    **kw

config(cnf=None, **kw) [#]
    Modifies one or more widget options.
    If called without an argument, this method returns a dictionary containing the current settings for all widget options. For each option key in the dictionary, the value is either a five-tuple (option, option database key, option database class, default value, current value), or a two-tuple (option alias, option). The latter case is used for aliases like bg (background) and bd (borderwidth).
    Note that the value fields aren�t correctly formatted for some option types. See the description of the keys method for more information, and a workaround. 

configure(cnf=None, **kw) [#]
    Same as config. 

deletecommand(name) [#]
    The deletecommand method.
    name

destroy() [#]
    Destroys the widget. The widget is removed from the screen, and all resources associated with the widget are released.

event_add(virtual, *sequences) [#]
    The event_add method.
    virtual
    *sequences

    some_widget.event_add('<<commit>>', '<F-9>')
    some_widget.bind('<<commit>>', callback)

event_delete(virtual, *sequences) [#]
    The event_delete method.
    virtual
    *sequences

event_generate(sequence, **kw) [#]
    The event_generate method.
    sequence
    **kw

event_info(virtual=None) [#]
    The event_info method.
    virtual

focus() [#]
    The focus method.

focus_displayof() [#]
    The focus_displayof method.

focus_force() [#]
    The focus_force method.

focus_get() [#]
    The focus_get method.

focus_lastfor() [#]
    The focus_lastfor method.

focus_set() [#]
    Moves the keyboard focus to this widget. This means that all keyboard events sent to the application will be routed to this widget.

getboolean(s) [#]
    (Internal) Converts a Tk string to a boolean (flag) value.

getvar(name=�PY_VAR�) [#]
    The getvar method.
    name

grab_current() [#]
    The grab_current method.

grab_release() [#]
    Releases the event grab.

grab_set() [#]
    Routes all events for this application to this widget.

grab_set_global() [#]
    Routes all events for the entire screen to this widget.
    This should only be used in very special circumstances, since it blocks all other applications running on the same screen. And that probably includes your development environment, so you better make sure your application won�t crash or lock up until it has properly released the grab. 

grab_status() [#]
    The grab_status method.

image_names() [#]
    The image_names method.

image_types() [#]
    The image_types method.

keys() [#]
    Returns a tuple containing the options available for this widget. You can use cget to get the corresponding value for each option.
    Note that the tuple currently include option aliases (like bd, bg, and fg). To avoid this, you can use config instead. On the other hand, config doesn�t return valid option values for some option types (such as font names), so the best way is to use a combination of config and cget:
    for item in w.config():
        if len(item) == 5:
            option = item[0]
            value = w.cget(option)
            print option, value

lift(aboveThis=None) [#]
    Moves the widget to the top of the window stack. If the widget is a child window, it is moved to the top of it�s toplevel window. If it is a toplevel window (the root or a Toplevel window), it is moved in front of all other windows on the display. If an argument is given, the widget (or window) is moved so it�s just above the given widget (window).

lower(belowThis=None) [#]
    Moves the window to the bottom of the window stack. Same as lift, but moves the widget to the bottom of the stack (or places it just under the belowThis widget). 

mainloop(n=0) [#]
    Enters Tkinter�s main event loop. To leave the event loop, use the quit method. Event loops can be nested; it�s ok to call mainloop from within an event handler. 

nametowidget(name) [#]
    Gets the widget object corresponding to a widget name.
    name
        The widget name.
    Returns:
        The corresponding widget object, if known.
    Raises KeyError:
        If the widget could not be found.

option_add(pattern, value, priority=None) [#]
    The option_add method.
    pattern
    value
    priority

option_clear() [#]
    The option_clear method.

option_get(name, className) [#]
    The option_get method.
    name
    className

option_readfile(fileName, priority=None) [#]
    The option_readfile method.
    fileName
    priority

pack_propagate(flag=[�_noarg_�]) [#]
    The pack_propagate method.
    flag

pack_slaves() [#]
    The pack_slaves method.

place_slaves() [#]
    The place_slaves method.

propagate(flag=[�_noarg_�]) [#]
    The propagate method.
    flag

quit() [#]
    The quit method.

register(func, subst=None, needcleanup=1) [#]
    Registers a Tcl to Python callback. Returns the name of a Tcl wrapper procedure. When that procedure is called from a Tcl program, it will call the corresponding Python function with the arguments given to the Tcl procedure. Values returned from the Python callback are converted to strings, and returned to the Tcl program.

rowconfigure(index, cnf={}, **kw) [#]
    The rowconfigure method.
    index
    cnf
    **kw

selection_clear(**kw) [#]
    The selection_clear method.
    **kw

selection_get(**kw) [#]
    The selection_get method.
    **kw

selection_handle(command, **kw) [#]
    The selection_handle method.
    command
    **kw

selection_own(**kw) [#]
    The selection_own method.
    **kw

selection_own_get(**kw) [#]
    The selection_own_get method.
    **kw

send(interp, cmd, *args) [#]
    The send method.
    interp
    cmd
    *args

setvar(name=�PY_VAR�, value=�1�) [#]
    The setvar method.
    name
    value

size() [#]
    The size method.

slaves() [#]
    The slaves method.

tk_bisque() [#]
    The tk_bisque method.

tk_focusFollowsMouse() [#]
    The tk_focusFollowsMouse method.

tk_focusNext() [#]
    Returns the next widget (following self) that should have focus. This is used by the default bindings for the Tab key. 

tk_focusPrev() [#]
    Returns the previous widget (preceding self) that should have focus. This is used by the default bindings for the Shift-Tab key. 

tk_menuBar(*args) [#]
    The tk_menuBar method.
    *args

tk_setPalette(*args, **kw) [#]
    The tk_setPalette method.
    *args
    **kw

tk_strictMotif(boolean=None) [#]
    The tk_strictMotif method.
    boolean

tkraise(aboveThis=None) [#]
    The tkraise method.
    aboveThis


unbind(sequence, funcid=None) [#]
    Removes any bindings for the given event sequence, for this widget.

unbind_all(sequence) [#]
    The unbind_all method.
    sequence

unbind_class(className, sequence) [#]
    The unbind_class method.
    className
    sequence

update() [#]
    Processes all pending events, calls event callbacks, completes any pending geometry management, redraws widgets as necessary, and calls all pending idle tasks. This method should be used with care, since it may lead to really nasty race conditions if called from the wrong place (from within an event callback, for example, or from a function that can in any way be called from an event callback, etc.). When in doubt, use update_idletasks instead. 

update_idletasks() [#]
    Calls all pending idle tasks, without processing any other events. This can be used to carry out geometry management and redraw widgets if necessary, without calling any callbacks.

wait_variable(name) [#]
    Waits for the given Tkinter variable to change. This method enters a local event loop, so other parts of the application will still be responsive. The local event loop is terminated when the variable is updated (setting it to it�s current value also counts).

wait_visibility(window=None) [#]
    Wait for the given widget to become visible. This is typically used to wait until a new toplevel window appears on the screen. Like wait_variable, this method enters a local event loop, so other parts of the application will still work as usual. 

wait_window(window=None) [#]
    Waits for the given widget to be destroyed. This is typically used to wait until a destroyed window disappears from the screen. Like wait_variable and wait_visibility, this method enters a local event loop, so other parts of the application will still work as usual. 

waitvar(name=�PY_VAR�) [#]
    The waitvar method.
    name

winfo_atom(name, displayof=0) [#]
    Maps the given string to a unique integer. Every time you call this method with the same string, the same integer will be returned.

winfo_atomname(id, displayof=0) [#]
    Returns the string corresponding to the given integer (obtained by a call to winfo_atom). If the integer isn�t in use, Tkinter raises a TclError exception. Note that Tkinter predefines a bunch of integers (typically 1-80 or so). If you�re curious, you can use this method to find out what they are used for. 

winfo_cells() [#]
    Returns the number of �cells� in the color map for self. This is typically a value between 2 and 256 (also for true color displays, for some odd reason).

winfo_children() [#]
    Returns a list containing widget instances for all children of this widget. The windows are returned in stacking order from bottom to top. If the order doesn�t matter, you can get the same information from the children widget attribute (it�s a dictionary mapping Tk widget names to widget instances, so widget.children.values() gives you a list of instances).

winfo_class() [#]
    Returns the Tkinter widget class name for this widget. If the widget is a Tkinter base widget, widget.winfo_class() is the same as widget.__class__.__name__.

winfo_colormapfull() [#]
    Returns true if the color map for this widget is full.

winfo_containing(rootX, rootY, displayof=0) [#]
    Returns the widget at the given position, or None if there is no such window, or it isn�t owned by this application. The coordinates are given relative to the screen�s upper left corner.
    rootX
    rootY
    displayof

winfo_depth() [#]
    Returns the bit depth used to display this widget. This is typically 8 for a 256-color display device, 15 or 16 for a �hicolor� display, and 24 or 32 for a true color display.

winfo_exists() [#]
    Returns true if there is Tk window corresponding to this widget. Unless you�ve done something really strange, this method should always return true.

winfo_fpixels(distance) [#]
    Converts the given distance (in any form accepted by Tkinter) to the corresponding number of pixels.
    distance
        The screen distance.
    Returns:
        The corresponding number of screen pixels, as a floating point number.

winfo_geometry() [#]
    Returns a string describing the widget�s �geometry�. The string has the following format:
    "%dx%d%+d%+d" % (width, height, xoffset, yoffset)

winfo_height() [#]
    Get the height of this widget, in pixels. Note that if the window isn�t managed by a geometry manager, this method returns 1. To you get the real value, you may have to call update_idletasks first. You can also use winfo_reqheight to get the widget�s requested height (that is, the �natural� size as defined by the widget itself based on it�s contents).
    Returns:
        The widget�s current height, in pixels.

winfo_id() [#]
    Get a system-specific window identifier for this widget. For Unix, this is the X window identifier. For Windows, this is the HWND cast to a long integer.
    Returns:
        The window identifier.

winfo_interps(displayof=0) [#]
    The winfo_interps method.
    displayof

winfo_ismapped() [#]
    Check if the window has been created. This method checks if Tkinter has created a window corresponding to the widget in the underlying window system (an X window, a Windows HWND, etc).
    Returns:
        A true value if a window has been created.

winfo_manager() [#]
    Return the name of the geometry manager used to keep manage this widget (typically one of grid, pack, place, canvas, or text).

winfo_name() [#]
    Get the Tk widget name. This is the same as the last part of the full widget name (which you can get via str(widget)).
    Returns:
        The widget name.

winfo_parent() [#]
    Get the full widget name of this widget�s parent. This method returns an empty string if the widget doesn�t have a parent (if it�s a root window or a toplevel, that is).
    To get the widget instance instead, you can simply use the master attribute instead of calling this method (the master attribute is None for the root window). Or if you insist, use nametowidget to map the full widget name to a widget instance.
    Returns:
        The widget name, as a string.

winfo_pathname(id, displayof=0) [#]
    Get the full window name for the window having the given identity (see winfo_id for details). If the window doesn�t exist, or it isn�t owned by this application, Tkinter raises a TclError exception.
    To convert the full name to a widget instance, use nametowidget.
    id
        The window identifier.
    displayof

winfo_pixels(distance) [#]
    Convert the given distance (in any form accepted by Tkinter) to the corresponding number of pixels.
    distance
        The screen distance.
    Returns:
        The corresponding number of screen pixels, as an integer.

winfo_pointerx() [#]
    The winfo_pointerx method.

winfo_pointerxy() [#]
    The winfo_pointerxy method.

winfo_pointery() [#]
    The winfo_pointery method.

winfo_reqheight() [#]
    Returns the �natural� height for this widget. The natural size is the minimal size needed to display the widget�s contents, including padding, borders, etc. This size is calculated by the widget itself, based on the given options. The actual widget size is then determined by the widget�s geometry manager, based on this value, the size of the widget�s master, and the options given to the geometry manager.

winfo_reqwidth() [#]
    Returns the �natural� width for this widget. The natural size is the minimal size needed to display the widget�s contents, including padding, borders, etc. This size is calculated by the widget itself, based on the given options. The actual widget size is then determined by the widget�s geometry manager, based on this value, the size of the widget�s master, and the options given to the geometry manager.

winfo_rgb(color) [#]
    Convert a color string (in any form accepted by Tkinter) to an RGB tuple.
    color
        A colour string. This can be a colour name, a string containing an rgb specifier (�#rrggbb�), or any other syntax supported by Tkinter.
    Returns:
        A 3-tuple containing the corresponding red, green, and blue components. Note that the tuple contains 16-bit values (0..65535).

winfo_rootx() [#]
    Get the pixel coordinate for the widget�s left edge, relative to the screen�s upper left corner.
    Returns:
        The root coordinate.

winfo_rooty() [#]
    Get the pixel coordinates for the widget�s upper edge, relative to the screen�s upper left corner.
    Returns:
        The root coordinate.

winfo_screen() [#]
    Get the X window screen name for the current window. The screen name is a string having the format �:display.screen�, where display and screen are decimal numbers.
    On Windows and Macintosh, this is always �:0.0�.
    Returns:
        The screen name.

winfo_screencells() [#]
    Get the number of �color cells� in the default color map for this widget�s screen.
    Returns:
        The number of color cells.

winfo_screendepth() [#]
    Get the default bit depth for this widget�s screen.
    Returns:
        The bit depth.

winfo_screenheight() [#]
    Get the height of this widget�s screen, in pixels.
    Returns:
        The height, in pixels.

winfo_screenmmheight() [#]
    Get the height of this widget�s screen, in millimetres. This may not be accurate on all platforms.
    Returns:
        The height, in millimetres.

winfo_screenmmwidth() [#]
    Get the width of this widget�s screen, in millimetres. This may not be accurate on all platforms.
    Returns:
        The width, in millimetres.

winfo_screenvisual() [#]
    Get the �visual� type used for this widget. This is typically �pseudocolor� (for 256-color displays) or �truecolor� (for 16- or 24-bit displays).
    Returns:
        A string containing the visual type. This is one of �pseudocolor�, �truecolor�, �directcolor�, �staticcolor�, �grayscale�, or �staticgray�.

winfo_screenwidth() [#]
    Get the width of this widget�s screen, in pixels.
    Returns:
        The width, in pixels.

winfo_server() [#]
    The winfo_server method.

winfo_toplevel() [#]
    Get the toplevel window (or root) window for this widget, as a widget instance.
    Returns:
        The toplevel parent widget. This is either a Tk instance, or a Toplevel instance.

winfo_viewable() [#]
    The winfo_viewable method.

winfo_visual() [#]
    Same as winfo_screenvisual.

winfo_visualid() [#]
    The winfo_visualid method.

winfo_visualsavailable(includeids=0) [#]
    The winfo_visualsavailable method.
    includeids

winfo_vrootheight() [#]
    The winfo_vrootheight method.

winfo_vrootwidth() [#]
    The winfo_vrootwidth method.

winfo_vrootx() [#]
    The winfo_vrootx method.

winfo_vrooty() [#]
    The winfo_vrooty method.

winfo_width() [#]
    Get the width of this widget, in pixels. Note that if the window isn�t managed by a geometry manager, this method returns 1. To you get the real value, you may have to call update_idletasks first. You can also use winfo_reqwidth to get the widget�s requested width (that is, the �natural� size as defined by the widget itself based on it�s contents).
    Returns:
        The widget�s current width, in pixels.

winfo_x() [#]
    Returns the pixel coordinates for the widgets�s left corner, relative to its parent�s left corner.

winfo_y() [#]
    Returns the pixel coordinates for the widgets�s upper corner, relative to its parent�s upper corner.

'''
