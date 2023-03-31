import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Clock")


def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(window, font=("ds-digital", 80),
                 background="black", foreground="cyan")
label.pack(anchor=tk.CENTER)

time()
tk.mainloop()
