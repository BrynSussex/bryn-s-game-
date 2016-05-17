# John attempting to fix key delays

import turtle
import time
import random
import math

# DEFAULT POSITIONS
top_pos = 200,75
middle_sta1_pos = 250, -150
docking_layer_1_pos = 300, 0

# setup stations
s = {
        'sta1': {'key': 'a', 'pos':[200,75]},
        'sta2': {'key': 'b', 'pos':[-300,45]},
        'sta3': {'key': 'c', 'pos':[-100,-200]},
    }

def rect(t, *args):
    """rect(t, w, h): Draw a rectangle of width w, height h
       using turtle t.
       If called as rect(t, x, y, w, h) move to position (x,y)
       before drawing the rectangle."""
    if len(args) == 4:
        x, y, w, h = args
        t.penup()
        t.setpos(x,y)
        t.seth(0)
        t.pendown()
    elif len(args) == 2:
        w, h = args
    else:
        raise RuntimeError("rect(t, w, h) or rect(t, x, y, w, h)")
    draw_rect(t, w, h)
    
def draw_rect(t, w, h):
    """Draw a rectangle of width w, height h,
       using turtle t, at the current position."""
    for i in range (2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)

def dashed_line(t, num_dashes, dash_len, gap_len):
    """Draws a dashed line

        t: The turtle
        num_dashes: How many dashes to draw
        line_len: The length of each dash
        gap_len: The gap between the dashes
    """
    for i in range(num_dashes):
        t.forward(gap_len)
        t.pendown()
        t.forward(dash_len)
        t.penup()    

def turn_and_go(t, dest):
    x,y = s[dest]['pos']
    t.seth(t.towards(x,y))
    t.goto(x,y)

def planet_layer():
    turtle.clearscreen()
    screen_setup()
    
    pla = turtle.Turtle()
    pla.hideturtle()
    pla.penup()
    pla.color('white')
    pla.speed(0)
    pla.setpos(35,0)
    pla.seth(90)
    pla.pendown()
    pla.circle(35)
    
    sta1 = turtle.Turtle()
    sta1.hideturtle()
    sta1.resizemode("user")
    sta1.shapesize(1, 1, 1)
    sta1.color('white')
    sta1.speed(0)
    sta1.penup()
    sta1.shape('circle')
    sta1.setpos(90,0)
    sta1.seth(90)
    sta1.showturtle()
    sta1.speed(1)
    
    while True:
        sta1.circle(90)
    
    
def top_layer():
    turtle.clearscreen()
    screen_setup()
    stations()
    sp = turtle.Turtle()
    sp.color('white')
    sp.penup()
    
    global top_pos
    sp.setpos(top_pos)
    sp.showturtle()
    sp.speed(1)
        
    def sta1():
        turn_and_go(sp, 'sta1')
    def sta2():
        turn_and_go(sp, 'sta2')
    def sta3():
        turn_and_go(sp, 'sta3')
        
    def zoom1():
        global top_pos
        top_pos = sp.pos()
        global middle_sta1_pos
        middle_sta1_pos = 250,-150
        if sp.pos() == (200,75):
            middle_layer_sta1()
        else:
            zoom()
    turtle.onkey(sta1, 'a')
    turtle.onkey(sta2, 'b')
    turtle.onkey(sta3, 'c')
    turtle.onkey(zoom1, '=')
    turtle.listen()


def middle_layer_sta1():
    time.sleep(0.5)
    turtle.clearscreen()
    screen_setup()
    station_1()
    sp2 = turtle.Turtle()
    sp2.color('white')
    sp2.penup()
    sp2.speed(0)
    global middle_sta1_pos
    sp2.setpos(middle_sta1_pos)
    sp2.seth(90)
    sp2.showturtle()
    speed = (10)
    def turnleft():
        sp2.left(30)
    def turnright():
        sp2.right(30)
    def forward():
        sp2.forward(speed)
    def backward():
        sp2.backward(speed)
    def zoom1():
        global middle_sta1_pos
        middle_sta1_pos = sp2.pos()
        if sp2.xcor() > -162 and sp2.xcor() < -98 and sp2.ycor() > -112 and sp2.ycor() < -64:
            docking_layer()            
            
    turtle.onkey(forward, 'Up')
    turtle.onkey(turnleft, 'Left')
    turtle.onkey(turnright, 'Right')
    turtle.onkey(backward, 'Down')
    turtle.onkey(top_layer, '-')
    turtle.onkey(zoom1,'=')
    turtle.listen()

    for i in range(1000):
        x = random.randrange(-250, 450)
        h = random.randrange(220, 340)
        ship = turtle.Turtle()
        ship.hideturtle()
        ship.color('blue')
        ship.penup()
        ship.speed(0)
        ship.setpos(x, 260)
        ship.showturtle()
        ship.speed(1)
        ship.seth(h)
        ship.forward(1000)
        if sp2.xcor() > -162 and sp2.xcor() < -98 and sp2.ycor() > -112 and sp2.ycor() < -64:
            break
        
         

      
