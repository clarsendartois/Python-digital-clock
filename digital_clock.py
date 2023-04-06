import tkinter as tk
import customtkinter as ctk
from time import strftime


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


font_style = ("ds-digital", 180)
bg_fg_color = "#000000"
clock_color = "#00FF00"


class DigitalClock:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x150")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Digital Clock")

        self.frame = self.create_frame()
        self.label = self.create_label()
        self.time = self.create_time()

    def create_frame(self):
        frame = ctk.CTkFrame(self.window, width=580,
                             height=130, corner_radius=10, fg_color=bg_fg_color)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return frame

    def create_label(self):
        global clock
        clock = tk.Label(self.frame, font=font_style,
                         background=bg_fg_color, foreground=clock_color)
        clock.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_time(self):
        string = strftime("%H:%M:%S %p")
        clock.configure(text=string)
        clock.after(1000, self.create_time)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    digital_clock = DigitalClock()
    digital_clock.run()
