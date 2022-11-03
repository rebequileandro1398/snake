#!/usr/bin/env python
import turtle
import time
import random


#Delay
stay = 0.1

#Colors
food_colors = ["#CA0000", "#C6E105", "#5505AF", "#E50C79", "#FFF300", "#CACACA", "#7AD35D"]
snake_head_color = "#51C669"
snake_body_colo_one = "#4E9C56"
snake_body_colo_two = "#27712F"
last_segment_color = snake_body_colo_one

#Score
current_score = 0
high_score = 0

#Window settings
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#Limit window
line = turtle.Turtle()
line.goto(-300, 240)
line.speed(2)
line.pencolor("white")
line.pensize(2)
line.goto(300, 240)
line.hideturtle()

#Create elements
def create_element(color, shape, goto): 
    element = turtle.Turtle()
    element.speed(0)
    element.color(color)
    element.shape(shape)
    element.penup()
    element.goto(goto["x"], goto["y"])
    return element

#Food
food = create_element(
    food_colors[random.randint(0, 6)], 
    "circle", 
    {
        "x": 0, 
        "y": 100
    } 
    )

#Score
score = create_element("white",None , {"x": 0, "y": 255})
score.hideturtle()
score.write("Score: 0    High Score: 0", 
    align="center", font=("Courier", 24, "normal"))
def updateScore():
    score.clear()
    score.write("Score: {}    High Score: {}".format(current_score, high_score), 
        align="center", font=("Courier", 24, "normal"))

#Head of the snake
head = create_element(snake_head_color,"square" , {"x": 0, "y": 0})
head.direction = "stop"

#Body of the snake
segment = []

#Movement
def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left":
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

#Collisions
def game_over():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    for seg in segment:
        seg.hideturtle()
    segment.clear()
    updateScore()

#Controls
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

#Main loop
while True:
    wn.update()
    #Collisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 220 or head.ycor() < -280:
        current_score = 0
        game_over()
    for seg in segment:
        if seg.distance(head) < 19:
            current_score = 0
            game_over()

    #Food
    if head.distance(food) < 20:
        #Random food
        x = random.randint(-280, 280)
        y = random.randint(-280, 210)
       
        food.color(food_colors[random.randint(0, 6)])
        food.goto(x, y)

        #Growing body
        if last_segment_color == snake_body_colo_one:
              last_segment_color = snake_body_colo_two
        else: last_segment_color = snake_body_colo_one
        new_segment = create_element(last_segment_color,"square" , {"x": 0, "y": 0})
        segment.append(new_segment)
     
        #Update score
        current_score += 5
        if current_score > high_score:
            high_score = current_score
        updateScore()

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
