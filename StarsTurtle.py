import turtle
import math

bob = turtle.Turtle()
bob.color("blue","pink")
bob.speed(10)

bob.begin_fill()
for i in range(5):
    bob.forward(math.floor(283))
    bob.left(143.5)
bob.end_fill()


import turtle

bob2 = turtle.Turtle()
bob2.color("green","pink")
bob2.speed(10)

bob2.begin_fill()
for i in range(5):
    bob2.forward(-283)
    bob2.left(-143.5)
bob2.end_fill()