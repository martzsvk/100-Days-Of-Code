from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


# setting up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# initializing classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

# while loop to move our snake
playing = True
while playing:
    # updating screen
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.collision()
        snake.extend()
        scoreboard.up_score()

    # detect collision with wall
    if snake.snake_head.xcor() > 299 or snake.snake_head.xcor() < -299 or snake.snake_head.ycor() > 299 or snake.snake_head.ycor() < -299:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()