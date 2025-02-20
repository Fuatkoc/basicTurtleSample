import turtle
import random
from random import randint

my_screen=turtle.Screen()
my_screen.bgcolor("light blue")
my_screen.title("Catch The Turtle")

#border of area
ymin,ymax=-200,200
xmin,xmax=-200,200

turtle1=turtle.Turtle()
turtle_instance=turtle.Turtle()
#turtle_instance.color()

def forward():
    xnow = turtle_instance.xcor()
    ynow = turtle_instance.ycor()

    turtle_instance.forward(30)
    new_x = turtle_instance.xcor()
    new_y = turtle_instance.ycor()

    if not(xmin<= xnow <=xmax and ymin<=ynow <=ymax):
        turtle_instance.backward(30)



def right():
    turtle_instance.right(10)

def left():
     turtle_instance.left(10)
def clear():
    turtle_instance.clear()
def backtopoint():
    turtle_instance.up()
    turtle_instance.goto(0,0)
    turtle_instance.down()





turtle.listen()
turtle.onkeypress(backtopoint,"m")
turtle.onkeypress(clear,"r")
turtle.onkeypress(forward,"Up")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")




while True:
    turtle1.forward(randint(10,50))
    turtle1.right(randint(10,60))
    turtle1.left(randint(10, 60))




turtle.mainloop()