def zoom():
    time.sleep(0.5)
    turtle.clearscreen()
    screen_setup()
    sp2 = turtle.Turtle()
    sp2.color('white')
    sp2.penup()
    sp2.speed(0)
    sp2.setpos(middle_sta1_pos)
    sp2.seth(90)
    sp2.showturtle()
    speed = (10)
    b = 2
    def turnleft():
        sp2.left(30)
    def turnright():
        sp2.right(30)
    def forward():
        sp2.forward(speed)
    def backward():
        sp2.backward(speed)    
    
            
    turtle.onkey(forward, 'Up')
    turtle.onkey(turnleft, 'Left')
    turtle.onkey(turnright, 'Right')
    turtle.onkey(backward, 'Down')
    turtle.onkey(top_layer, '-')
    turtle.listen()


def station_1():
    turtle.tracer(1000)
    sta= turtle.Turtle()
    sta.color('white')
    sta.penup()
    sta.speed(0)
    sta.hideturtle()
    
    #top two parts
    rect(sta, -250, 160, 30, 10)
    rect(sta, -255, 150, 40, 10)
    rect(sta, -253, 140, 36, 10)
    
    #connector 1
    rect(sta, -250, 130, 30, 10)
        
    #ring 1
    rect(sta, -310, 120, 150, 20)
    
    #connector 2
    rect(sta, -250, 100, 30, 15)
    
    #ring 2
    rect(sta, -310, 85, 150, 25)
    
    #connector 3
    rect(sta, -250, 60, 30, 15)
    
    #ring 3
    rect(sta, -310, 45, 150, 40)
    
    #connector 4
    rect(sta, -250, 5, 30, 15)
    
    #ring 4
    rect(sta, -310, -10, 150, 20)
    
    #connector 5
    rect(sta, -250, -30, 30, 15)

    #junction 1
    rect(sta, -260, -45, 50, 20)

    #arm 1
    rect(sta, -260, -46, -5, 18)
    rect(sta, -265, -47, -50, 16)

    #motor 1
    rect(sta, -315, -41, -7, 28)
    rect(sta, -322, -37, -9, 36)
    
    #ring 5
    rect(sta, -331, -7, -15, 96)
    
    #arm 2
    rect(sta, -210, -46, 5, 18)
    rect(sta, -205, -47, 30, 16)

    #juntion 2
    rect(sta, -175,-46, 18, 18)

    #arm 3
    rect(sta, -162,-64, -10, 50)

    #docking bay
    for i in range(5):
        rect(sta, -162, -75-i*5, 10, 2)
        
    #solar panels
    ## strut 1
    sta.penup()
    sta.setpos(-250,-65)
    sta.seth(270)
    sta.pendown()

    # panel 1
    sta.forward(70)
    sta.right(90)
    sta.forward(70)
    sta.right(90)
    sta.forward(2)
    sta.right(90)
    sta.forward(68)
    sta.left(90)
    sta.forward(68)

    ## strut 2
    sta.penup()
    sta.setpos(-220,-65)
    sta.seth(270)
    sta.pendown()

    # panel 2
    sta.forward(70)
    sta.left(90)
    sta.forward(70)
    sta.left(90)
    sta.forward(2)
    sta.left(90)
    sta.forward(68)
    sta.right(90)
    sta.forward(68)
        
    sta.penup()
    sta.setpos(-250,-70)
    sta.seth(0)
    sta.pendown()
    for i in range(14):
        sta.forward(14)
        sta.right(90)
        sta.forward(4)
        sta.right(90)
        sta.forward(14)
        sta.left(180)
        
    sta.penup()
    sta.setpos(-252,-70)
    sta.seth(180)
    sta.pendown()
    for i in range(14):
        sta.forward(18)
        sta.left(90)
        sta.forward(4)
        sta.left(90)
        sta.forward(18)
        sta.right(180)
        
    sta.penup()
    sta.setpos(-272,-133)
    sta.seth(90)
    sta.pendown()
    for i in range(11):
        sta.forward(18)
        sta.left(90)
        sta.forward(4)
        sta.left(90)
        sta.forward(18)
        sta.right(180)
        
    sta.penup()
    sta.setpos(-220,-70)
    sta.seth(180)
    sta.pendown()
    for i in range(14):
        sta.forward(14)
        sta.left(90)
        sta.forward(4)
        sta.left(90)
        sta.forward(14)
        sta.right(180)
        
    sta.penup()
    sta.setpos(-218,-70)
    sta.seth(0)
    sta.pendown()
    for i in range(14):
        sta.forward(18)
        sta.right(90)
        sta.forward(4)
        sta.right(90)
        sta.forward(18)
        sta.left(180)
        
    sta.penup()
    sta.setpos(-198,-133)
    sta.seth(90)
    sta.pendown()
    for i in range(11):
        sta.forward(18)
        sta.right(90)
        sta.forward(4)
        sta.right(90)
        sta.forward(18)
        sta.right(180)
        
    sta.penup()
    sta.setpos(-154,-135)
    sta.seth(270)
    sta.pendown()
    for i in range(14):
        sta.forward(18)
        sta.right(90)
        sta.forward(4)
        sta.right(90)
        sta.forward(18)
        sta.right(180)
        
    sta.penup()
    sta.setpos(-260,-135)
    sta.seth(270)
    sta.pendown()
    for i in range(14):
        sta.forward(18)
        sta.right(90)
        sta.forward(4)
        sta.right(90)
        sta.forward(18)
        sta.right(180)

    
    skm = turtle.Turtle()
    skm.hideturtle()
    skm.color('white')
    skm.speed(0)
    skm.penup()
    skm.setpos(-162,-64)
    skm.seth(0)
            
    dashed_line(skm, 8, 5, 3)       
    skm.right(90)
    dashed_line(skm, 6, 5, 3)        
    skm.right(90)
    dashed_line(skm, 8, 5, 3)
   
    skm.setpos(-162,-77)
    skm.write('Docking Port', font=('Arial', 7, 'normal'))
    turtle.update()
    

    
    
