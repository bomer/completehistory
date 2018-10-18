#Rainbow Snake Paint
#Alpha Version 0.01

from Tkinter import *
from random import *

#Function Variables

colorsetting="black"
thickness=1
selected_tool="spray_paint"
click=1
mousex=0
mousey=0
mousex1=0
mousey1=0

#program functions

def tools(event):
    
    global thickness, colorsetting, selected_tool, click, mousex, mousey, mousex1, mousey1

    if selected_tool=="pencil":
        cnvDraw.create_line(event.x,event.y,event.x-1,event.y-1, width=thickness, fill=colorsetting)
        
    elif selected_tool=="PaintBrush":

        cnvDraw.create_oval(event.x,event.y,event.x+thickness,event.y-thickness, fill=colorsetting, outline=colorsetting)

    elif selected_tool=="spray_paint":

        dotcount=0

        randx=event.x - randrange (-30,30) 
        randy=event.y - randrange (-30,30)
    
        cnvDraw.create_oval(randx,randy,randx+1,randy+1, width=thickness, fill=colorsetting, outline=colorsetting)

        dotcount+=1
    
        while dotcount!=30:
    
            randx=event.x - randrange (-30,30) 
            randy=event.y - randrange (-30,30)
    
            cnvDraw.create_oval(randx,randy,randx+1,randy+1, width=thickness, fill=colorsetting, outline=colorsetting)

            dotcount+=1

        dotcount=0

    elif selected_tool=="CreateLine":
   
        if click==1:
            mousex=event.x
            mousey=event.y
            click=0
            return click, mousex, mousey
        else:
            click=1
            mousex1=event.x
            mousey1=event.y
            cnvDraw.create_line(mousex,mousey,mousex1,mousey1,width=thickness, fill=colorsetting)
            return click
        
    elif selected_tool=="CreateBox":
    
        if click==1:
            mousex=event.x
            mousey=event.y
            click=0
            return click, mousex, mousey
        else:
            click=1
            mousex1=event.x
            mousey1=event.y
            cnvDraw.create_rectangle(mousex,mousey,mousex1,mousey1,width=thickness, fill=colorsetting)
            return click
        
    else:

        if click==1:
            mousex=event.x
            mousey=event.y
            click=0
            return click, mousex, mousey
        else:
            click=1
            mousex1=event.x
            mousey1=event.y
            cnvDraw.create_oval(mousex,mousey,mousex1,mousey1,width=thickness, fill=colorsetting)
            return click
      
#--------Tool Selection--------

def ChoosePencil():
    global selected_tool
    selected_tool="pencil"
    return selected_tool

def ChoosePaintbrush():
    global selected_tool
    selected_tool="PaintBrush"
    return selected_tool

def ChooseSpraypaint():
    global selected_tool
    selected_tool="spray_paint"
    return selected_tool

def ChooseLine():
    global selected_tool
    selected_tool="CreateLine"
    return selected_tool

def ChooseBox():
    global selected_tool
    selected_tool="CreateBox"
    return selected_tool

def ChooseCircle():
    global selected_tool
    selected_tool="CreateCircle"
    return selected_tool

#--------Variant Options-------

def ChooseColor_red():
        global colorsetting
        colorsetting="red"
        return colorsetting
    
def ChooseColor_green():
        global colorsetting
        colorsetting="green"
        return colorsetting

def ChooseColor_blue():
        global colorsetting
        colorsetting="blue"
        return colorsetting
    
def ChooseColor_yellow():
        global colorsetting
        colorsetting="yellow"
        return colorsetting
    
def ChooseColor_white():
        global colorsetting
        colorsetting="white"
        return colorsetting
    
def ChooseColor_black():
        global colorsetting
        colorsetting="black"
        return colorsetting
    
def ChooseColor_orange():
        global colorsetting
        colorsetting="orange"
        return colorsetting
    
def ChooseColor_brown():
        global colorsetting
        colorsetting="brown"
        return colorsetting
    
