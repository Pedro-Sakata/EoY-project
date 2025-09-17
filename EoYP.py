#imports the tkinter library
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import json

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
PREVIEW_RESIZE_WIDTH = 320
PREVIEW_RESIZE_HEIGHT = 600
MAX_LENGTH = 16

#Function to open the images
def open_images():

    #global variables
    global monster_photo1
    global monster_photo2
    global monster_photo3
    global monster_photo4
    global monster_photo5
    global monster_photo6
    global monster_photo7

    global monster_image1
    global monster_image2
    global monster_image3
    global monster_image4
    global monster_image5
    global monster_image6
    global monster_image7

    global monster_option1
    global monster_option2
    global monster_option3
    global monster_option4
    
    global option1
    global option2
    global option3
    global option4

    #opens and assigness first image
    image1_path= "EPK.png"
    monster_image1 = Image.open(image1_path)
    monster_image1 = monster_image1.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo1 = ImageTk.PhotoImage(monster_image1)

     #opens and assigness second image
    image2_path= "MULE.png" 
    monster_image2 = Image.open(image2_path)
    monster_image2 = monster_image2.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo2 = ImageTk.PhotoImage(monster_image2)

    #opens and assigness third image
    image3_path= "OG_BIG.png" 
    monster_image3 = Image.open(image3_path)
    monster_image3 = monster_image3.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo3 = ImageTk.PhotoImage(monster_image3)

    #opens and assigness fourth image
    image4_path= "PIPELINE_PUNCH.png" 
    monster_image4 = Image.open(image4_path)
    monster_image4 = monster_image4.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo4 = ImageTk.PhotoImage(monster_image4)

    #opens and assigness fifth image
    image5_path= "PUNCH.png" 
    monster_image5 = Image.open(image5_path)
    monster_image5 = monster_image5.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo5 = ImageTk.PhotoImage(monster_image5)

    #opens and assigness sixth image
    image6_path= "UFRR.png" 
    monster_image6 = Image.open(image6_path)
    monster_image6 = monster_image6.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo6 = ImageTk.PhotoImage(monster_image6)

    #opens and assigness seventh image
    image7_path= "ULTRA_FIEASTA.png" 
    monster_image7 = Image.open(image7_path)
    monster_image7 = monster_image7.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo7 = ImageTk.PhotoImage(monster_image7)

    #opens and assigness first option image
    option1_path = "ULTRA_ROSA.png"
    option1 = Image.open(option1_path)
    option1 = option1.resize((145,213), Image.LANCZOS)
    monster_option1 = ImageTk.PhotoImage(option1)

    #opens and assigness second option image
    option2_path = "ULTRA_VIOLET.png"
    option2 = Image.open(option2_path)
    option2 = option2.resize((145,213), Image.LANCZOS)
    monster_option2 = ImageTk.PhotoImage(option2)

    #opens and assigness third option image
    option3_path = "WATER_MELLON.png"
    option3 = Image.open(option3_path)
    option3 = option3.resize((145,213), Image.LANCZOS)
    monster_option3 = ImageTk.PhotoImage(option3)

    #opens and assigness fourth option image
    option4_path = "OG.png"
    option4 = Image.open(option4_path)
    option4 = option4.resize((145,213), Image.LANCZOS)
    monster_option4 = ImageTk.PhotoImage(option4)

#Function that sorts the dictionary
def sort_cards():

    #global variables
    global index 
    global sort_strength, sort_speed, sort_stealth, sort_cunning, sort_total
    
    #creates dictionaries that will be used to store each type of sort
    sort_strength = {}
    sort_speed = {}
    sort_stealth = {}
    sort_cunning = {}
    sort_total = {}

    #checks if the index has exeded the limit of 5, if yes it reverts the index value back to 1
    if (index > 5):
        index = 1

    #Checks if the index is equal to 1
    if (index == 1):

        #Makes sort_strength a copy of monsters dictionary that is sorted by strength 
        sort_strength = dict(
            sorted(monsters.items(), key=lambda item: item[1]['strength'], reverse=True))

    #Checks if the index is equal to 2
    elif (index == 2):

        #Makes sort_speed a copy of monsters dictionary that is sorted by speed 
        sort_speed = dict( 
            sorted(monsters.items(), key=lambda item: item[1]['speed'], reverse=True))

    #Checks if the index is equal to 3      
    elif (index == 3):

        #Makes sort_stealth a copy of monsters dictionary that is sorted by stealth 
        sort_stealth = dict(
            sorted(monsters.items(), key=lambda item: item[1]['stealth'], reverse=True))

    #Checks if the index is equal to 4
    elif (index == 4):

        #Makes sort_cunning a copy of monsters dictionary that is sorted by cunning 
        sort_cunning = dict(
            sorted(monsters.items(), key=lambda item: item[1]['cunning'], reverse=True))

    #Checks if the index is equal to 5
    elif (index == 5):

        #Makes sort_total a copy of monsters dictionary that is sorted by total 
        sort_total = dict(
            sorted(monsters.items(), key=lambda item: item[1]['total_score'], reverse=True))

    #calls the function were the sorted dictionary is saved to the file
    save_to_file()

