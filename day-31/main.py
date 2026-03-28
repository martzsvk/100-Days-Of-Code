from tkinter import *
import pandas

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

# Functions

position = 0
# Creating dict for words to learn
words_to_learn = {"French": [],
                  "English": []}


# Just change to French - nothing else
def change_french():
    global position
    # Changing back to card_front.png
    front_card.itemconfig(card_front, image=front_image)

    # Trying words_to_learn if user already "played"
    try:
        # Opening words_to_learn.csv
        words_to_learn_data = pandas.read_csv("./words_to_learn.csv")
        words_to_learn_dict = pandas.DataFrame(words_to_learn_data)
        front_card.itemconfig(language_label, text="French", font=(FONT, 35, "italic"), fill="black")
        front_card.itemconfig(word_label, text=f"{words_to_learn_dict["French"][position]}", font=(FONT, 45, "bold"),
                              fill="black")

    except (FileNotFoundError, IndexError, KeyError):
        # Changing language and word label to french
        front_card.itemconfig(language_label, text="French", font=(FONT, 35, "italic"), fill="black")
        front_card.itemconfig(word_label, text=f"{french_dict["French"][position]}", font=(FONT, 45, "bold"),
                              fill="black")



# Change to French
def change_words_right():
    global position
    # Changing back to card_front.png
    front_card.itemconfig(card_front, image=front_image)

    # Trying words_to_learn if user already "played"
    try:
        # Opening words_to_learn.csv
        words_to_learn_data = pandas.read_csv("./words_to_learn.csv")
        words_to_learn_dict = pandas.DataFrame(words_to_learn_data)
        front_card.itemconfig(language_label, text="French", font=(FONT, 35, "italic"), fill="black")
        front_card.itemconfig(word_label, text=f"{words_to_learn_dict["French"][position + 1]}", font=(FONT, 45, "bold"), fill="black")
        position += 1
        return position

    except (FileNotFoundError, IndexError, KeyError):
        # Changing language and word label to french
        front_card.itemconfig(language_label, text="French", font=(FONT, 35, "italic"), fill="black")
        front_card.itemconfig(word_label, text=f"{french_dict["French"][position + 1]}", font=(FONT, 45, "bold"), fill="black")
        position += 1
        return position



# Change to English
def change_words_wrong():
    global position
    # Changing front card image to card_back.png
    front_card.itemconfig(card_front, image=back_image)

    # Trying words_to_learn if user already "played"
    try:

        # Opening words_to_learn.csv
        words_to_learn_data = pandas.read_csv("./words_to_learn.csv")
        words_to_learn_dict = pandas.DataFrame(words_to_learn_data)
        front_card.itemconfig(language_label, text="English", font=(FONT, 35, "italic"), fill="black")
        front_card.itemconfig(word_label, text=f"{words_to_learn_dict["English"][position]}",
                              font=(FONT, 45, "bold"), fill="black")

        window.after(ms=1500, func=change_french)
        position += 1
        return position

    except (FileNotFoundError, IndexError, KeyError):
        # Changing language and word label to english
        front_card.itemconfig(language_label, text="English", font=(FONT, 35, "italic"), fill="white")
        front_card.itemconfig(word_label, text=f"{french_dict["English"][position]}", font=(FONT, 45, "bold"), fill="white")

        # Appending words which the user didn't know
        words_to_learn["French"].append(french_dict["French"][position])
        words_to_learn["English"].append(french_dict["English"][position])

        window.after(ms=1500, func=change_french)
        position += 1
        return position




# Window
window = Tk()
# Configuring the window
window.config(width=1200, height=600, background=BACKGROUND_COLOR)
window.title("Flashy learny language project")
# Making the window non-resizable
window.resizable(width=False, height=False)


# Canvas for front card
front_card = Canvas(width=1000, height=600, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_front = front_card.create_image(500, 335, image=front_image)
front_card.grid(row=1, column=1, columnspan=2)


# Opening French.csv
french_data = pandas.read_csv("./data/french_words.csv")
# Making dictionary from french_data
french_dict = pandas.DataFrame.to_dict(french_data)

# Labels
language_label = front_card.create_text(500, 190, text="")
word_label = front_card.create_text(500, 375, text="")


# Right button
right_image = PhotoImage(file="./images/right.png")
right = Button(image=right_image, background=BACKGROUND_COLOR, highlightthickness=0, command=change_words_right)
right.grid(row=2, column=2, pady=25)


# Wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image, background=BACKGROUND_COLOR, highlightthickness=0, command=change_words_wrong)
wrong.grid(row=2, column=1, pady=25)

change_french()

window.mainloop()

# Creating CSV file from dict words_to_learn
df = pandas.DataFrame(words_to_learn)
df.to_csv("words_to_learn.csv", index=False)