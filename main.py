from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# --------------------------- GENERATE A RANDOM WORD ---------------------------#

df = pandas.read_csv('./data/french_words.csv')
to_learn = df.to_dict(orient='records')


def next_card():

    current_card = random.choice(to_learn)
    canvas.itemconfigure(card_title, text='French')
    canvas.itemconfigure(card_word, text=current_card["French"])

# ---------------------------- SETUP GUI ---------------------------------------#

window = Tk()
window.title("Flash-Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=("Arial", 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=("Arial", 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

check_image = PhotoImage(file='./images/right.png')
known_button = Button(bg=BACKGROUND_COLOR, image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(bg=BACKGROUND_COLOR, image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Call the function next_card the first time the program charges to show the first flash-card
next_card()

window.mainloop()
