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
CARD_WIDTH = 100
CARD_HEIGHT = 130
BOTTOM_ROW_BUTTONS_YAXIS = 420
TOP_ROW_BUTTONS_YAXIS = 260
STATS_LABELS_XAXIS = 15
STATS_XAXIS = 140
STATS_FONT_SIZE = 19
SLIDER_XAXIS = 147
SLIDER_WIDTH = 235
SLIDER_HEIHGT = 45
TEAL_BAR_WIDTH = 390
TEAL_BAR_HEIHGT = 60
IMAGE_RESIZE_WIDTH = 130
IMAGE_RESIZE_HEIGHT = 125

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

def return_function():
    frame_card_preview.pack_forget()
    frame_mainpage_bg.pack(fill = BOTH, expand= TRUE)
    root.geometry("840x570")

def output():
    global strength
    global speed
    global stealth
    global cunning
    global total
    global label_strength_stat
    global label_speed_stat
    global label_sneak_stat
    global label_cunning_stat
    global label_total_stat

    if card_id == 1:
        strength = monsters["monster1"]["strength"]
        speed = monsters["monster1"] ["speed"]
        stealth = monsters["monster1"] ["stealth"]
        cunning = monsters["monster1"] ["cunning"]
        total = monsters["monster1"] ["total_score"]
        monster_image = monsters["monster1"]["image_id"]
    if card_id == 2:
        strength = monsters["monster2"]["strength"]
        speed = monsters["monster2"] ["speed"]
        stealth = monsters["monster2"] ["stealth"]
        cunning = monsters["monster2"] ["cunning"]
        total = monsters["monster2"] ["total_score"]
        monster_image = monsters["monster2"]["image_id"]   
    if card_id == 3:
        strength = monsters["monster3"]["strength"]
        speed = monsters["monster3"] ["speed"]
        stealth = monsters["monster3"] ["stealth"]
        cunning = monsters["monster3"] ["cunning"]
        total = monsters["monster3"] ["total_score"] 
        monster_image = monsters["monster3"]["image_id"]
    if card_id == 4:
        strength = monsters["monster4"]["strength"]
        speed = monsters["monster4"] ["speed"]
        stealth = monsters["monster4"] ["stealth"]
        cunning = monsters["monster4"] ["cunning"]
        total = monsters["monster4"] ["total_score"]    
        monster_image = monsters["monster4"]["image_id"]     
    if card_id == 5:
        strength = monsters["monster5"]["strength"]
        speed = monsters["monster5"] ["speed"]
        stealth = monsters["monster5"] ["stealth"]
        cunning = monsters["monster5"] ["cunning"]
        total = monsters["monster5"] ["total_score"]
        monster_image = monsters["monster5"]["image_id"]
    if card_id == 6:
        strength = monsters["monster6"]["strength"]
        speed = monsters["monster6"] ["speed"]
        stealth = monsters["monster6"] ["stealth"]
        cunning = monsters["monster6"] ["cunning"]
        total = monsters["monster6"] ["total_score"]  
        monster_image = monsters["monster6"]["image_id"]      
    if card_id == 7:
        strength = monsters["monster7"]["strength"]
        speed = monsters["monster7"] ["speed"]
        stealth = monsters["monster7"] ["stealth"]
        cunning = monsters["monster7"] ["cunning"]
        total = monsters["monster7"] ["total_score"]   
        monster_image = monsters["monster7"]["image_id"]    
    if card_id == 8:
        strength = monsters["monster8"]["strength"]
        speed = monsters["monster8"] ["speed"]
        stealth = monsters["monster8"] ["stealth"]
        cunning = monsters["monster8"] ["cunning"]
        total = monsters["monster7"] ["total_score"] 
        monster_image = monsters["monster8"]["image_id"] 
    if card_id == 9:
        strength = monsters["monster9"]["strength"]
        speed = monsters["monster9"] ["speed"]
        stealth = monsters["monster9"] ["stealth"]
        cunning = monsters["monster9"] ["cunning"]
        total = monsters["monster9"] ["total_score"]  
        monster_image = monsters["monster9"]["image_id"] 
    if card_id == 10:
        strength = monsters["monster10"]["strength"]
        speed = monsters["monster10"] ["speed"]
        stealth = monsters["monster10"] ["stealth"]
        cunning = monsters["monster10"] ["cunning"]
        total = monsters["monster10"] ["total_score"]  
        monster_image = monsters["monster10"]["image_id"]

    strength_stat.config(text= strength)
    speed_stat.config(text= speed)
    sneak_stat.config(text= stealth)
    cunning_stat.config(text= cunning)
    total_stat.config(text= total)

    frame_mainpage_bg.pack_forget()
    root.geometry("450x650")

    frame_card_preview.pack(fill=BOTH, expand = TRUE)