def ChooseColor_purple():
        global colorsetting
        colorsetting="purple"
        return colorsetting
#______


def ChooseThickness_light():
        global thickness
        thickness=3
        return thickness
def ChooseThickness_medium():
        global thickness
        thickness=8
        return thickness
def ChooseThickness_heavy():
        global thickness
        thickness=15
        return thickness    

#------Application Commands-------

#def New():

#def Save():

#def Exit():
   # root.destroy

root = Tk()

cnvDraw = Canvas (root, height=600, width=800, bg="white")
cnvDraw.grid (column=2,row=0, columnspan=1, rowspan=10)
cnvDraw.bind ("<B1-Motion>", tools)
cnvDraw.bind ("<Button-3>", tools)

#Tools buttons------------

cmdPencil = Button(root, text="Pencil", fg= "#0024ff", command=ChoosePencil)
cmdPencil.grid(column=0, row= 1)

cmdPaintBrush = Button(root, text="Paint Brush", fg= "#0024ff", command=ChoosePaintbrush)
cmdPaintBrush.grid(column=0, row= 2)

cmdSprayPaint = Button(root, text="SprayPaint", fg= "#0024ff", command=ChooseSpraypaint)
cmdSprayPaint.grid(column=0, row= 3)

cmdCreateLine = Button(root, text="Create Line", fg= "#0024ff", command=ChooseLine)
cmdCreateLine.grid(column=0, row= 4)

cmdCreateBox = Button(root, text="Create Box", fg= "#0024ff", command=ChooseBox)
cmdCreateBox.grid(column=0, row= 5)

cmdCreateCirlce = Button(root, text="Create Cirlce", fg= "#0024ff", command=ChooseCircle)
cmdCreateCirlce.grid(column=0, row= 6)

#Color buttons------------

cmdChooseColor_orange = Button(root, text="Orange", fg= "black", bg= "orange", command=ChooseColor_orange)
cmdChooseColor_orange.grid(column=1, row= 1)

cmdChooseColor_red = Button(root, text="Red", fg= "black", bg= "red", command=ChooseColor_red)
cmdChooseColor_red.grid(column=1, row= 2)

cmdChooseColor_blue = Button(root, text="Blue", fg= "black", bg= "blue", command=ChooseColor_blue)
cmdChooseColor_blue.grid(column=1, row= 3)

cmdChooseColor_green= Button(root, text="Green", fg= "black", bg= "green", command=ChooseColor_green)
cmdChooseColor_green.grid(column=1, row= 4)

cmdChooseColor_yellow = Button(root, text="Yellow", fg= "black", bg= "yellow", command=ChooseColor_yellow)
cmdChooseColor_yellow.grid(column=1, row= 5)

cmdChooseColor_white = Button(root, text="White", fg= "black", bg= "white", command=ChooseColor_white)
cmdChooseColor_white.grid(column=1, row= 6)

cmdChooseColor_black = Button(root, text="Black", fg= "white", bg= "black", command=ChooseColor_black)
cmdChooseColor_black.grid(column=1, row= 7)

cmdChooseColor_brown = Button(root, text="Brown", fg= "white", bg= "brown", command=ChooseColor_brown)
cmdChooseColor_brown.grid(column=1, row= 8)

cmdChooseColor_purple = Button(root, text="Purple", fg= "white", bg= "purple", command=ChooseColor_purple)
cmdChooseColor_purple.grid(column=1, row= 9)

#Thickness--------------

cmdChooseThickness_light= Button(root, text="Light", fg= "black", bg= "white", command=ChooseThickness_light)
cmdChooseThickness_light.grid(column=0, row= 7)

cmdChooseThickness_medium= Button(root, text="Medium", fg= "black", bg= "white", command=ChooseThickness_medium)
cmdChooseThickness_medium.grid(column=0, row= 8)

cmdChooseThickness_heavy= Button(root, text="Heavy", fg= "black", bg= "white", command=ChooseThickness_heavy)
cmdChooseThickness_heavy.grid(column=0, row= 9)
  
mainloop ()
