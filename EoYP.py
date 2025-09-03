#imports the tkinter library
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

#constants 
MONS_MAX = 10
SCORE_MAXIMUM = 25
SCORE_MINIMUM = 1
NAME_MAX = 16
FONT_TYPE = "Roboto Mono"
GRAY_COLOUR = "#737373"
DARK_RED = "#330a0a"
LIGHT_TEAL = "#11676a"
RED = "#7a0000"
DARK_TEAL = "#00343d"
CARD_WIDTH = 11
CARD_HEIGHT = 8
BOTTOM_ROW_BUTTONS_YAXIS = 430
TOP_ROW_BUTTONS_YAXIS = 260
STATS_LABELS_XAXIS = 15
STATS_XAXIS = 18
STATS_FONT_SIZE = 19


def id_1():
    global card_id
    card_id = 1
    

def id_2():
    global card_id
    card_id = 2

def id_3():
    global card_id
    card_id = 3

def id_4():
    global card_id
    card_id = 4

def id_5():
    global card_id
    card_id = 5

def id_6():
    global card_id
    card_id = 6

def id_7():
    global card_id
    card_id = 7

def id_8():
    global card_id
    card_id = 8

def id_9():
    global card_id
    card_id = 9

def id_10():
    global card_id
    card_id = 10

