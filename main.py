from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- SETUP GUI ---------------------------------------#

window = Tk()
window.title("Flash-Card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text='Title', font=("Arial", 40, 'italic'))
canvas.create_text(400, 263, text='word', font=("Arial", 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

check_image = PhotoImage(file='./images/right.png')
known_button = Button(bg=BACKGROUND_COLOR, image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(bg=BACKGROUND_COLOR, image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

window.mainloop()
