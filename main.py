import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ctypes
from read_files import *
from utils.window import *

window = tk.Tk()
window.geometry('800x600')
window.title('My Spotify Stats')

window.iconbitmap('app_icon.ico')

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.iconbitmap('app_icon.ico')

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        data = read_file(file_path)
        load_stats(data)

center_window(window)



main_menu_frame = ttk.Frame(window, width=window.winfo_width(), height=window.winfo_height())
main_menu_frame.pack()

stats_frame = ttk.Frame(window, width=window.winfo_width(), height=window.winfo_height())
stats_frame

image_label = ttk.Label(main_menu_frame, text='Image label')
image_label.place(anchor='center', relx=0.15, rely=0.25)
trebel_clef_img = tk.PhotoImage(file='treble_clef.png')
image_label['image'] = trebel_clef_img

title = ttk.Label(main_menu_frame, text='My stats', font='Calibri 72 bold')
title.place(relx=0.5, rely=0.2, anchor='center')

stats_button = tk.Button(main_menu_frame, text='My Stats', relief=tk.GROOVE, command=stats_frame.tkraise())
stats_button.place(anchor='center', bordermode='outside', relx=0.5, rely=0.6, relwidth=0.3, relheight=0.075)

load_button = tk.Button(main_menu_frame, text='Load File', relief=tk.GROOVE, command=open_file)
load_button.place(anchor='center', bordermode='outside', relx=0.5, rely=0.7, relwidth=0.3, relheight=0.075)

exit_button = tk.Button(main_menu_frame, text='Exit', relief=tk.GROOVE, command= lambda: print('exit_button_pressed'))
exit_button.place(anchor='center', bordermode='outside', relx=0.5, rely=0.8, relwidth=0.3, relheight=0.075)





window.mainloop()