def output():
    global strength
    global speed
    global stealth
    global cunning
    global total

    if card_id == 1:
        strength = monsters["monster1"]["strength"]
        speed = monsters["monster1"] ["speed"]
        stealth = monsters["monster1"] ["stealth"]
        cunning = monsters["monster1"] ["cunning"]
        total = monsters["monster1"] ["total_score"]

    label_strength = Label(frame_card_preview, text="Srength:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_strength.place(y = 390, x = STATS_LABELS_XAXIS, width= 105)

    label_strength_stat = Label(frame_card_preview, text=strength, fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_strength_stat.place(y = 390, x = STATS_XAXIS, width= 105)

    label_speed = Label(frame_card_preview, text="Speed:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_speed.place(y = 430, x = STATS_LABELS_XAXIS, width= 105)

    label_speed_stat = Label(frame_card_preview, text=speed, fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_speed_stat.place(y = 430, x = STATS_XAXIS, width= 105)

    label_Stealth = Label(frame_card_preview, text="Stealth:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_Stealth.place(y = 470, x = STATS_LABELS_XAXIS, width= 105)

    label_Stealth_stat = Label(frame_card_preview, text=stealth, fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_Stealth_stat.place(y = 470, x = STATS_XAXIS, width= 105)

    label_cunning = Label(frame_card_preview, text="Cunning:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_cunning.place(y = 510, x = STATS_LABELS_XAXIS, width= 105)

    label_cunning_stat = Label(frame_card_preview, text=total, fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_cunning_stat.place(y = 510, x = STATS_XAXIS, width= 105)

    label_total = Label(frame_card_preview, text="Total", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_total.place(y = 550, x = STATS_LABELS_XAXIS, width= 105)

    label_total_stat = Label(frame_card_preview, text="Total", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
    label_total_stat.place(y = 550, x = STATS_XAXIS, width= 105)

    button_cancel = Button(frame_card_preview, text="Cancel", fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL)
    button_cancel.place(y = 600, x = 50)

    button_confirm = Button(frame_card_preview, text="Confirm", fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL)
    button_confirm.place(y = 600, x = 320)

    frame_mainpage_bg.pack_forget()
    root.geometry("450x650")

    frame_card_preview.pack(fill=BOTH, expand = TRUE)


monsters= {
    "monster1" : {
        "monster_name": "Vexscream", 
        "strength": 1, 
        "speed": 6, 
        "stealth": 21, 
        "cunning": 19,
        "total_score": 47
    },
    "monster2" : {
        "monster_name": "Dawnmirage", 
        "strength": 5, 
        "speed": 15, 
        "stealth": 18, 
        "cunning": 22,
        "total_score": 60
    },
       "monster3" : {
        "monster_name": "Blazegolem", 
        "strength": 15, 
        "speed": 20, 
        "stealth": 23, 
        "cunning": 6,
        "total_score": 64
    }, 
        "monster4" : {
        "monster_name": "Moldvine", 
        "strength": 21, 
        "speed": 18, 
        "stealth": 14, 
        "cunning": 5,
        "total_score": 58
    }, 
        "monster5" : {
        "monster_name": "Vertexwing", 
        "strength": 19, 
        "speed": 13, 
        "stealth": 18, 
        "cunning": 2,
        "total_score": 53
    }, 
        "monster6" : {
        "monster_name": "Froststep", 
        "strength": 14, 
        "speed": 14, 
        "stealth": 17, 
        "cunning": 4,
        "total_score": 49
    }, 
        "monster7" : {
        "monster_name": "Wispghoul", 
        "strength": 17, 
        "speed": 19, 
        "stealth": 3, 
        "cunning": 2,
        "total_score": 41
    }
}

card_id = 0

root = Tk()
root.title ("Monster Catalogue")
root.geometry("840x570")

frame_mainpage_bg = Frame(root, bg=DARK_TEAL)
frame_mainpage_bg.pack(fill=BOTH, expand=TRUE)

frame_graytbox = Frame(frame_mainpage_bg, bg = GRAY_COLOUR, width = 775, height = 220)
frame_graytbox.place(y = 10, x = 35)

label_maintitle = Label(frame_graytbox, text = "Monster Catalogue", fg = DARK_RED, font = (FONT_TYPE, 35), bg=GRAY_COLOUR)
label_maintitle.place(y = 5, x = 170)

button_main_exit = Button(frame_graytbox, text="Exit", fg = DARK_RED, font = (FONT_TYPE, 16), bg=RED, command= exit)
button_main_exit.place(y = 4, x = 715)

button_add= Button(frame_graytbox, text="Add", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL)
button_add.place(y = 85, x = 120)

button_edit = Button(frame_graytbox, text="Edit", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL)
button_edit.place(y = 85, x = 270)

button_sort = Button(frame_graytbox, text="Sort", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL)
button_sort.place(y = 85, x = 420)

button_print = Button(frame_graytbox, text="Print", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command= output)
button_print.place(y = 85, x = 570)

entry_searchbar = Entry(frame_graytbox, text="search", fg = DARK_RED, font = (FONT_TYPE, 10), bg=GRAY_COLOUR)
entry_searchbar.place(y = 170, x = 40, width = 580, height = 30)

button_search = Button(frame_graytbox, text="Search", fg = DARK_RED, font = (FONT_TYPE, 13), bg=LIGHT_TEAL)
button_search.place(y = 167, x = 640)

button_cardslot_1 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_1)
button_cardslot_1.place(y = TOP_ROW_BUTTONS_YAXIS, x = 100)

button_cardslot_2 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_2)
button_cardslot_2.place(y = TOP_ROW_BUTTONS_YAXIS, x = 240)

button_cardslot_3 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_3)
button_cardslot_3.place(y = TOP_ROW_BUTTONS_YAXIS, x = 380)

button_cardslot_4 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_4)
button_cardslot_4.place(y = TOP_ROW_BUTTONS_YAXIS, x = 520)

button_cardslot_5 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_5)
button_cardslot_5.place(y = TOP_ROW_BUTTONS_YAXIS, x = 660)

button_cardslot_6 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_6)
button_cardslot_6.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 100)

button_cardslot_7 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_7)
button_cardslot_7.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 240)

button_cardslot_8 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_8)
button_cardslot_8.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 380)

button_cardslot_9 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_9)
button_cardslot_9.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 520)

button_cardslot_10 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_10)
button_cardslot_10.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 660)

frame_card_preview = Frame(root, bg=DARK_TEAL)
image_monster = Image.open("MANGO_LOCO2.png")
image_monster = image_monster.resize((300,360), Image.LANCZOS)
monster_image = ImageTk.PhotoImage(image_monster)
label_preview_image = Label(frame_card_preview, image=monster_image)
label_preview_image.place(y = 15, x = 15)

button_card_exit = Button(frame_card_preview, text="Exit", fg = DARK_RED, font = (FONT_TYPE, 16), bg=RED, command= exit)
button_card_exit.place(y = 12, x = 380)



root.mainloop()