#Function were the index is incrimented 
def incriment_index():

    #Globals the index 
    global index

    #incriments the index
    index = index + 1

    #calls the function were the cards are sorted
    sort_cards()

    #checks if index equals 1
    if (index == 1):

        #creates message box saying the sort is set to strength
        messagebox.showinfo("Sorted by strength", "The file has been sorted by strength. Print to view")
    
    #checks if index equals 2
    elif (index == 2): 

        #creates message box saying the sort is set to speed
        messagebox.showinfo("Sorted by speed", "The file has been sorted by speed. Print to view")
    
    #checks if index equals 3
    elif (index == 3): 

        #creates message box saying the sort is set to stealth
        messagebox.showinfo("Sorted by stealth", "The file has been sorted by stealth. Print to view")
    
    #checks if index equals 4
    elif (index == 4): 

        #creates message box saying the sort is set to cunning
        messagebox.showinfo("Sorted by cunning", "The file has been sorted by cunning. Print to view")
    
    #checks if index equals 5
    elif (index == 5): 

        #creates message box saying the sort is set to total
        messagebox.showinfo("Sorted by total", "The file has been sorted by total. Print to view")

#Function were the dictionary is saved to the file
def save_to_file():

    #Globals the variables
    global monsters
    global index
    global sort_strength, sort_speed, sort_stealth, sort_cunning, sort_total
    global saved_dictionary 

    #checks if the index is equal to 1
    if (index == 1):

        #loops the through the dictionary that is sorted by strength 
        for each in sort_strength:

            #turns the image_id of the current incriment in the dictionary into a string
            sort_strength[each]["image_id"] = str(sort_strength[each]["image_id"])

        #Makes the saved dictionary equal to the sorted by strenth dictionary that was turned into a string
        saved_dictionary = str(sort_strength)

        #opens the json file
        with open("monster.json", 'w') as json_file:

            #saves the sorted by strength dictionary to the json file
            json.dump(sort_strength, json_file, indent=4)    

    #checks if the index is equal to 2
    elif (index == 2):

        #loops the through the dictionary that is sorted by speed 
        for each in sort_speed:

            #turns the image_id of the current incriment in the dictionary into a string
            sort_speed[each]["image_id"] = str(sort_speed[each]["image_id"])

        #Makes the saved dictionary equal to the sorted by speed dictionary that was turned into a string
        saved_dictionary = str(sort_speed)

        #opens the json file
        with open("monster.json", 'w') as json_file:

            #saves the sorted by speed dictionary to the json file
            json.dump(sort_speed, json_file, indent=4)  

    #checks if the index is equal to 3
    elif (index == 3):

        #loops the through the dictionary that is sorted by stealth 
        for each in sort_stealth:

            #turns the image_id of the current incriment in the dictionary into a string
            sort_stealth[each]["image_id"] = str(sort_stealth[each]["image_id"])

        #Makes the saved dictionary equal to the sorted by stealth dictionary that was turned into a string
        saved_dictionary = str(sort_stealth)

        #opens the json file
        with open("monster.json", 'w') as json_file:

            #saves the sorted by stealth dictionary to the json file
            json.dump(sort_stealth, json_file, indent=4)  

    #checks if the index is equal to 4
    elif (index == 4):

        #loops the through the dictionary that is sorted by cunning 
        for each in sort_cunning:

            #turns the image_id of the current incriment in the dictionary into a string
            sort_cunning[each]["image_id"] = str(sort_cunning[each]["image_id"])

        #Makes the saved dictionary equal to the sorted by cunning dictionary that was turned into a string
        saved_dictionary = str(sort_cunning)
        
        #opens the json file
        with open("monster.json", 'w') as json_file:

            #saves the sorted by cunning dictionary to the json file
            json.dump(sort_cunning, json_file, indent=4)          

    #checks if the index is equal to 5
    elif (index == 5):

        #loops the through the dictionary that is sorted by total 
        for each in sort_total:

            #turns the image_id of the current incriment in the dictionary into a string
            sort_total[each]["image_id"] = str(sort_total[each]["image_id"])

        #Makes the saved dictionary equal to the sorted by total dictionary that was turned into a string
        saved_dictionary = str(sort_total)

        #opens the json file
        with open("monster.json", 'w') as json_file:

            #saves the sorted by total dictionary to the json file
            json.dump(sort_total, json_file, indent=4)  

