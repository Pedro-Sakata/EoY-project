#imports the tkinter library
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

#constants 
mons_max = 10
score_maximum = 25
score_minimum = 1
name_max = 16
font_type = "Roboto Mono"

root = Tk()
root.title ("Monster Catalogue")
root.geometry("840x470")

frame_mainpage_bg = Frame(root, bg="#00343d")
frame_mainpage_bg.pack(fill=BOTH, expand=TRUE)

frame_graytbox = Frame(frame_mainpage_bg, bg="#737373", width=775, height=210)
frame_graytbox.place(y=10, x=35)

label_maintitle = Label(frame_graytbox, text="Monster Catalogue", fg="#330a0a", font = (font_type, 40), bg="#737373")
label_maintitle.place(y=5, x=160)

button_main_exitbutton = Button(frame_graytbox, text="Exit", fg="#330a0a", font = (font_type, 16), bg="#7a0000")
button_main_exitbutton.place(y=4, x=715)

button_main_addbutton = Button(frame_graytbox, text="Add", fg="#330a0a", font = (font_type, 20), bg="#737373")
button_main_addbutton.place(y=60, x=500)

root.mainloop()