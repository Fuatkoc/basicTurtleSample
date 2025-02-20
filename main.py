import turtle
import random
from random import randint

my_screen=turtle.Screen()
my_screen.bgcolor("light blue")
my_screen.title("Catch The Turtle")

#border of area
ymin,ymax=-345,345
xmin,xmax=-345,345

turtle_default=turtle.Turtle()
turtle1=turtle.Turtle()
turtle_instance=turtle.Turtle()
turtle_instance.speed(5)
turtle_default.speed(5)
#turtle_instance.color()
turtle_instance.up()
turtle_default.up()
turtle_default.goto(345,345)
turtle_default.down()
for i in range(4):
    turtle_default.right(90)
    turtle_default.forward(345*2)


def forward():
    """Kaplumbağa sınırı geçerse otomatik olarak geri gider."""
    xnow = turtle_instance.xcor()
    ynow = turtle_instance.ycor()

    # Turtle'ı ileri hareket ettir
    turtle_instance.forward(10)

    # Yeni pozisyonu kontrol et
    new_x = turtle_instance.xcor()
    new_y = turtle_instance.ycor()

    # Eğer X veya Y sınırını geçerse otomatik olarak geri git
    if new_x < xmin or new_x > xmax or new_y < ymin or new_y > ymax:
        turtle_instance.backward(10)  # Sınıra çarpınca geri git

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