#Function were the new card is saved to the dictionary
def save_card():

    #globals variables
    global monster_option1, monster_option2, monster_option3, monster_option4
    global option1, option2, option3, option4
    global new_strength, new_speed, new_stealth, new_cunning, new_total
    global cards_added
    global button_cardslot_8, button_cardslot_9, button_cardslot_10
    global is_slot_8_free, is_slot_9_free, is_slot_10_free
    global name

    #incriments the cards added variable
    cards_added += 1

    #call button resize function
    button_resize()

    #checks if slot 8 is free 
    if (is_slot_8_free == True):

        #Add the new card data as 8 on the dictionary
        monsters[8] = { 
        "monster_name": name, 
        "image_id": chosen_card,
        "strength": new_strength, 
        "speed": new_speed, 
        "stealth": new_stealth, 
        "cunning": new_cunning,
        "total_score": new_total
        }
        
        #creates and packs eightth card button
        button_cardslot_8 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_8)
        button_cardslot_8.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 380)
        button_cardslot_8.image = chosen_card
        is_slot_8_free = False

    #checks if slot 9 is free 
    elif(is_slot_9_free == True):

        #Add the new card data as 9 on the dictionary
        monsters[9] = { 
        "monster_name": name, 
        "image_id": chosen_card,
        "strength": new_strength, 
        "speed": new_speed, 
        "stealth": new_stealth, 
        "cunning": new_cunning,
        "total_score": new_total
        }

        #creates and packs nineth card button
        button_cardslot_9 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_9)
        button_cardslot_9.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 520)
        button_cardslot_9.image = chosen_card
        is_slot_9_free = False

    #checks if slot 10 is free 
    elif(is_slot_10_free == True):

        #Add the new card data as 10 on the dictionary
        monsters[10] = { 
        "monster_name": name, 
        "image_id": chosen_card,
        "strength": new_strength, 
        "speed": new_speed, 
        "stealth": new_stealth, 
        "cunning": new_cunning,
        "total_score": new_total
        }

        #creates and packs tenth card button
        button_cardslot_10 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_10)
        button_cardslot_10.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 660)
        button_cardslot_10.image = chosen_card
        is_slot_8_free = False

    #calls card sorting function
    sort_cards()

    #calls save to file function
    save_to_file()

    #calls return function
    return_function()

#Function were the option button images are resized
def button_resize():

    #Globals variables
    global monster_option1
    global monster_option2
    global monster_option3
    global monster_option4
    
    global option1
    global option2
    global option3
    global option4

    #Resize option image 1
    option1 = option1.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_option1= ImageTk.PhotoImage(option1)

    #Resize option image 2
    option2 = option2.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_option2= ImageTk.PhotoImage(option2)

    #Resize option image 3
    option3 = option3.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_option3= ImageTk.PhotoImage(option3)

    #Resize option image 4
    option4 = option4.resize((IMAGE_RESIZE_WIDTH,IMAGE_RESIZE_HEIGHT), Image.LANCZOS)
    monster_option4= ImageTk.PhotoImage(option4)

#Function were card ID is set to 1
def id_1():

    #Globals variables
    global card_id
    global monster_image1
    global monster_photo1

    #sets card id to 1
    card_id = 1

    #resizes monster image 1
    monster_image1 = monster_image1.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo1 = ImageTk.PhotoImage(monster_image1)

    #calls card preview function
    card_preview()

#Function were card ID is set to 2    
def id_2():

    #Globals variables
    global card_id
    global monster_image2
    global monster_photo2

    #sets card id to 2
    card_id = 2

    #resizes monster image 2
    monster_image2 = monster_image2.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo2 = ImageTk.PhotoImage(monster_image2)
    
    #calls card preview function
    card_preview()

#Function were card ID is set to 3
def id_3():

    #Globals variables
    global card_id
    global monster_image3
    global monster_photo3

    #sets card id to 3
    card_id = 3

    #resizes monster image 3
    monster_image3 = monster_image3.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo3 = ImageTk.PhotoImage(monster_image3)

    #calls card preview function
    card_preview()

#Function were card ID is set to 4
def id_4():

    #Globals variables
    global card_id
    global monster_image4
    global monster_photo4

    #sets card id to 4
    card_id = 4

    #resizes monster image 4
    monster_image4 = monster_image4.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo4 = ImageTk.PhotoImage(monster_image4)

    #calls card preview function
    card_preview()

#Function were card ID is set to 5
def id_5():

    #Globals variables
    global card_id
    global monster_image5
    global monster_photo5

    #sets card id to 5
    card_id = 5

    #resizes monster image 5
    monster_image5 = monster_image5.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo5 = ImageTk.PhotoImage(monster_image5)

    #calls card preview function
    card_preview()

