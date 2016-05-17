#night phantom interface
import time
import getpass
import sys
import math
import turtle
import subprocess
import random

def intro():
    print ("""----------------------------
Night Phantom Interface Mk.I
----------------------------""")

#DEFAULT POSITIONS
top_pos = 200,75
middle_sta1_pos = 250, -150
docking_layer_1_pos = 300, 0

def nav_sys():
        #DEFAULT POSITIONS           
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
            sp.goto(200, 75)
        def sta2():
            sp.goto(-300, 45)
        def sta3():
            sp.goto(-100,-200)
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

    def station_1():
        world = turtle.Screen()
        world.tracer(8,25)
        sta= turtle.Turtle()
        sta.color('white')
        sta.penup()
        sta.speed(0)
        sta.hideturtle()
        sta.setpos(-250,160)
        sta.pendown()
        sta.seth(0)
        #top two parts
        for i in range (2):
            sta.forward(30)
            sta.right(90)
            sta.forward(10)
            sta.right(90)
        sta.penup()
        sta.setpos(-255,150)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(40)
            sta.right(90)
            sta.forward(10)
            sta.right(90)
        sta.penup()
        sta.setpos(-253,140)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(36)
            sta.right(90)
            sta.forward(10)
            sta.right(90)
        #conector 1
        sta.penup()
        sta.setpos(-250,130)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(10)
            sta.right(90)
        #ring 1
        sta.penup()
        sta.setpos(-310,120)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(150)
            sta.right(90)
            sta.forward(20)
            sta.right(90)
        #conector 2
        sta.penup()
        sta.setpos(-250,100)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(15)
            sta.right(90)
        #ring 2
        sta.penup()
        sta.setpos(-310,85)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(150)
            sta.right(90)
            sta.forward(25)
            sta.right(90)
        #conector 3
        sta.penup()
        sta.setpos(-250,60)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(15)
            sta.right(90)
        #ring 3
        sta.penup()
        sta.setpos(-310,45)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(150)
            sta.right(90)
            sta.forward(40)
            sta.right(90)
        #conector 4
        sta.penup()
        sta.setpos(-250,5)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(15)
            sta.right(90)
        #ring 4
        sta.penup()
        sta.setpos(-310,-10)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(150)
            sta.right(90)
            sta.forward(20)
            sta.right(90)
        #conector 5
        sta.penup()
        sta.setpos(-250,-30)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(15)
            sta.right(90)
        #junction 1
        sta.penup()
        sta.setpos(-260,-45)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(50)
            sta.right(90)
            sta.forward(20)
            sta.right(90)
        #arm 1
        sta.penup()
        sta.setpos(-260,-46)
        sta.setheading(270)
        sta.pendown()
        for i in range(2):
            sta.forward(18)
            sta.right(90)
            sta.forward(5)
            sta.right(90)
        sta.penup()
        sta.setpos(-265,-47)
        sta.seth(180)
        sta.pendown()
        for i in range(2):
            sta.forward(50)
            sta.left(90)
            sta.forward(16)
            sta.left(90)
        #motor 1 
        sta.penup()
        sta.setpos(-315,-41)
        sta.seth(270)
        sta.pendown()
        for i in range(2):
            sta.forward(28)
            sta.right(90)
            sta.forward(7)
            sta.right(90)
        sta.penup()
        sta.setpos(-322,-37)
        sta.seth(270)
        sta.pendown()
        for i in range(2):
            sta.forward(36)
            sta.right(90)
            sta.forward(9)
            sta.right(90)
        #ring 5
        sta.penup()
        sta.setpos(-331,-7)
        sta.pendown()
        sta.seth(270)
        for i in range(2):
            sta.forward(96)
            sta.right(90)
            sta.forward(15)
            sta.right(90)
        #arm 2
        sta.penup()
        sta.setpos(-210,-46)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(5)
            sta.right(90)
            sta.forward(18)
            sta.right(90)
        sta.penup()
        sta.setpos(-205,-47)
        sta.seth(0)
        sta.pendown()
        for i in range(2):
            sta.forward(30)
            sta.right(90)
            sta.forward(16)
            sta.right(90)
        #juntion 2 
        sta.penup()
        sta.setpos(-175,-46)
        sta.seth(0)
        sta.pendown()
        for i in range(4):
            sta.forward(18)
            sta.right(90)
        #arm 3
        sta.penup()
        sta.setpos(-162,-64)
        sta.seth(270)
        sta.pendown()
        for i in range(2):
            sta.forward(50)
            sta.right(90)
            sta.forward(10)
            sta.right(90)
        #docking bay
        sta.penup()
        sta.setpos(-162,-75)
        sta.seth(0)
        sta.pendown()
        for i in range(5):
            sta.forward(10)
            sta.right(90)
            sta.forward(2)
            sta.right(90)
            sta.forward(10)
            sta.left(90)
            sta.forward(5)
            sta.left(90)
        #solar panels
            #strut 1
        sta.penup()
        sta.setpos(-250,-65)
        sta.seth(270)
        sta.pendown()
        for i in range(1):
            sta.forward(70)
            sta.right(90)
            sta.forward(70)
            sta.right(90)
            sta.forward(2)
            sta.right(90)
            sta.forward(68)
            sta.left(90)
            sta.forward(68)
            #strut 2
        sta.penup()
        sta.setpos(-220,-65)
        sta.seth(270)
        sta.pendown()
        for i in range(1):
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
        for i in range(8):
            skm.forward(5)
            skm.pendown()
            skm.forward(3)
            skm.penup()
        skm.right(90)
        for i in range(6):
            skm.forward(5)
            skm.pendown()
            skm.forward(3)
            skm.penup()
        skm.right(90)
        for i in range(8):
            skm.forward(5)
            skm.pendown()
            skm.forward(3)
            skm.penup()
        skm.setpos(-162,-77)
        skm.write('Docking Port', font=('Arial', 7, 'normal'))
        world.update()

        
        
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
        world = turtle.Screen()
        world.tracer(8,25)
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
        world.update()
            
             
        
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

        
        
        turtle.onkey(forward, 'Up')
        turtle.onkey(turnleft, 'Left')
        turtle.onkey(turnright, 'Right')
        turtle.onkey(backward, 'Down')
        turtle.onkey(middle_layer_sta1, '-')
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
        b = 2
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
            ship.color('gray')
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


    top_layer()



