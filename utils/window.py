import tkinter

def center_window(window:tkinter.Tk):

    window.update()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_width()
    window_height = window.winfo_height()

    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    window.geometry(f'+{x_pos}+{y_pos}')