def stations():
    station = turtle.Turtle()
    station.color('white')
    station.penup()
    station.shape('circle')
    station.speed(0)
    station.resizemode('user')
    station.shapesize(0.3, 0.3, 0.3)
    station.setpos(200, 75)
    station.stamp()
    station.write('station 001')
    station.setpos(-300, 45)
    station.stamp()
    station.write('station 002')
    station.setpos(-100,-200)
    station.stamp()
    station.write('station 003')


def screen_setup():
    turtle.setup(900, 500, 0,0)
    turtle.title("Navigation system")
    turtle.bgcolor('black')
    con = turtle.Turtle()
    con.penup()
    con.speed(0)
    con.color('white')
    con.hideturtle()
    con.setpos(420, -230)
    con.write('+')
    con.setpos(430, -230)
    con.write('-')
   
    

def docking_port1():
    #MAIN BODY
    dp1 = turtle.Turtle()
    dp1.hideturtle()
    dp1.color('white')
    dp1.speed(0)
    dp1.penup()
    dp1.setpos(-400,-250)
    dp1.pendown()
    dp1.seth(90)
    for i in range(5):
        dp1.forward(35)
        dp1.right(90)
        dp1.forward(200)
        dp1.left(90)
        dp1.forward(30)
        dp1.left(90)
        dp1.forward(200)
        dp1.right(90)
        dp1.forward(35)
    #AIR LOCKS
    dp1.penup()
    dp1.setpos(-370,-215)        
    for i in range(5):
        dp1.seth(270)
        dp1.pendown()
        for i in range(4):
            dp1.forward(3)
            dp1.left(90)
            dp1.forward(8)
            dp1.left(90)
            dp1.forward(3)
            dp1.right(90)
            dp1.forward(30)
            dp1.right(90)
        dp1.penup()
        dp1.seth(90)
        dp1.forward(30)
        dp1.seth(180)
        dp1.forward(152)
        dp1.seth(90)
        dp1.pendown()
        for i in range(4):
            dp1.forward(3)
            dp1.right(90)
            dp1.forward(8)
            dp1.right(90)
            dp1.forward(3)
            dp1.left(90)
            dp1.forward(30)
            dp1.left(90)
        dp1.penup()
        dp1.seth(90)
        dp1.forward(70)
        dp1.seth(180)
        dp1.forward(152)
    #PANELS 1
    dp1.penup()
    dp1.setpos(-255,-215)
    for i in range(5):
        dp1.seth(90)
        dp1.pendown()
        dp1.forward(30)
        dp1.left(90)
        dp1.forward(40)
        dp1.left(90)
        dp1.forward(30)
        dp1.seth(90)
        dp1.forward(15)
        dp1.left(90)
        dp1.forward(20)
        dp1.right(90)
        dp1.forward(15)
        dp1.right(180)
        dp1.forward(30)
        dp1.right(90)
        dp1.forward(30)
        dp1.right(90)
        dp1.forward(30)
        dp1.seth(270)
        for i in range(2):
            dp1.forward(10)
            dp1.right(90)
            dp1.forward(40)
            dp1.left(180)
            dp1.forward(40)
            dp1.right(90)
        dp1.forward(10)
        dp1.right(90)
        dp1.forward(40)
        dp1.right(90)
        dp1.forward(30)
        dp1.left(90)
        dp1.forward(15)
        dp1.left(90)
        dp1.forward(30)
        dp1.penup()
        dp1.seth(90)
        dp1.forward(100)
        dp1.setx(-255)
    #PANELS 2
    dp1.penup()
    dp1.setpos(-400,-220)
    dp1.pendown()
    for i in range(4):
        dp1.seth(180)
        dp1.forward(50)
        dp1.seth(0)
        dp1.forward(25)
        dp1.left(90)
        dp1.forward(40)
        dp1.left(90)
        dp1.forward(25)
        dp1.seth(0)
        for i in range(2):
            dp1.forward(16.6)
            dp1.left(90)
            dp1.forward(50)
            dp1.seth(270)
            dp1.forward(50)
            dp1.seth(0)
        dp1.setx(-400)
        for i in range(2):
            dp1.left(90)
            dp1.forward(50)
        dp1.seth(0)
        dp1.forward(50)
        dp1.left(90)
        dp1.forward(30)
        
         
    