def run_tests():
	testing = [
		['top', 'c', 'fail'],

                #Data File
                ['top', 'a', 'a', 'SS'],
                ['top', 'a', 'b', 'a', 'J'],
                ['top', 'a', 'c', 'LOA'],

                #Oxygen Generation System
		['top', 'c', 'b', 'a', 'a', 'SW'],
		['top', 'c', 'b', 'a', 'b', 'SF'],
                ['top', 'c', 'b', 'a', 'c', 'LOE'],

                #Vertical Thrusters
                ['top', 'c', 'a', 'a', 'a', 'VD'],
                ['top', 'c', 'a', 'a', 'b', 'SUF'],

                #Jet Engines
                ['top', 'c', 'a', 'b', 'a', 'HI'],
                ['top', 'c', 'a', 'b', 'b', 'IO'],
                ['top', 'c', 'a', 'b', 'c', 'U'],

                
               
			
	]

	if testing:
		for test in testing:
			print ('\n===== Starting Test {0} ====='.format(test[-1]))
			menu = test[0]
			for choice in test[1:-1]:
				menu = get_choice(menu, choice)		
				print ('Executing automated option ' + menu)
			assert menu == test[-1]
		print 
		print ('===== All tests passed =====')

def login():
    time.sleep(1)
    password_accepted = False
    while not password_accepted:
        b = getpass.getpass ('enter security key>>> ')
        if b == 'phantom024':
            password_accepted = True
        else:
            print ("Sorry, password not recognised.")
    return password_accepted

def logout():
    time.sleep(1)
    print('Checking systems')
    time.sleep(0.5)
    run_tests()
    print('system check complete')
    time.sleep(1.5)
    print('logging out')
    time.sleep(2)
    logged_in = False
    print('shutting down')
    time.sleep(2)
    sys.exit()    

def calculate_ov():
    mass_str=input ("""please enter the mass of the central object (planet)
in kilograms>>> """)
    M=int (mass_str)

    altitude=input ('please enter the height of the required orbit(in kilometers)>>> ')
    r=int (altitude)

    periapsis=input ("""please enter the distantce of the periapsis from the
central object>>> """)
    r2=int (periapsis)

    epiapsis=input ("""please enter the distance of the epiapsis from the
central object>>> """)
    r1=int (epiapsis)

    G=(0.00000000000667)
    a=((r1)+(r2)/2)
    
    velocity= ((G)*(M))*((2)/(r))-((1)/(a))

    print ('V^2=',(velocity))

  

def get_choice(name, default_choice = ''):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	if 'action' in menus[name]:
		print ('\nACTION: ' + menus[name]['action'].strip())
       
	else:
		print ('\nMENU: ' + menus[name]['prompt'])

	num_options = len(menus[name]['options'])
	
	accepted_user_choice = False
	while not accepted_user_choice:
		for i in range(num_options):
			letter = alphabet[i]
			text = menus[name]['options'][i][0]
			print ('   ({0}) {1}'.format(letter, text))

		if not default_choice:
			user_choice = input('>>>')
		else:
			user_choice = default_choice
			print ('>>> ' + default_choice)
		
		if user_choice in alphabet[0:num_options]:
			accepted_user_choice = True
  
	pos = alphabet.find(user_choice)
	chosen_item = menus[name]['options'][pos][1]
	return chosen_item # eg DF


