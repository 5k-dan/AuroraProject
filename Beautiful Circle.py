import turtle
turtle.bgcolor("light blue")
turtle.pensize(2.5)
turtle.speed(0.5)
colors = ["red", "blue", "orange", "green"]

for x in range(9):
    for i in colors:
        turtle.color(i)
        turtle.circle(150)
        turtle.left(193.2)
turtle.mainloop()