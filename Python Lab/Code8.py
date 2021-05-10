import turtle
turtle.speed(3)
turtle.penup()

height = 5
width = 5

for i in range(height):
    for j in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(width*20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

    
