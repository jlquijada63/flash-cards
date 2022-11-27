from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

# check if the file "words_to_learn" exists using catching exceptions

try:
    df = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('./data/french_words.csv')

to_learn = df.to_dict(orient='records')
current_card = {}


def on_press_known_button():
    next_card()
    remove_known_words()


# ---------------------------- REMOVE KNOWN WORDS ------------------------------#

def remove_known_words():
    to_learn.remove(current_card)
    new_df = pandas.DataFrame(to_learn)
    new_df.to_csv('./data/words_to_learn.csv', index=False)



# ---------------------------- FLIP THE IMAGE OF THE CANVAS ---------------------#



def flip_card():

    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=current_card["English"], fill="white")
    canvas.itemconfigure(canvas_image, image=card_back_img)


# --------------------------- GENERATE A RANDOM WORD ---------------------------#


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(card_title, text='French', fill="black")
    canvas.itemconfigure(card_word, text=current_card["French"], fill='black')
    canvas.itemconfigure(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)



# ---------------------------- SETUP GUI ---------------------------------------#



window = Tk()
window.title("Flash-Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=("Arial", 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=("Arial", 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

check_image = PhotoImage(file='./images/right.png')
known_button = Button(bg=BACKGROUND_COLOR, image=check_image, highlightthickness=0, command=on_press_known_button)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(bg=BACKGROUND_COLOR, image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Call the function next_card the first time the program charges to show the first flash-card
next_card()

window.mainloop()
