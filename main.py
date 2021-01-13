from tkinter import *
from card import Card

BACKGROUND_COLOR = "#B1DDC6"

#---------------------------------------
# IMPORTED TABLE DATA

window = Tk()
card = Card()

window.title("🇪🇸 Spanish Flashcards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

w=900
h=800

window.minsize(width=w, height=h)
window.maxsize(width=w, height=h)

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

def guess():
    if card.remember():
        global flip_timer
        window.after_cancel(flip_timer)
        print(f"Tries = {card.tries}")
        print(f"Score = {card.score}")
        default()
        card.next_card()
        flip_timer = window.after(3000,flip)

def forgot():
    if card.forgot():
        global flip_timer
        window.after_cancel(flip_timer)
        print("hi")
        print(f"Tries = {card.tries}")
        print(f"Score = {card.score}")
        canvas.itemconfig(translate, text=card.spanish, fill="black")
        card.next_card()
        flip_timer = window.after(3000,flip)

def flip():
    canvas.itemconfig(language, text='English', fill="white")
    canvas.itemconfig(translate, text=card.english, fill="white")
    canvas.itemconfig(background, image=back)

def default():
    canvas.itemconfig(language, text='🇪🇸 Spanish ', fill="black")
    canvas.itemconfig(translate, text=card.spanish, fill="black")
    canvas.itemconfig(background, image=my_image)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")

background = canvas.create_image(405,268,image=my_image)
canvas.grid(column=0,row=0,columnspan=2)

language = canvas.create_text(400,150,fill="black",font="Verdana 40 italic",
                        text="🇪🇸 Spanish ")
translate = canvas.create_text(400,263,fill="black",font="Arial 60 bold",
                        text=f"{card.spanish}")

print(translate)

tick = PhotoImage(file="./images/right.png")
button_right = Button(image=tick,highlightthickness=0,command=guess)
button_right.grid(column=0,row=2)

wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong,highlightthickness=0, command=forgot)
button_wrong.grid(column=1,row=2)



window.mainloop()
