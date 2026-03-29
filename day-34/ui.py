from tkinter import *
from quiz_brain import QuizBrain

# Constants
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text=f"Score: 0", font=("Arial", 15, "italic"), fg="white", background=THEME_COLOR)
        self.score.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="", width=280, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40, padx=40)

        right_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_image, command=self.true_pressed, highlightthickness=0)
        self.right_button.grid(row=3, column=1)

        self.wrong_button = Button(image=false_image, command=self.false_pressed, highlightthickness=0)
        self.wrong_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Your score was {self.quiz.score}/{self.quiz.question_number}\n"
                                                          f"Thank you for playing:)")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0)

        self.window.after(ms=1000, func=self.get_next_question)