#Function were card ID is set to 6
def id_6():

    #Globals variables
    global card_id
    global monster_image6
    global monster_photo6

    #sets card id to 6
    card_id = 6

    #resizes monster image 6
    monster_image6 = monster_image6.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo6 = ImageTk.PhotoImage(monster_image6)

    #calls card preview function
    card_preview()

#Function were card ID is set to 7
def id_7():

    #Globals variables
    global card_id
    global monster_image7
    global monster_photo7

    #sets card id to 7
    card_id = 7

    #resizes monster image 7
    monster_image7 = monster_image7.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
    monster_photo7 = ImageTk.PhotoImage(monster_image7)

    #calls card preview function
    card_preview()

#Function were card ID is set to 8
def id_8():

    #Globals variables
    global card_id

    #sets card id to 8
    card_id = 8

    #calls card preview function
    card_preview()

#Function were card ID is set to 9
def id_9():

    #Globals variables
    global card_id

    #sets card id to 9
    card_id = 9

    #calls card preview function
    card_preview()

#Function were card ID is set to 10
def id_10():

    #Globals variables
    global card_id

    #sets card id to 10
    card_id = 10

    #calls card preview function
    card_preview()

#Funtion that closes other frames and returns to the main page 
def return_function():

    #closes other frames
    frame_output.pack_forget()
    frame_card_preview.pack_forget()
    frame_adding_page.pack_forget()
    frame_card_confirmation.pack_forget()
    frame_card_editing.pack_forget()

    #packs main page and reverts the root geometry
    frame_mainpage.pack(fill = BOTH, expand= True)
    root.geometry("840x570")

#Function were the card preview is done
def card_preview():

    #globals variables
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
    global monsters
    
    #sets the temporary vaiables to equal to the coresponding stat from the dictionary based on card id
    name = monsters[card_id]["monster_name"]
    strength = monsters[card_id]["strength"]
    speed = monsters[card_id] ["speed"]
    stealth = monsters[card_id] ["stealth"]
    cunning = monsters[card_id] ["cunning"]
    total = monsters[card_id] ["total_score"]
    monster_image = monsters[card_id]["image_id"]


    delete_button = Button(frame_card_preview , text = "Delete", fg = DARK_RED, font = (FONT_TYPE, 16), bg = RED, command=lambda: remove_card(monsters, card_id))
    delete_button.place(y = 600, x = 200)

    strength_stat.config(text= strength)
    speed_stat.config(text= speed)
    sneak_stat.config(text= stealth)
    cunning_stat.config(text= cunning)
    total_stat.config(text= total)

    label_preview_image.config(image= monster_image)
    
    label_preview_name.config(text = name)

    frame_mainpage.pack_forget()
    frame_card_preview.pack(fill=BOTH, expand = True)
    root.geometry("450x650")

def remove_card(d, card_id):
    global button_cardslot_8, button_cardslot_9, button_cardslot_10
    global is_slot_8_free, is_slot_9_free, is_slot_10_free
    global cards_added
    
    if (card_id < 8):
        messagebox.showerror("Original seven monster selected", "You can not remove one of the original monsters")
        return_function()
    elif (card_id > 7):
        cards_added = cards_added - 1

        if (card_id == 8):
            button_cardslot_8.destroy()
            is_slot_8_free = True
        elif(card_id == 9):
            button_cardslot_9.destroy()
            is_slot_9_free = True
        elif(card_id == 10):
            button_cardslot_10.destroy()
            is_slot_10_free = True

        keys_to_remove_in_current_level = []

        for key, value in d.items():
            if key == card_id:
                keys_to_remove_in_current_level.append(key)
            elif isinstance(value, dict):
                remove_card(value, card_id)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        remove_card(item, card_id)

        for key in keys_to_remove_in_current_level:
            del d[key]

        return_function()

def chose_card1():
    global chosen_card
    global option1
    global monster_option1
    global is_picked
    is_picked = True
    option1 = option1.resize((320,360), Image.LANCZOS)
    monster_option1 = ImageTk.PhotoImage(option1)
    chosen_card = monster_option1

def chose_card2():
    global chosen_card
    global option2
    global monster_option2
    global is_picked
    is_picked = True
    option2 = option2.resize((320,360), Image.LANCZOS)
    monster_option2 = ImageTk.PhotoImage(option2)
    chosen_card = monster_option2

def chose_card3():
    global chosen_card
    global option3
    global monster_option3
    global is_picked
    is_picked = True
    option3 = option3.resize((320,360), Image.LANCZOS)
    monster_option3 = ImageTk.PhotoImage(option3)
    chosen_card = monster_option3

