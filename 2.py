import turtle
amy= turtle.Turtle()
amy.color("cyan")
amy.speed(0)
colors=["green","white","orange","navy","lightblue","red","purple","red","navy"]
def draw_square(color):
    for side in range(4):
        amy.forward(100)
        amy.right(90)
        for side in range(4):
            amy.forward(50)
            amy.right(90)

amy.penup()
amy.back(40)
amy.pendown()
def new_f():
    for color in colors:
        amy.color(color)
        draw_square(colors)
        amy.forward(50)
        amy.left(45)
amy.hideturtle()
new_f()