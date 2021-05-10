import turtle
turtle.speed(1)

# Spiral
for i in range(11):
        turtle.forward(100 - i*10)
        turtle.left(90)


turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()

# Circle
for i in range(270):
        turtle.forward(1)
        turtle.left(1)


turtle.hideturtle()
