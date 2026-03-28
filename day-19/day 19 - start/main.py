from turtle import Turtle,Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def cleaning():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(cleaning, "c")
screen.exitonclick()