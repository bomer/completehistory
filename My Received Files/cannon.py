#Cannon

from Tkinter import *
from math import*

#Canvas
root = Tk()
root.title("Welcome to Cannon")

graph=Canvas(height=1000, width=1000)
graph.grid(column=300,row=500, rowspan=1)

Boardimage=PhotoImage(file="prototype.gif")

#graph.create_image(5,2, anchor=NE, image=Boardimage)

#Label height, velocity, angle
lblH=Label(root, text="Height")
lblH.grid(column=10, row=300)
entH=Entry(root)
entH.grid(column=15, row=300)

lblV=Label(root, text="Velocity")
lblV.grid(column=10,row=200)
entV=Entry(root)
entV.grid(column=15,row=200)

lblV=Label(root, text="angle")
lblV.grid(column=10,row=400)
entV=Entry(root)
entV.grid(column=15,row=400)


#Variables

V=0
A=0
RAD=0
IVX=0
IVY=0
G=-9.8
H=0

#V=int(raw_input("enter velocity: "))
#A=int(raw_input("enter angle: "))
#H=int(raw_input("enter Height: "))



#Converting dgrees to radians
def RAD(IVX,IVY):
    RAD=A*pi/180
    IVX=V*cos(RAD)
    IVY=V*sin(RAD)
    return IVX,IVY
    

#Creating parabola
def f(x):
    return x*x

for x in range(0,500):
    print x,f(x)
    graph.create_line(x,500-f(x),x+1,500-f(x+1))


mainloop()