def adding_page():

    global slider_strength
    global slider_speed
    global slider_stealth
    global slider_cunning
    global label_strength_stat
    global label_speed_stat
    global label_sneak_stat
    global label_cunning_stat
    global label_total_stat

    frame_teal_bar1 = Frame(frame_adding_page, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= 70)
    frame_teal_bar1.place(y = 10, x = 20)

    label_card_creation = Label(frame_teal_bar1, text="Card Cration", fg = DARK_RED, font = (FONT_TYPE, 35), background= LIGHT_TEAL)
    label_card_creation.place(y = 7, x = 10)

    button_add_exit = Button(frame_teal_bar1, text = "Exit", fg = DARK_RED, font = (FONT_TYPE, 18), bg=RED, command= exit)
    button_add_exit.place(y = 13, x = 300)

    frame_teal_bar2 = Frame(frame_adding_page, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar2.place(y = 120, x = 20)

    label_strength = Label(frame_teal_bar2, text="Strength: ", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_strength.place(y = 8, x = 10)

    slider_strength = Scale(frame_teal_bar2, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_strength.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar3 = Frame(frame_adding_page, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar3.place(y = 230, x = 20)

    label_speed = Label(frame_teal_bar3, text="Speed: ", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_speed.place(y = 8, x = 10)

    slider_speed = Scale(frame_teal_bar3, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_speed.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar4 = Frame(frame_adding_page, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar4.place(y = 340, x = 20)

    label_Stealth = Label(frame_teal_bar4, text="Stealth:", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_Stealth.place(y = 8, x = 10)

    slider_stealth = Scale(frame_teal_bar4, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_stealth.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar5 = Frame(frame_adding_page, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar5.place(y = 450, x = 20)

    label_cunning = Label(frame_teal_bar5, text="Cunning:", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_cunning.place(y = 8, x = 10)

    slider_cunning = Scale(frame_teal_bar5, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_cunning.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    entry_name = Entry(frame_adding_page, background= DARK_TEAL, fg = "white", font = (FONT_TYPE, 10), bd=3)
    entry_name.place(y = 20, x = 450, width= 350, height= 30)

    button_card_option1 = Button(frame_adding_page, bg="white", width= 20, height= 14)
    button_card_option1.place(y = 65, x = 450)

    button_card_option2 = Button(frame_adding_page, bg="white", width= 20, height= 14)
    button_card_option2.place(y = 65, x = 650)

    button_card_option3 = Button(frame_adding_page, bg="white", width= 20, height= 14)
    button_card_option3.place(y = 300, x = 450)   
    
    button_card_option4 = Button(frame_adding_page, bg="white", width= 20, height= 14)
    button_card_option4.place(y = 300, x = 650)  

    button_confirm = Button(frame_adding_page, text= "Confirm", bg=LIGHT_TEAL, font = (FONT_TYPE, 13), command= card_confirmation)
    button_confirm.place(y = 530, x = 20)

    frame_mainpage_bg.pack_forget()
    frame_card_confirmation.pack_forget()
    frame_adding_page.pack(fill = BOTH, expand= TRUE)
    root.geometry("840x570")

def card_confirmation(): 

    frame_adding_page.pack_forget()
    frame_card_confirmation.pack(fill = BOTH, expand = TRUE)
    root.geometry("450x650")

    new_strength = slider_strength.get()
    new_speed = slider_speed.get()
    new_stealth = slider_stealth.get()
    new_cunning = slider_cunning.get()
    new_total = new_strength + new_speed + new_stealth + new_cunning

    label_strength_stat.config(text=new_strength)
    label_speed_stat.config(text = new_speed)
    label_cunning_stat.config(text = new_cunning)
    label_total_stat.config(text = new_total)
    label_sneak_stat.config(text = new_stealth)


monsters= {
    "monster1" : {
        "monster_name": "Vexscream", 
        "image_id": "black_monster.png",
        "strength": 1, 
        "speed": 6, 
        "stealth": 21, 
        "cunning": 19,
        "total_score": 47
    },
    "monster2" : {
        "monster_name": "Dawnmirage", 
        "image_id": "badapple_monster.png",
        "strength": 5, 
        "speed": 15, 
        "stealth": 18, 
        "cunning": 22,
        "total_score": 60
    },
       "monster3" : {
        "monster_name": "Blazegolem", 
        "image_id": "fullthrottle_monster.png",
        "strength": 15, 
        "speed": 20, 
        "stealth": 23, 
        "cunning": 6,
        "total_score": 64
    }, 
        "monster4" : {
        "monster_name": "Moldvine", 
        "image_id": "khaotic_monster.png",
        "strength": 21, 
        "speed": 18, 
        "stealth": 14, 
        "cunning": 5,
        "total_score": 58
    }, 
        "monster5" : {
        "monster_name": "Vertexwing", 
        "image_id": "pipelinepunch_monster.png",
        "strength": 19, 
        "speed": 13, 
        "stealth": 18, 
        "cunning": 2,
        "total_score": 53
    }, 
        "monster6" : {
        "monster_name": "Froststep", 
        "image_id": "riopunch_monster.png",
        "strength": 14, 
        "speed": 14, 
        "stealth": 17, 
        "cunning": 4,
        "total_score": 49
    }, 
        "monster7" : {
        "monster_name": "Wispghoul", 
        "image_id": "UPK_monster.png",
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

button_add= Button(frame_graytbox, text="Add", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command= adding_page)
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

image1_path= "black_monster.png"
monster_image1 = Image.open(image1_path)
monster_image1 = monster_image1.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo1 = ImageTk.PhotoImage(monster_image1)


image2_path= "badapple_monster.png" 
monster_image2 = Image.open(image2_path)
monster_image2 = monster_image2.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo2 = ImageTk.PhotoImage(monster_image2)

image3_path= "fullthrottle_monster.png" 
monster_image3 = Image.open(image3_path)
monster_image3 = monster_image3.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo3 = ImageTk.PhotoImage(monster_image3)

image4_path= "khaotic_monster.png" 
monster_image4 = Image.open(image4_path)
monster_image4 = monster_image4.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo4 = ImageTk.PhotoImage(monster_image4)

image5_path= "pipelinepunch_monster.png" 
monster_image5 = Image.open(image5_path)
monster_image5 = monster_image5.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo5 = ImageTk.PhotoImage(monster_image5)

image6_path= "riopunch_monster.png" 
monster_image6 = Image.open(image6_path)
monster_image6 = monster_image6.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo6 = ImageTk.PhotoImage(monster_image6)

image7_path= "UPK_monster.png" 
monster_image7 = Image.open(image7_path)
monster_image7 = monster_image7.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
monster_photo7 = ImageTk.PhotoImage(monster_image7)

button_cardslot_1 = Button(frame_mainpage_bg, image = monster_photo1, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_1)
button_cardslot_1.place(y = TOP_ROW_BUTTONS_YAXIS, x = 100)
button_cardslot_1.image = monster_photo1

button_cardslot_2 = Button(frame_mainpage_bg, image= monster_photo2, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_2)
button_cardslot_2.place(y = TOP_ROW_BUTTONS_YAXIS, x = 240)
button_cardslot_2.image = monster_photo2

button_cardslot_3 = Button(frame_mainpage_bg, image= monster_photo3, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_3)
button_cardslot_3.place(y = TOP_ROW_BUTTONS_YAXIS, x = 380)
button_cardslot_3.image = monster_photo3

button_cardslot_4 = Button(frame_mainpage_bg, image= monster_photo4, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_4)
button_cardslot_4.place(y = TOP_ROW_BUTTONS_YAXIS, x = 520)
button_cardslot_4.image = monster_photo4

button_cardslot_5 = Button(frame_mainpage_bg, image= monster_photo5, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_5)
button_cardslot_5.place(y = TOP_ROW_BUTTONS_YAXIS, x = 660)
button_cardslot_5.image = monster_photo5

button_cardslot_6 = Button(frame_mainpage_bg, image= monster_photo6, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_6)
button_cardslot_6.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 100)
button_cardslot_6.image = monster_photo6

button_cardslot_7 = Button(frame_mainpage_bg, image= monster_photo7, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_7)
button_cardslot_7.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 240)
button_cardslot_7.image = monster_photo7

button_cardslot_8 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_8)
button_cardslot_8.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 380)

button_cardslot_9 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_9)
button_cardslot_9.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 520)

button_cardslot_10 = Button(frame_mainpage_bg, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_10)
button_cardslot_10.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 660)

frame_card_preview = Frame(root, bg=DARK_TEAL)

image_placeholder = "placeholder.png"
image_monster = Image.open(image_placeholder)
image_monster = image_monster.resize((300,360), Image.LANCZOS)
image_monster = ImageTk.PhotoImage(image_monster)
label_preview_image = Label(frame_card_preview, image=image_monster)
label_preview_image.place(y = 15, x = 15)

label_strength = Label(frame_card_preview, text="Srength:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_strength.place(y = 390, x = STATS_LABELS_XAXIS, width= 105)

strength_stat = Label(frame_card_preview, text="", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
strength_stat.place(y = 390, x = STATS_XAXIS)

label_speed = Label(frame_card_preview, text="Speed:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_speed.place(y = 430, x = STATS_LABELS_XAXIS, width= 105)

speed_stat = Label(frame_card_preview, text="", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
speed_stat.place(y = 430, x = STATS_XAXIS)

label_Stealth = Label(frame_card_preview, text="Stealth:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_Stealth.place(y = 470, x = STATS_LABELS_XAXIS, width= 105)

sneak_stat = Label(frame_card_preview, text="", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
sneak_stat.place(y = 470, x = STATS_XAXIS)

label_cunning = Label(frame_card_preview, text="Cunning:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_cunning.place(y = 510, x = STATS_LABELS_XAXIS, width= 105)

cunning_stat = Label(frame_card_preview, text="", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
cunning_stat.place(y = 510, x = STATS_XAXIS)

label_total = Label(frame_card_preview, text="Total:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_total.place(y = 550, x = STATS_LABELS_XAXIS, width= 105)

total_stat = Label(frame_card_preview, text="", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
total_stat.place(y = 550, x = STATS_XAXIS)

button_return = Button(frame_card_preview, text="Return", fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL, command= return_function)
button_return.place(y = 600, x = 320)

button_card_exit = Button(frame_card_preview, text="Exit", fg = DARK_RED, font = (FONT_TYPE, 16), bg=RED, command= exit)
button_card_exit.place(y = 12, x = 380)

frame_adding_page = Frame(root, bg=DARK_TEAL)

frame_card_confirmation = Frame(root, bg = DARK_TEAL)

label_strength = Label(frame_card_confirmation, text="strength:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_strength.place(y = 390, x = STATS_LABELS_XAXIS, width= 105)

label_strength_stat = Label(frame_card_confirmation, text=" ", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
label_strength_stat.place(y = 390, x = STATS_XAXIS)

label_speed = Label(frame_card_confirmation, text="Speed:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_speed.place(y = 430, x = STATS_LABELS_XAXIS, width= 105)

label_speed_stat = Label(frame_card_confirmation, text=" ", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
label_speed_stat.place(y = 430, x = STATS_XAXIS)

label_Stealth = Label(frame_card_confirmation, text="Stealth:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_Stealth.place(y = 470, x = STATS_LABELS_XAXIS, width= 105)

label_sneak_stat = Label(frame_card_confirmation, text=" ", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
label_sneak_stat.place(y = 470, x = STATS_XAXIS)

label_cunning = Label(frame_card_confirmation, text="Cunning:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_cunning.place(y = 510, x = STATS_LABELS_XAXIS, width= 105)

label_cunning_stat = Label(frame_card_confirmation, text=" ", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
label_cunning_stat.place(y = 510, x = STATS_XAXIS)

label_total = Label(frame_card_confirmation, text="Total:", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=LIGHT_TEAL )
label_total.place(y = 550, x = STATS_LABELS_XAXIS, width= 105)

label_total_stat = Label(frame_card_confirmation, text=" ", fg = DARK_RED, font = (FONT_TYPE, STATS_FONT_SIZE), bg=DARK_TEAL )
label_total_stat.place(y = 550, x = STATS_XAXIS)

button_cancel = Button(frame_card_confirmation, text="Cancel", fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL, command= adding_page)
button_cancel.place(y = 600, x = 50)

root.mainloop()