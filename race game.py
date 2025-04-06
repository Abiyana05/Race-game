import turtle

road=turtle.Screen()
road.bgpic("road.gif")

redcar=turtle.Turtle()
redcar.setheading(90)
redcar.penup()
redcar.goto(-100,-240)
road.addshape("red.gif")
redcar.shape("red.gif")

bluecar=turtle.Turtle()
bluecar.setheading(90)
bluecar.penup()
bluecar.goto(100,-240)
road.addshape("blue.gif")
bluecar.shape("blue.gif")

def player1():
    redcar.forward(5)

def player2():
    bluecar.forward(5)

turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")

turtle.listen()

while True:
    road.update() #ithu kudukala na initial point laye irukkum so oru oru thadavaium update pannanum
    if redcar.pos() > (-100,200) : #to find the plot of red car 
     road.bgpic("redfinish.gif")
    if bluecar.pos() > (100,200) : 
     road.bgpic("bluefinish.gif")
   

turtle.done()