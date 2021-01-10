from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()

window.title("Spanish Flashcards")
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

canvas = Canvas(width=800,height=526, bg=BACKGROUND_COLOR)
my_image = PhotoImage(file="./images/card_front.png")

canvas.create_image(405,268,image=my_image)
canvas.grid(column=0,row=0,columnspan=2)

language = canvas.create_text(400,150,fill="black",font="Verdana 40 italic",
                        text="Spanish")
translate = canvas.create_text(400,263,fill="black",font="Arial 60 bold",
                        text="Word")

tick = PhotoImage(file="./images/right.png")
button_right = Button(image=tick,highlightthickness=0)
button_right.grid(column=0,row=2)

wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong,highlightthickness=0)
button_wrong.grid(column=1,row=2)














window.mainloop()
