import turtle
import random

genx = random.randrange(-200,200)
geny = random.randrange(-200,200)
r = genx
x = genx
y = geny
cenx =genx
ceny = 0
cens = 5

world = turtle.Screen()
world.setup(900, 500, 0, 0)
world.title("docking test")
world.bgcolor('black')

al = turtle.Turtle()
al.hideturtle()
al.color('white')
al.penup()
al.speed(0)

ma = turtle.Turtle()
ma.hideturtle()
ma.color('white')
ma.penup()
ma.speed(0)

def docking():
    cr = turtle.Turtle()
    cr.hideturtle()
    cr.color('gray')
    cr.speed(0)
    cr.penup()
    cr.setpos(0,250)
    cr.seth(270)
    cr.pendown()
    cr.forward(500)
    cr.penup()
    cr.setpos(450,0)
    cr.seth(180)
    cr.pendown()
    cr.forward(900)
    
    def left():
      global cenx  
      global x
      x = x-10
      cenx = cenx-10
    def right():
      global cenx
      global x
      x = x+10
      cenx = cenx+10
    def up():
      global y
      global ceny
      y = y+10
      ceny = ceny+10
    def down():
      global y
      global ceny
      y = y-10
      ceny = ceny-10
    for i in range(100):
        global r
        global x
        global cens
        ma.setx(cenx)
        ma.sety(ceny)
        al.setx(x)
        al.sety(y)
        al.pendown()
        al.seth(90)
        al.clear()
        ma.clear()
        al.circle(r)
        ma.dot(cens, 'white')
        al.penup()
        r = r+1
        x = x+1
        if cens <= 10:
            cens+0.5
        turtle.onkey(left, 'Left')
        turtle.onkey(right, 'Right')
        turtle.onkey(up, 'Up')
        turtle.onkey(down, 'Down')
        turtle.listen()
        turtle.delay(50)

docking()

