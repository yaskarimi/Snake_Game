from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
score.clear()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    score.score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 16:
        score.increase()
        food.refresh()
        snake.extend()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