menus = {
    'top':{
        'prompt': 'enter command requst',
        'options':[
        ['open data file', 'DF'],
        ['calculate orbital velocity', 'OV'],
        ['run ship diagnostics', 'fail'],
        ['run system diagnostics', 'SYD'],
        ['run navigation systems', 'NS'],
        ['Logout and shutdown', 'LO'],
        ]
        },
    'fail':{
        'prompt': 'enter the fault in the ships systems',
        'options':[
        ['engine failure', 'EF'],
        ['life systems failure', 'LS'],
        ['power failure', 'PF'],
        ['hull breach', 'HB'],
        ['return to menu', 'top'],
        ]
        },
     'EF':{
        'prompt': 'Select engine:',
        'options':[
        ['vertical thruster', 'VT'],
        ['jet engine', 'JE'],
        ['ion engine', 'IE'],
        ]
        },
     'VT':{
        'prompt': 'Type of fault:',
        'options':[
        ['visible damage', 'VD'],
        ['start up failure', 'SUF'],        
        ]
        },
      'VD':{
        'action': 'Repair and/ or replace all damaged parts',
        'options':[
        ['return to ship diagnostics', 'fail'],        
        ]
        },

      'SUF':{
        'prompt':("""
check the connections to the main control unit.
If the connections seem secure, apply direct
voltage to the faulty engine. If the engine
is non-responsive, check for visible damage
to the module. If none can be seen, the
fault is likely to be internal. Replace the
engine. If the engine responds to the direct
voltage, re-check the conections. Look for
corroded wires and faults in the circuit.
If these are intact, check the activation
switch.
"""),
        'options':[
        ['return to ship diagnostics', 'fail'],
        ]
        },

    'JE':{
        'prompt': 'select reason for fault',
        'options':[
        ['heavy impact', 'HI'],
        ['intake obstruction', 'IO'],
        ['unknown', 'U'],        
        ]
        },
    'HI':{
        'prompt':("""
Remove cowling. Check for breaches in
combustion chamber. If breach is small,
seal with weld seams. For larger
breaches, replace damaged panels. If
the whole chamber is warped, replace
the whole damn thing. Check for warping
in the main turbines. Make sure that
all of the turbines can rotate feely.
If this is not possible, repair or
replace warped turbine.""") ,
        'options':[
        ['return to ship diagnostics', 'fail'],             
        ]
        },

    'IO':{
        'prompt':("""
Clear the obstruction. Use all means available.
if too deep to manually remove, backfire
the main turbines WITHOUT IGNITING THE
COMBUSTION CHAMBER! If you do this, the
front half of the ship will violently
explode. The debrie should be blown out
of the intake. If this does not work,
remove the main shafft of the intake and
try to clear obstruction from the other
end. If this still doesn't work, replace
the obstructed section of the intake.
""") ,
        'options':[
        ['return to ship diagnostics', 'fail'],    
        ]
        },
    'U':{
        'prompt': ("""
Check the conections to the main control unit.
if conections are intact, remove cowling
and make sure that the turbines are able
to rotate freely. Check the ignition
system is functioning. DO NOT FIRE UP
THE ENGINE WHILE COWLING IS REMOVED.
You'll be fried.
"""),
        'options':[        
        ['return to ship diagnostics', 'fail'],           
        ]
        },

    'LS':{
        'prompt': 'select the faulty system',
        'options':[
        ['Oxygen Generation System', 'OGS'],
        ['Water Reclaimer', 'WR'],           
        ]
        },
    'OGS':{
        'prompt': 'select the type of fault',
        'options':[
        ['stopped working', 'SW'],
        ['startup failure', 'SF'],
        ['loss of efficiency', 'LOE'],
        ]
        },
    'SW':{
        'prompt': ("""
Check the wiring to the generator.
If the connection is stable run a
seperate currrent through the
cathode and anode. If gas bubbles
are released from each of the
diodes, re-check the power source.
If no bubbles are visible, clean
any encrustations or rust off the
diodes."""),
        'options':[
          ['return to ship diagnostics', 'fail'],
          ]
        },
    'SF':{
        'prompt': ("""
Check the wiring to the generator.
If the connection is stable, make
sure the connection joints at the
activation switches are stable.
If these connnections are stable,
make sure that the wiring to the
diodes are fully insulated untill
they connect to the diode.
If all of this is stable, check
the indicator light is working.
The unit could be functioning
perfectly, and the LED is just
worn out or has come loose."""),
        'options':[
          ['return to ship diagnostics', 'fail'],
          ]
        },
    'LOE':{
      'prompt':("""
Make sure that all wires inside the
tank are insulated properly and
are not in contact with the water.
Clear the diodes of any rust or 
crustations that could be
obstructing contact with the
water. Be sure that the water is
not running low and that the
diodes are fully submerged. Also
make sure that the water supply
is clean and unclouded. Also be
sure that the vent for the Oxygen
to pass through is unobstructed
or clogged up."""),
      'options':[
        ['return to ship diagnostics', 'fail'],
        ]
      },

    'DF':{
        'prompt': 'Select the file you want to open',
        'options':[
        ['ship specs', 'SS'],
        ['threat database', 'TD'],
        ['list of onboard assets', 'LOA'],
        ['Return to main menu', 'top'],
        ]
        },
    'SS':{
        'prompt':("""
               ------------------------------
               Modified Light Troop Transport
               -----------------------------
           Ship Type: Heavely modifyed Phantom 257.
                      Added armour, upgraded engines
                      and thrusters.
           Fuel Type: Uranium Power Cells, Modular
                      reactor
           Engine system: Jet engine*3
                          Ion thrusters*2
                          Vertical turbine thrusters*4
           Top speed: 1563 Km/hr (Atmospheric conditions) 
           Weapon systems: Automatic EMA cannons*2
           Landing system: All terrain vertical take off
                           and landing
           Fuel sustainability: 60 hours with engine thrust at
                                50% (781.5 Km/hr)
           Condition capabilities: Operational in both atmospheric and
                                   extraterrestrial conditions. Single
                                   stage to orbit vehicle (SSTO) 
           External lighting systems: High powered searchlights*2
           Crew: Minimum-2
                 Maximum-7



         """),
        'options': [
           ['Back to Data File', 'DF'],
           ]
        },
      'LOA':{
        'prompt': ("""
Inventory
------------
Ship maintenence kit*1
EVA suit*2
EMA Asssult rifle*2
Clip of rifle ammunition*400
Oxygenator*1
Backup oxygen tank*3
Atmospheric regulator*1
Water reclaimer*1
Water supply-300litres
Computer system*4
PDA / Data Pad*2
Radio wave frequency comm units*4
Tool kit*1
EMA Hand gun*3
Clip of hand gun ammunition*450
Flight jacket*3
Ship diagnostics kit*2
Spare engine parts*53
Spare landing gear parts*32
Electrical parts kit*2



        """),

        'options':[
        ['return to data file', 'DF'],
        ]
        },
     'TD':{
        'prompt': 'Choose the sub-file you want to open',
        'options':[
        ['Junkers', 'J'],
        ['return to data file', 'DF'],
        ]
        },
     'J':{
        'prompt': ("""                                   
                                                  Junkers
                                                 ---------
                |    Originating from Kepler-186f, Junkers are descended from the crew        |
                |    of a Mk.4 Cargo Carrier that crashed in the eastern junk yards long      |
                |    ago. A rescue party was sent out, but when they arrived, they            |
                |    found the survivors franticly trying to repair the wrecked ship          |  
                |    that the party had deemed beyond repair. The rescue party was unable     |
                |    to convince them to leave. They left the junkers where they              |
                |    continued their hopeless task until death. However, even though the      |
                |    original crew died, their descendants continue their ancestors mission   |
                |    doing whatever it takes to finish the job. There have even been reports  |
                |    of junkers murdering other scavengers over parts.                        |
                |    One eyewitness attests to this.                                          |
                |    "Me and my friend were scavenging around in a junk yard looking for a    |
                |    UPC I think it was. Anyway we found one and suddenly this Junker         | 
                |    appeared out of nowhere. It spotted the UPC in my mates hand and it      |
                |    started making these deep growling noises. Is all of a sudden lunged     |
                |    towards us with this huge as club and-... oh man. My friend was          | 
                |    screaming and the blood- there was blood every where. It was...It was    | 
                |    horrible. My friends screaming was cut short... That thing just          | 
                |    snatched the power cell and ditched."                                    |
                |    Other eyewitness' and survivors of similar attacks claim that they       |
                |    were only saved because they put down the part the junker had wanted     |   
                |    and left the area quickly before it could attack. It is recommended to   |
                |    avoid junker territory if at all possible.                               |
                |                                                                             |
                




        """),
        'options':[
        ['return to threat database', 'TD'],
        ]
        },
}

#Main Program

intro()
logged_in = True
login()


while logged_in== True:
  m = 'top'
  while m in menus:
    m = get_choice(m)
    print ('executing option' + m)
    if m == 'LO':
      logout()
    elif m == 'OV':
      calculate_ov()
    elif m == 'SYD':
      run_tests()
    elif m == 'NS':
        nav_sys()
  
  



