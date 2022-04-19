from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    if snake.move() is False or snake.tail_collision() is True:
        scoreboard.game_over()
        game_over = True
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

screen.exitonclick()
