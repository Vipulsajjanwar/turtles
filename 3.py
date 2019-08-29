import turtle
t= turtle.Turtle()
t.color("red")

for side in range(100):
    t.forward(10*side)
    t.left(360/3)
