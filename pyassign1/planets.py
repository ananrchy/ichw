import turtle
import math

wn=turtle.Screen()
wn.screensize(10000,10000)
turtle.bgcolor("white")
sun=turtle.Turtle()
mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()
plants=[mercury,venus,earth,mars,jupiter,saturn]

l=0.035
ac=10000
si=2
sp=300

mercury.color("blue")
venus.color("yellow")
earth.color("black")
mars.color("orange")
jupiter.color("brown")
saturn.color("green")
sun.shape("circle")
sun.color("orange")

sun.shapesize(30*0.1)
plants[0].shapesize(0.024*si)
plants[1].shapesize(0.061*si)
plants[2].shapesize(0.064*si)
plants[3].shapesize(0.034*si)
plants[4].shapesize(0.70*si)
plants[5].shapesize(0.58*si)
for i in range(6):
    plants[i].shape("circle")

for i in range(6):
    plants[i].penup()
    plants[i].speed(0)
plants[0].setpos(3.07/l,0)
plants[1].setpos(7.18/l,0)
plants[2].setpos(9.83/l,0)
plants[3].setpos(13.80/l,0)
plants[4].setpos(49.50/l,0)
plants[5].setpos(90.40/l,0)

for i in range(6):
    plants[i].pendown()

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0

for i in range(ac):
    plants[0].setpos((3.87*math.cos(a1)-0.80)/l,3.79/l*math.sin(a1))
    a1=a1+1/0.24/sp
    plants[1].setpos((7.23*math.cos(a2)-0.05)/l,7.23/l*math.sin(a2))
    a2=a2+1/0.615/sp
    plants[2].setpos((10.00*math.cos(a3)-0.167)/l,10.00/l*math.sin(a3))
    a3=a3+1/sp
    plants[3].setpos((15.23*math.cos(a4)-1.42)/l,15.16/l*math.sin(a4))
    a4=a4+1/1.88/sp
    plants[4].setpos((52.04*math.cos(a5)-2.54)/l,51.97/l*math.sin(a5))
    a5=a5+1/11.86/sp
    plants[5].setpos((95.83*math.cos(a6)-5.42)/l,95.76/l*math.sin(a6))
    a6=a6+1/29.46/sp

    

































