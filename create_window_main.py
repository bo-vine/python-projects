"""
Creates a window with the layout below:

LAYOUT
____________________________________
|  ______________________________  |
| |                              | |
| |        Generated Pass        | |
| |______________________________| |
|  ___________         __________  |
| | Copy Text |       | Generate | |
|  ¯¯¯¯¯¯¯¯¯¯¯         ¯¯¯¯¯¯¯¯¯¯  |
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
"""

import tkinter as tk

class GUIWindow:
    window = tk.Tk()

    text_frame = tk.Frame()
    buttons_frame = tk.Frame()

    Text = tk.Text(master=text_frame)
    copy_text_button = tk.Button(master=buttons_frame)
    generate_password_button = tk.Button(master=buttons_frame)

    window.mainloop()

def copy_command():
    pass

def generate_command():
    pass