from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
s_food = Food()
g_score = Score()

g_snake = Snake("white")


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

play_on = True


while play_on:
    screen.update()
    g_snake.move()
    time.sleep(0.1)
    if g_snake.head.distance(s_food) < 20:
        s_food.refresh()
        g_score.update()
        g_snake.extends()
    screen.update()
    screen.listen()
    screen.onkey(fun = g_snake.up, key = "Up")
    screen.onkey(fun = g_snake.down, key = "Down")
    screen.onkey(fun = g_snake.left, key = "Left")
    screen.onkey(fun = g_snake.right, key = "Right")
    if g_snake.head.xcor() > 290 or g_snake.head.xcor() < -290 or g_snake.head.ycor() < -290 or g_snake.head.ycor() > 290:
        g_score.game_over()
        play_on = False
    if g_snake.collide():
        g_score.game_over()
        play_on = False
screen.exitonclick()