import turtle

t = turtle
wn = turtle.Screen()
wn.bgcolor ("green")


# Initials
t.color('red')
t.pensize(10)

# "S"
t.forward(45)
for y in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
    t.left(10)
    t.forward (5)
for y in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]:
    t.right(10)
    t.forward (5)

t.penup()           # Pen up
t.forward(60)
t.left(70)
t.pendown()         # Pen Down


# "W"
t.right(65)
t.forward(100)
t.left(130)
t.forward(70)
t.right(130)
t.forward(70)
t.left(130)
t.forward(100)
t.hideturtle        # Made the letter W

