def chose_card4():
    global chosen_card
    global option4
    global monster_option4
    global is_picked
    is_picked = True
    option4 = option4.resize((320,360), Image.LANCZOS)
    monster_option4 = ImageTk.PhotoImage(option4)
    chosen_card = monster_option4

def enforce_limit(*args):

    s = entry_text.get()
    if len(s) > MAX_LENGTH:
        entry_text.set(s[:MAX_LENGTH])

def card_confirmation(): 

    global entry_name, label_monster_name
    global new_strength, new_speed, new_stealth, new_cunning, new_total
    global cards_added
    global is_picked
    global name

    name = entry_name.get()

    frame_adding_page.pack_forget()
    frame_card_confirmation.pack(fill = BOTH, expand = True)
    root.geometry("450x650")

    if (not name):
        messagebox.showerror("missing monster name", "No name was input. Please chosse a name with up to 16 characters")
        adding_page()
        card_confirmation.pack_forget()
    if (is_picked == False):
        messagebox.showerror("missing monster image", "No image was selected. Please chosse an image")
        adding_page()
        card_confirmation.pack_forget()

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

    label_confirm_image = Label(frame_card_confirmation, image=chosen_card, width=320, height=360)
    label_confirm_image.place(y = 15, x = 15)

    label_monster_name = Label(frame_card_confirmation, text = name, fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL)
    label_monster_name.place(y = 385, x = 197)

def adding_page():

    global slider_strength, slider_speed, slider_stealth, slider_cunning
    global label_strength_stat, label_speed_stat, label_sneak_stat, label_cunning_stat, label_total_stat
    global monster_option1, monster_option2, monster_option3, monster_option4
    global option1, option2, option3, option4
    global entry_name
    global entry_text
    global cards_added

    if (cards_added == 3):
        messagebox.showerror("Maximum card limit reached", "You have reached the maximum card limit of 10")
        return_function()

    else:
        option1 = option1.resize((145,213), Image.LANCZOS)
        monster_option1 = ImageTk.PhotoImage(option1)

        option2 = option2.resize((145,213), Image.LANCZOS)
        monster_option2 = ImageTk.PhotoImage(option2)

        option3 = option3.resize((145,213), Image.LANCZOS)
        monster_option3 = ImageTk.PhotoImage(option3)

        option4 = option4.resize((145,213), Image.LANCZOS)
        monster_option4 = ImageTk.PhotoImage(option4)

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

        entry_text = StringVar()
        entry_text.trace("w", enforce_limit)
        entry_name = Entry(frame_adding_page, textvariable=entry_text, background= DARK_TEAL, fg = "white", font = (FONT_TYPE, 10), bd=3)
        entry_name.place(y = 20, x = 450, width= 350, height= 30)  

        button_card_option1 = Button(frame_adding_page, image= monster_option1, width= 145, height= 213, command=chose_card1)
        button_card_option1.place(y = 65, x = 450)
        button_card_option1.image = monster_option1

        button_card_option2 = Button(frame_adding_page, image= monster_option2, width= 145, height= 213, command=chose_card2)
        button_card_option2.place(y = 65, x = 650)
        button_card_option2.image = monster_option2

        button_card_option3 = Button(frame_adding_page, image= monster_option3, width= 145, height= 213, command=chose_card3)
        button_card_option3.place(y = 300, x = 450)
        button_card_option3.image = monster_option3
        
        button_card_option4 = Button(frame_adding_page, image= monster_option4, width= 145, height= 213, command=chose_card4)
        button_card_option4.place(y = 300, x = 650)
        button_card_option4.image = monster_option4

        button_confirm = Button(frame_adding_page, text= "Confirm", fg = DARK_RED, bg=LIGHT_TEAL, font = (FONT_TYPE, 13), command= card_confirmation)
        button_confirm.place(y = 530, x = 20)

        button_cancel = Button(frame_adding_page, text="Cancel", fg = DARK_RED, font = (FONT_TYPE, 13), bg=LIGHT_TEAL, command= return_function)
        button_cancel.place(y = 530, x = 100)

        frame_mainpage.pack_forget()
        frame_card_confirmation.pack_forget()
        frame_adding_page.pack(fill = BOTH, expand= True)
        root.geometry("840x570")

