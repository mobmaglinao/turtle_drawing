import turtle
import random

display = turtle.Screen()

mikey = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

# set colors for turtle
mikey.color('green', 'green')

# set pen width, speed, shape
mikey.width(3)
mikey.shape('turtle')
mikey.speed(4)

def rectangle():
    mikey.forward(100)
    mikey.left(90)
    mikey.forward(100)
    mikey.left(90)
    mikey.forward(100)
    mikey.left(90)
    mikey.forward(100)
    mikey.left(90)

def triangle(edge=20):
    mikey.forward(edge)
    mikey.right(120)
    mikey.forward(edge)
    mikey.right(120)
    mikey.forward(edge)
    mikey.right(120)
    mikey.forward(edge)
    mikey.right(120)


rectangle()

mikey.penup()
mikey.forward(25)
mikey.left(90)
mikey.forward(30)
mikey.left(180)
mikey.pendown()
mikey.circle(25, 180)
mikey.penup()
mikey.forward(15)
mikey.left(90)
mikey.forward(14.5)
mikey.pendown()
triangle()
mikey.penup()
mikey.forward(63)
mikey.pendown()
mikey.right(60)
mikey.forward(30)
mikey.circle(20)
mikey.circle(40)
mikey.penup()
mikey.left(180)
mikey.forward(100)
mikey.right(180)
mikey.pendown()
mikey.circle(20)
mikey.circle(40)
mikey.penup()
mikey.forward(25)
mikey.right(90)
mikey.forward(30)
mikey.left(90)
mikey.pendown()
mikey.circle(10)
mikey.penup()
mikey.forward(50)
mikey.pendown()
mikey.circle(10)
mikey.penup()
mikey.forward(50)

display.mainloop()

##### notes from tutorial video
# use keyboard to move turtle
# def up():
#     tim.setheading(90)
#     tim.forward(100)
# def down():
#     tim.setheading(270)
#     tim.forward(100)
# def left():
#     tim.setheading(180)
#     tim.forward(100)
# def right():
#     tim.setheading(0)
#     tim.forward(100)
#
# turtle.listen()
#
# turtle.onkey(up, 'Up')
# turtle.onkey(down, 'Down')
# turtle.onkey(left, 'Left')
# turtle.onkey(right, 'Right')

#fill in shape with color
# tim.begin_fill()
# tim.circle(50)
# tim.end_fill()

#for loop to make a rectangle
# mikey.color('green', 'green')
# mikey.begin_fill()
# for rectangle in range(4):
#     mikey.forward(100)
#     mikey.right(90)
# mikey.end_fill()


