"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # TODOne: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # TODOne: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding=15)
    frame1.grid()
    # ------------------------------------------------------------------
    # TODOne: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    i_did_it_button = ttk.Button(frame1, text='I Did It')
    i_did_it_button.grid()
    # ------------------------------------------------------------------
    # TODOne: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    i_did_it_button['command'] = lambda: do_things()
    # ------------------------------------------------------------------
    # TODOne: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry_box1 = ttk.Entry(frame1)
    entry_box1.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_contents(entry_box1))
    print_entry_button.grid()
    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry_box2 = ttk.Entry(frame1)
    entry_box2.grid()

    new_entry_button = ttk.Button(frame1, text='new entry')
    new_entry_button['command'] = (lambda: print_int(entry_box1, entry_box2))
    new_entry_button.grid()
    # --------------------------------------------------------
    # ----------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    window.mainloop()


def do_things():
    print('hello')


def print_contents(entry_box):
    contents_of_entry_box = entry_box.get()
    if contents_of_entry_box == 'ok':
        print('hello')
    else:
        print('goodbye')


def print_int(entry_box1, entry_box):
    a = entry_box1.get()
    contents_of_entry_box = entry_box.get()
    if a == int:
        for k in range(contents_of_entry_box):
            print(a)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