def edit_save(d):
    global card_id

    edited_name = entry_name_edit.get()

    edited_strength =  slider_strength_edit.get()
    edited_speed = slider_speed_edit.get()
    edited_stealth = slider_stealth_edit.get()
    edited_cunning = slider_cunning_edit.get()

    edited_new_total = edited_strength + edited_speed + edited_stealth + edited_cunning

    keys_to_remove_in_current_level = []

    for key, value in d.items():
        if key == card_id:
            keys_to_remove_in_current_level.append(key)
        elif isinstance(value, dict):
            remove_card(value, card_id)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_card(item, card_id)

    for key in keys_to_remove_in_current_level:
        del d[key]

    if (card_id == 8):
        monsters[8] = { 
        "monster_name": edited_name, 
        "image_id": chosen_card,
        "strength": edited_strength, 
        "speed": edited_speed, 
        "stealth": edited_stealth, 
        "cunning": edited_cunning,
        "total_score": edited_new_total
        }    
        button_cardslot_8 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_8)
        button_cardslot_8.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 380)
        button_cardslot_8.image = chosen_card

    elif (card_id == 9):
        monsters[9] = { 
        "monster_name": edited_name, 
        "image_id": chosen_card,
        "strength": edited_strength, 
        "speed": edited_speed, 
        "stealth": edited_stealth, 
        "cunning": edited_cunning,
        "total_score": edited_new_total
        } 
        button_cardslot_9 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_9)
        button_cardslot_9.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 520)
        button_cardslot_9.image = chosen_card

    elif (card_id == 10):
        monsters[10] = { 
        "monster_name": edited_name, 
        "image_id": chosen_card,
        "strength": edited_strength, 
        "speed": edited_speed, 
        "stealth": edited_stealth, 
        "cunning": edited_cunning,
        "total_score": edited_new_total
        }    
        button_cardslot_10 = Button(frame_mainpage, image = chosen_card, bg=DARK_TEAL, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_10)
        button_cardslot_10.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 660)
        button_cardslot_10.image = chosen_card

    save_to_file()
    return_function()

def aditing_confirmation():
    confirmation = messagebox.askquestion("confirm changes", "Do you want to confirm these changes?")
    if (confirmation == "yes"):
        messagebox.showinfo("Confirmed", "Your changes have been saved")
        edit_save()
    else:
        messagebox.showinfo("Canceled", "Your changes have been descarted")
        return_function()

