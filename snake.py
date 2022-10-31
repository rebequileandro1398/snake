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

#Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

#Head of the snake
head = turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Body of the snake
segment = []

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

        #Random food
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        #Growing body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        segment.append(new_segment)

        #Body movement
    totalSegment = len(segment)
    for i in range(totalSegment -1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x,y)

    if totalSegment > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
    movement()
    time.sleep(stay)