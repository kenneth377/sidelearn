import turtle

rect = {"x":50,
         "y":200,
         "posx":30,
         "posy":50
         }

turtle.penup()
turtle.goto(rect["posx"],rect["posy"])
turtle.pendown()
# turtle.speed(20000)
turtle.forward(rect["x"])
turtle.right(90)
turtle.forward(rect["y"])
turtle.right(90)
turtle.forward(rect["x"])
turtle.right(90)
turtle.forward(rect["y"])