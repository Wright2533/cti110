import turtle
import random

wn = turtle.Screen()
wn.bgcolor("cyan")




# assign a name to turtle
t = turtle.Turtle()
t.speed(15)

# create a list of colours
sfcolor = ["white", "blue", "purple", "grey", "magenta"]

# function to create snowflake
def snowflake(size):
# move the pen into starting position
    t.penup()
    t.forward(10*size)
    t.left(45)
    t.pendown()
    t.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        t.left(45)
    

# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            t.forward(10.0*size/3)
            t.backward(10.0*size/3)
            t.right(45)
        t.left(90)
        t.backward(10.0*size/3)
        t.left(45)
    t.right(90) 
    t.forward(10.0*size)

# loop to create 1 Snowflake
for i in range(1):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    t.penup()
    t.goto(x, y)
    t.pendown()
    snowflake(sf_size)
