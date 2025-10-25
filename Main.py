from customtkinter import *
from random import *

window = CTk()

window.geometry("400x300")
window.title("GP")
window.configure(fg_color="black")

def Generate_pass():
    pass

pass_en = CTkEntry(window, width=200)
pass_en.grid(row=0, column=0, padx=20, pady=20)

button_gen = CTkButton(window, text="Generated", command=Generate_pass)
button_gen.grid(row=0, column=1, pady=20)

frame_opt = CTkFrame(window, width=200)
frame_opt.grid(row=1, column=0)

lowercase_btn = CTkCheckBox(frame_opt, text="Малі літери", width=200)
lowercase_btn.pack(pady=5)

uppercase_btn = CTkCheckBox(frame_opt, text="Великі літери", width=200)
uppercase_btn.pack(pady=5)

specchars_btn = CTkCheckBox(frame_opt, text="Спец. Символи", width=200)
specchars_btn.pack(pady=5)

number_btn = CTkCheckBox(frame_opt, text="числа", width=200)
number_btn.pack(pady=5)

frame_sld = CTkFrame(window, )
frame_sld.grid(row=1, column=1)

slider = CTkSlider(frame_sld, from_=4, to=32, height=140, orientation="vertical")
slider.pack(side="right",pady=5)

pass_lb = CTkLabel(frame_sld, text=4, width=80)
pass_lb.pack(side="left", padx=20)

window.mainloop()