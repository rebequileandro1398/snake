import turtle
import time
import random
#Delay
stay = 0.1

#Window settings
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#Head of the snake
head = turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

#Movement
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

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

#Controls
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

#Main loop
while True:
    wn.update()
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
    movement()
    time.sleep(stay)