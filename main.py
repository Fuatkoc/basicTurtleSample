import turtle
import random
from random import randint


# Ekranda yazı yazdıran turtle oluştug
pen = turtle.Turtle()

# Yazıyı yazdırmak için fonksiyon
pen.write("Score:", font=("Arial", 16, "normal"))




my_screen = turtle.Screen()
my_screen.bgcolor("light blue")
my_screen.title("Catch The Turtle")

# Sınır ayarları
ymin, ymax = -350, 350
xmin, xmax = -600, 600

turtle_default = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle_instance = turtle.Turtle()

turtle_instance.speed(5)
turtle_default.speed(5)
turtle1.speed(3)
turtle_instance.up()
turtle_default.up()

turtle_default.goto(600, 350)
turtle_default.down()

# Sınır çizgisi
for i in range(2):
    turtle_default.right(90)
    turtle_default.forward(350 * 2)
    turtle_default.right(90)
    turtle_default.forward(600 * 2)


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
    turtle_instance.goto(0, 0)
    turtle_instance.down()

score=0
turtle.listen()
turtle.onkeypress(backtopoint, "m")
turtle.onkeypress(clear, "r")
turtle.onkeypress(forward, "Up")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")

# Başlangıç konumu
turtle1.up()
turtle1.goto(100, 100)  # turtle1'in başlangıç noktasını belirledik.

# Sonsuz döngü ile hareket
while True:
    turtle1.forward(randint(10, 50))  # Sınırda değilse, ileri git

    # Yeni pozisyonu kontrol et
    new_x1 = turtle1.xcor()  # Şu anki x pozisyonu
    new_y1 = turtle1.ycor()  # Şu anki y pozisyonu

    # Eğer X veya Y sınırını geçerse, geri git
    if new_x1 < xmin or new_x1 > xmax or new_y1 < ymin or new_y1 > ymax:
        turtle1.backward(50)  # Sınıra çarpınca geri git
        turtle1.right(90)  # Yönünü değiştir (90 derece)

    # Yön değişikliği yapma komutları
    turtle1.right(randint(10, 50))  # Sağ dön
    turtle1.left(randint(10, 50))  # Sol dön

    # Mesafe sıfır olduğunda turtle1'i sıfır noktasına taşı
    distance = turtle1.distance(turtle_instance)
    if distance < 50:
        """global score"""
        score=score+1
        print("Mesafe sıfır, turtle1 sıfır noktasına taşındı.")
        turtle1.goto(0, 0)  # Turtle1'i sıfır noktasına taşı