def edit_cards():

    global slider_strength_edit, slider_speed_edit, slider_stealth_edit, slider_cunning_edit
    global monster_option1, monster_option2, monster_option3, monster_option4
    global option1, option2, option3, option4
    global entry_name_edit
    global entry_text
    global card_id

    frame_teal_bar1 = Frame(frame_card_editing, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= 70)
    frame_teal_bar1.place(y = 10, x = 20)

    label_card_creation = Label(frame_teal_bar1, text="Card Cration", fg = DARK_RED, font = (FONT_TYPE, 35), background= LIGHT_TEAL)
    label_card_creation.place(y = 7, x = 10)

    button_add_exit = Button(frame_teal_bar1, text = "Exit", fg = DARK_RED, font = (FONT_TYPE, 18), bg=RED, command= exit)
    button_add_exit.place(y = 13, x = 300)

    frame_teal_bar2 = Frame(frame_card_editing, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar2.place(y = 120, x = 20)

    label_strength = Label(frame_teal_bar2, text="Strength: ", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_strength.place(y = 8, x = 10)

    slider_strength_edit = Scale(frame_teal_bar2, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_strength_edit.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar3 = Frame(frame_card_editing, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar3.place(y = 230, x = 20)

    label_speed = Label(frame_teal_bar3, text="Speed: ", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_speed.place(y = 8, x = 10)

    slider_speed_edit = Scale(frame_teal_bar3, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_speed_edit.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar4 = Frame(frame_card_editing, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar4.place(y = 340, x = 20)

    label_Stealth = Label(frame_teal_bar4, text="Stealth:", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_Stealth.place(y = 8, x = 10)

    slider_stealth_edit = Scale(frame_teal_bar4, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_stealth_edit.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    frame_teal_bar5 = Frame(frame_card_editing, bg = LIGHT_TEAL, width= TEAL_BAR_WIDTH, height= TEAL_BAR_HEIHGT)
    frame_teal_bar5.place(y = 450, x = 20)

    label_cunning = Label(frame_teal_bar5, text="Cunning:", fg = DARK_RED, font = (FONT_TYPE, 25), background= LIGHT_TEAL)
    label_cunning.place(y = 8, x = 10)

    slider_cunning_edit = Scale(frame_teal_bar5, from_=1, to=25, orient=HORIZONTAL, bg=LIGHT_TEAL, troughcolor=DARK_TEAL, bd= 0, highlightthickness=0, fg = DARK_RED)
    slider_cunning_edit.place(y=8, x = SLIDER_XAXIS, width= SLIDER_WIDTH, height= SLIDER_HEIHGT)

    entry_text = StringVar()
    entry_text.trace("w", enforce_limit)
    entry_name_edit = Entry(frame_card_editing, textvariable=entry_text, background= DARK_TEAL, fg = "white", font = (FONT_TYPE, 10), bd=3)
    entry_name_edit.place(y = 20, x = 450, width= 350, height= 30)  

    button_edditing_card_option1 = Button(frame_card_editing, image= monster_option1, width= 145, height= 213, command=chose_card1)
    button_edditing_card_option1.place(y = 65, x = 450)
    button_edditing_card_option1.image = monster_option1

    button_edditing_card_option2 = Button(frame_card_editing, image= monster_option2, width= 145, height= 213, command=chose_card2)
    button_edditing_card_option2.place(y = 65, x = 650)
    button_edditing_card_option2.image = monster_option2

    button_edditing_card_option3 = Button(frame_card_editing, image= monster_option3, width= 145, height= 213, command=chose_card3)
    button_edditing_card_option3.place(y = 300, x = 450)
    button_edditing_card_option3.image = monster_option3
    
    button_edditing_card_option4 = Button(frame_card_editing, image= monster_option4, width= 145, height= 213, command=chose_card4)
    button_edditing_card_option4.place(y = 300, x = 650)
    button_edditing_card_option4.image = monster_option4

    button_confirm = Button(frame_card_editing, text= "Confirm", fg = DARK_RED, bg=LIGHT_TEAL, font = (FONT_TYPE, 13), command= aditing_confirmation)
    button_confirm.place(y = 530, x = 20)

    button_cancel = Button(frame_card_editing, text="Cancel", fg = DARK_RED, font = (FONT_TYPE, 13), bg=LIGHT_TEAL, command= return_function)
    button_cancel.place(y = 530, x = 100)

    frame_mainpage.pack_forget()
    frame_card_preview.pack_forget()
    frame_card_editing.pack(fill=BOTH, expand=True)
    root.geometry("840x570")    

    if (card_id <= 7):
        messagebox.showerror("invalid card", "You can not edit one of the 7 original cards")
        return_function()

def output():
    
    with open('monster.json', 'r') as json_file:
        saved_json = json.load(json_file)

    label_output.config(text = (json.dumps(saved_json, indent=1)))

    frame_mainpage.pack_forget()
    frame_output.pack(fill = BOTH, expand = True)
    root.geometry("300x760")

def search_for_monster():
    global card_id

    card_to_search = entry_searchbar.get()

    for each in monsters:
        if (card_to_search == monsters[each]["monster_name"]):
            card_id = each
            card_preview()

cards_added = 0

is_picked = False

is_slot_8_free = True
is_slot_9_free = True
is_slot_10_free = True

card_id = 0

index = 1

root = Tk()
root.title ("Monster Catalogue")
root.geometry("840x570")

open_images()

monsters= {
    1 : {
        "monster_name": "Vexscream", 
        "image_id": monster_photo1,
        "strength": 1, 
        "speed": 6, 
        "stealth": 21, 
        "cunning": 19,
        "total_score": 47
    },
    2 : {
        "monster_name": "Dawnmirage", 
        "image_id": monster_photo2,
        "strength": 5, 
        "speed": 15, 
        "stealth": 18, 
        "cunning": 22,
        "total_score": 60
    },
    3 : {
        "monster_name": "Blazegolem", 
        "image_id": monster_photo3,
        "strength": 15, 
        "speed": 20, 
        "stealth": 23, 
        "cunning": 6,
        "total_score": 64
    }, 
    4 : {
        "monster_name": "Moldvine", 
        "image_id": monster_photo4,
        "strength": 21, 
        "speed": 18, 
        "stealth": 14, 
        "cunning": 5,
        "total_score": 58
    }, 
    5 : {
        "monster_name": "Vertexwing", 
        "image_id": monster_photo5,
        "strength": 19, 
        "speed": 13, 
        "stealth": 18, 
        "cunning": 2,
        "total_score": 53
    }, 
    6 : {
        "monster_name": "Froststep", 
        "image_id": monster_photo6,
        "strength": 14, 
        "speed": 14, 
        "stealth": 17, 
        "cunning": 4,
        "total_score": 49
    }, 
    7 : {
        "monster_name": "Wispghoul", 
        "image_id": monster_photo7,
        "strength": 17, 
        "speed": 19, 
        "stealth": 3, 
        "cunning": 2,
        "total_score": 41
    }
}

frame_mainpage = Frame(root, bg=DARK_TEAL)
frame_mainpage.pack(fill=BOTH, expand=True)

sort_cards()

frame_graytbox = Frame(frame_mainpage, bg = GRAY_COLOUR, width = 775, height = 220)
frame_graytbox.place(y = 10, x = 35)

label_maintitle = Label(frame_graytbox, text = "Monster Catalogue", fg = DARK_RED, font = (FONT_TYPE, 35), bg=GRAY_COLOUR)
label_maintitle.place(y = 5, x = 170)

button_main_exit = Button(frame_graytbox, text="Exit", fg = DARK_RED, font = (FONT_TYPE, 16), bg=RED, command= exit)
button_main_exit.place(y = 4, x = 715)

button_add= Button(frame_graytbox, text="Add", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command= adding_page)
button_add.place(y = 85, x = 120)

button_sort = Button(frame_graytbox, text="Sort", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command = incriment_index)
button_sort.place(y = 85, x = 345)

button_print = Button(frame_graytbox, text="Print", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command = output)
button_print.place(y = 85, x = 570)

entry_searchbar = Entry(frame_graytbox, text="search", fg = DARK_RED, font = (FONT_TYPE, 10), bg=GRAY_COLOUR)
entry_searchbar.place(y = 170, x = 40, width = 580, height = 30)

button_search = Button(frame_graytbox, text="Search", fg = DARK_RED, font = (FONT_TYPE, 13), bg=LIGHT_TEAL, command = search_for_monster)
button_search.place(y = 167, x = 640)

button_cardslot_1 = Button(frame_mainpage, image = monster_photo1, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_1)
button_cardslot_1.place(y = TOP_ROW_BUTTONS_YAXIS, x = 100)
button_cardslot_1.image = monster_photo1

button_cardslot_2 = Button(frame_mainpage, image= monster_photo2, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_2)
button_cardslot_2.place(y = TOP_ROW_BUTTONS_YAXIS, x = 240)
button_cardslot_2.image = monster_photo2

button_cardslot_3 = Button(frame_mainpage, image= monster_photo3, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_3)
button_cardslot_3.place(y = TOP_ROW_BUTTONS_YAXIS, x = 380)
button_cardslot_3.image = monster_photo3

button_cardslot_4 = Button(frame_mainpage, image= monster_photo4, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_4)
button_cardslot_4.place(y = TOP_ROW_BUTTONS_YAXIS, x = 520)
button_cardslot_4.image = monster_photo4

button_cardslot_5 = Button(frame_mainpage, image= monster_photo5, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_5)
button_cardslot_5.place(y = TOP_ROW_BUTTONS_YAXIS, x = 660)
button_cardslot_5.image = monster_photo5

button_cardslot_6 = Button(frame_mainpage, image= monster_photo6, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_6)
button_cardslot_6.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 100)
button_cardslot_6.image = monster_photo6

button_cardslot_7 = Button(frame_mainpage, image= monster_photo7, height = CARD_HEIGHT, width = CARD_WIDTH, command= id_7)
button_cardslot_7.place(y = BOTTOM_ROW_BUTTONS_YAXIS, x = 240)
button_cardslot_7.image = monster_photo7

frame_card_preview = Frame(root, bg=DARK_TEAL)

image_placeholder = "PLACEHOLDER.png"
image_monster = Image.open(image_placeholder)
image_monster = image_monster.resize((PREVIEW_RESIZE_WIDTH,PREVIEW_RESIZE_HEIGHT), Image.LANCZOS)
image_monster = ImageTk.PhotoImage(image_monster)
label_preview_image = Label(frame_card_preview, image=image_monster, width=320, height=360)
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

label_preview_name = Label(frame_card_preview, text = "placeholder", fg = DARK_RED, font = (FONT_TYPE, 14), bg=LIGHT_TEAL)
label_preview_name.place(y = 385, x = 197)

button_edit = Button(frame_card_preview, text="Edit", fg = DARK_RED, font = (FONT_TYPE, 18), bg=LIGHT_TEAL, command = edit_cards)
button_edit.place(y = 550, x = 330)

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

button_card_exit = Button(frame_card_confirmation, text="Exit", fg = DARK_RED, font = (FONT_TYPE, 16), bg=RED, command= exit)
button_card_exit.place(y = 12, x = 380)

button_accept = Button(frame_card_confirmation, text="Accept", fg = DARK_RED, font = (FONT_TYPE, 16), bg=LIGHT_TEAL, command= save_card)
button_accept.place(y = 600, x = 350)

frame_output = Frame(root, bg=DARK_TEAL)

label_output = Label(frame_output, text = "placeholder", fg = "white", font = (FONT_TYPE, 5), bg="black")
label_output.pack()

button_return = Button(frame_output, text="Return", fg = DARK_RED, font = (FONT_TYPE, 10), bg=LIGHT_TEAL, command= return_function)
button_return.place(y = 20, x = 20)

frame_card_editing = Frame(root, bg=DARK_TEAL)

root.mainloop()