def docking_layer():
    turtle.clearscreen()
    screen_setup()
    docking_port1()
    sp3 = turtle.Turtle()
    sp3.color('white')
    sp3.penup()
    sp3.speed(0)
    sp3.setpos(300, 0)
    sp3.seth(180)
    sp3.showturtle()
    speed = (10)
    def turnleft():
        sp3.left(30)
    def turnright():
        sp3.right(30)
    def forward():
        sp3.forward(speed)
    def backward():
        sp3.backward(speed)
#airlocks
    a1 = (-370,-215)
    a2 = (-332,-215)
    a3 = (-294,-215)
    a4 = (-256,-215)
    a5 = (-370,-185)
    a6 = (-332,-185)
    a7 = (-294,-185)
    a8 = (-256,-185)
    a9 = (-370,-115)
    a10 = (-332,-115)
    a11 = (-294,-115)
    a12 = (-256,-115)
    a13 = (-370,-85)
    a14 = (-332,-85)
    a15 = (-294,-85)
    a16 = (-256,-85)
    a17 = (-370,-15)
    a18 = (-332,-15)
    a19 = (-294,-15)
    a20 = (-256,-15)
    a21 = (-370,15)
    a22 = (-332,15)
    a23 = (-294,15)
    a24 = (-256,15)
    a25 = (-370,85)
    a26 = (-332,85)
    a27 = (-294,85)
    a28 = (-256,85)
    a29 = (-370,115)
    a30 = (-332,115)
    a31 = (-294,115)
    a32 = (-256,115)
    a33 = (-370,185)
    a34 = (-332,185)
    a35 = (-294,185)
    a36 = (-256,185)
    a37 = (-370,215)
    a38 = (-332,215)
    a39 = (-294,215)
    a40 = (-256,215)
    
    
    turtle.onkey(forward, 'Up')
    turtle.onkey(turnleft, 'Left')
    turtle.onkey(turnright, 'Right')
    turtle.onkey(backward, 'Down')
    turtle.onkey(middle_layer_sta1, '-')
    turtle.listen()

    for i in range(1000):
        a = random.randrange([a1,a2,a3,a4,a5,a6,a7,a8])
        y = random.randrange(-250, 250)
        t = random.randrange(50,160)
        ship = turtle.Turtle()
        ship.hideturtle()
        ship.color('gray')
        ship.penup()
        ship.speed(0)
        ship.setpos(455, y)
        ship.showturtle()
        ship.speed(1)
        ship.goto(a)
        ship.delay(t)
        ship2 = turtle.Turtle()
        ship2.hideturtle()
        ship2.color('gray')
        ship2.penup()
        ship2.speed(0)
        ship2.setpos(455, y)
        ship2.showturtle()
        ship2.speed(1)
        ship2.goto(a1)
        ship2.delay(t)
        if sp2.xcor() > -162 and sp2.xcor() < -98 and sp2.ycor() > -112 and sp2.ycor() < -64:
            break
       
# planet_layer()
top_layer()
# docking_layer()
