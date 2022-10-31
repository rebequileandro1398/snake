import turtle
import time

#delay
stay = 0.1

#window settings
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#head of the snake
head = turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

#functions
def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#main loop
while True:
    wn.update()
    mov()
    time.sleep(stay)