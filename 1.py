import turtle
amy= turtle.Turtle()
amy.color("black")
amy.speed(1000)
def draw_square():
    for side in range(1):
        amy.forward(100)
        amy.left(90)
        for side in range(1):
            amy.forward(50)
            amy.left(90)

amy.penup()
amy.back(20)
amy.pendown()

for square in range(100):
    draw_square()
    amy.forward(5)
    amy.left(5)
amy.hideturtle()
print(turtle)