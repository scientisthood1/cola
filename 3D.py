from math import *
from turtle import *
F=float(input("input the speed (the lower the faster (must be more than 0.).)."))
S=float(input("input the speed of the star (the higher the faster.)."))
C=float(input("input the speed of the cube (the higher the faster.)."))
P=float(input("input the speed of the perspective (the higher the faster.)."))
D=float(input("input the speed of the triangle thing (the higher the faster.)."))
T=pi/4
x1=-1
y1=-1
z1=-1
x2=1
y2=-1
z2=-1
x3=-1
y3=1
z3=-1
x4=-1
y4=-1
z4=1
x5=1
y5=1
z5=-1
x6=-1
y6=1
z6=1
x7=1
y7=-1
z7=1
x8=1
y8=1
z8=1
xC=0
yC=0
zC=-4
speed(0)
#penup()
import turtle
t=turtle.Turtle()
screen=turtle.Screen()
#while 0 < 1:
#    Point=pi
#    for i in range(4):
#        penup()
#        goto(0,-100*sin(T+Point))
#        pendown()
#        goto(100*sin(T+Point),100*sin(T+Point))
#        goto(0,100*sin(T+Point))
#        Point-=pi/2
#    goto(100*sin(T+pi),0)
#    pendown()
#    goto(100*sin(T+pi/2),100*sin(T))
#    goto(100*sin(T),0)
#    goto(100*sin(T-pi/2),-100*sin(T))
#    screen.tracer(True)
#    screen.update()
#    screen.tracer(False)
#    T+=pi/90
#    turtle.reset()
while 0 < 1:
#    goto(200*(x1-xC)/(z1-zC),200*(y1-yC)/(z1-zC))
#    goto(200*(x2-xC)/(z2-zC),200*(y2-yC)/(z2-zC))
#    goto(200*(x3-xC)/(z3-zC),200*(y3-yC)/(z3-zC))
#    goto(200*(x4-xC)/(z4-zC),200*(y4-yC)/(z4-zC))
#    goto(200*(x5-xC)/(z5-zC),200*(y5-yC)/(z5-zC))
#    goto(200*(x6-xC)/(z6-zC),200*(y6-yC)/(z6-zC))
#    goto(200*(x7-xC)/(z7-zC),200*(y7-yC)/(z7-zC))
#    goto(200*(x8-xC)/(z8-zC),200*(y8-yC)/(z8-zC))
    B=0.1
    t.color("mediumspringgreen","mediumspringgreen")
    penup()
    goto(200*(sin(T*C)-xC)/(cos(T*C)-zC),200*(y8-yC)/(cos(T*C)-zC))
    pendown()
    goto(200*(sin(T*C+pi/2)-xC)/(cos(T*C+pi/2)-zC),200*(y6-yC)/(cos(T*C+pi/2)-zC))
    goto(200*(sin(T*C+pi/2)-xC)/(cos(T*C+pi/2)-zC),200*(y4-yC)/(cos(T*C+pi/2)-zC))
    goto(200*(sin(T*C)-xC)/(cos(T*C)-zC),200*(y7-yC)/(cos(T*C)-zC))
    goto(200*(sin(T*C)-xC)/(cos(T*C)-zC),200*(y8-yC)/(cos(T*C)-zC))
    goto(200*(sin(T*C+3*pi/2)-xC)/(cos(T*C+3*pi/2)-zC),200*(y5-yC)/(cos(T*C+3*pi/2)-zC))
    goto(200*(sin(T*C+pi)-xC)/(cos(T*C+pi)-zC),200*(y3-yC)/(cos(T*C+pi)-zC))
    goto(200*(sin(T*C+pi/2)-xC)/(cos(T*C+pi/2)-zC),200*(y6-yC)/(cos(T*C+pi/2)-zC))
    goto(200*(sin(T*C+pi)-xC)/(cos(T*C+pi)-zC),200*(y3-yC)/(cos(T*C+pi)-zC))
    goto(200*(sin(T*C+pi)-xC)/(cos(T*C+pi)-zC),200*(y1-yC)/(cos(T*C+pi)-zC))
    goto(200*(sin(T*C+pi/2)-xC)/(cos(T*C+pi/2)-zC),200*(y4-yC)/(cos(T*C+pi/2)-zC))
    goto(200*(sin(T*C+pi)-xC)/(cos(T*C+pi)-zC),200*(y1-yC)/(cos(T*C+pi)-zC))
    goto(200*(sin(T*C+3*pi/2)-xC)/(cos(T*C+3*pi/2)-zC),200*(y2-yC)/(cos(T*C+3*pi/2)-zC))
    goto(200*(sin(T*C)-xC)/(cos(T*C)-zC),200*(y7-yC)/(cos(T*C)-zC))
    goto(200*(sin(T*C+3*pi/2)-xC)/(cos(T*C+3*pi/2)-zC),200*(y2-yC)/(cos(T*C+3*pi/2)-zC))
    goto(200*(sin(T*C+3*pi/2)-xC)/(cos(T*C+3*pi/2)-zC),200*(y5-yC)/(cos(T*C+3*pi/2)-zC))
    penup()
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(-1-yC)/(sin(T*D)-zC))
    pendown()
    goto(-200*(cos(T*D+2*pi/3)-xC)/(sin(T*D+2*pi/3)-zC),-200*(-1-yC)/(sin(T*D+2*pi/3)-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(-1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(-1-yC)/(sin(T*D)-zC))
    goto(-200*(-xC)/(-zC),-200*(1-yC)/(-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(-1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(-xC)/(-zC),-200*(1-yC)/(-zC))
    goto(-200*(cos(T*D+2*pi/3)-xC)/(sin(T*D+2*pi/3)-zC),-200*(-1-yC)/(sin(T*D+2*pi/3)-zC))
    penup()
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(1-yC)/(sin(T*D)-zC))
    pendown()
    goto(-200*(cos(T*D+2*pi/3)-xC)/(sin(T*D+2*pi/3)-zC),-200*(1-yC)/(sin(T*D+2*pi/3)-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(1-yC)/(sin(T*D)-zC))
    goto(-200*(-xC)/(-zC),-200*(-1-yC)/(-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(-xC)/(-zC),-200*(-1-yC)/(-zC))
    goto(-200*(cos(T*D+2*pi/3)-xC)/(sin(T*D+2*pi/3)-zC),-200*(1-yC)/(sin(T*D+2*pi/3)-zC))
    goto(-200*(cos(T*D+2*pi/3)-xC)/(sin(T*D+2*pi/3)-zC),-200*(-1-yC)/(sin(T*D+2*pi/3)-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(-1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(cos(T*D+4*pi/3)-xC)/(sin(T*D+4*pi/3)-zC),-200*(1-yC)/(sin(T*D+4*pi/3)-zC))
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(1-yC)/(sin(T*D)-zC))
    goto(-200*(cos(T*D)-xC)/(sin(T*D)-zC),-200*(-1-yC)/(sin(T*D)-zC))
    penup()
    for i in range(99):
        goto((10*B-1)*sin(T*S),(10/B-1))
        pendown()
        B+=0.1
    B=0.1
    penup()
    for i in range(99):
        goto((10*B-1)*sin(T*S),(-10/B+1))
        pendown()
        B+=0.1
    B=0.1
    penup()
    for i in range(99):
        goto((-10*B+1)*sin(T*S),(-10/B+1))
        pendown()
        B+=0.1
    B=0.1
    penup()
    for i in range(99):
        goto((-10*B+1)*sin(T*S),(10/B-1))
        pendown()
        B+=0.1
    goto(0,0)
    goto(0,99)
    goto(0,0)
    goto(99*sin(T*S),0)
    goto(0,0)
    goto(0,-99)
    screen.tracer(True)
    screen.update()
    screen.tracer(False)
    T+=pi/F
    turtle.reset()
    xC=sin(T*P)
    yC=cos(T*P)
    zC=2*sin(T*P)+4
