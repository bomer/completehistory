#snake

from Tkinter import *
from random import*

root=Tk()
root.canv = Canvas(root, width=600, height=600)
root.canv.grid(row=0,column=0)

length=4

board=[["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]]           

#Player
#STarting co-ordinates
x1=14*20
x2=x1+20
y1=29*20
y2=y1+20
#What player is kept under in the board
player="P"
#Player co on board
x=14
y=29

#Points
#Point keeper; for when the get the point
pk=0
#what point is kept under in board
point="1"
#To put the point on the board
numx=0
numy=0
#points
points=0

#Enemy
#board location
numx2=0
numy2=0
#Hwether or not to put enemy on board
en=0
#What enemy is under on board
enemy="E"

#Makes the player and puts in starting co-or
class Player:
    x1=x1
    x2=x2
    y1=y1
    y2=y2
    print"x",x
    print"y",y
    root.canv.create_oval(x1,y1,x2,y2,fill="blue")

#Puts the points on the board
def Point():
    global pk,numx,numy,en,point
    if pk==0:
        numx=randrange(1,29)-1
        numy=randrange(1,29)
        pk+=1
        en+=1
    x1=numx*20
    x2=x1+20
    y1=numy*20
    y2=y1+20
    root.canv.create_oval(x1,y1,x2,y2,fill="yellow")
    board[numy][numx]=point

#Puts inactive enemy on the board
def Enemy():
    global numx2,numy2,en,enemy
    if en==3:
        numx2=randrange(0,30)
        numy2=randrange(0,30)
        en=0
        x1=numx2*20
        x2=x1+20
        y1=numy2*20
        y2=y1+20
        root.canv.create_oval(x1,y1,x2,y2,fill="red")
        board[numy2][numx2]=enemy

def PlayerCheck(x,y):
    global points,pk
    if board[y][x]!="":
        if board[y][x]=="1":
            points+=1
            pk=0
            board[y][x]=""
        
        
#Makes player move
class move:
    global length
    def MoveUp(event):
        global x1,x2,y1,y2,y,x,player
        x1=x1   
        x2=x2
        y1=y1-20
        y2=y2-20
        board[y][x]=""
        y=y-1
        x=x
        board[y][x]=player
        for x in range(length):
            board[y-length][x]=player
        root.canv.delete(ALL)
        root.canv.create_oval(x1,y1,x2,y2,fill="blue")
        Point()
        Enemy()
        PlayerCheck(x,y)
        

    def MoveDown(event):
        global x1,x2,y1,y2,y,x,player
        x1=x1
        x2=x2
        y1=y1+20
        y2=y2+20
        board[y][x]=""
        y=y+1
        x=x
        board[y][x]=player
        root.canv.delete(ALL)
        root.canv.create_oval(x1,y1,x2,y2,fill="blue")
        Point()
        Enemy()
        PlayerCheck(x,y)

    def MoveRight(event):
        global x1,x2,y1,y2,x,y,player
        x1=x1+20
        x2=x2+20
        y1=y1
        y2=y2
        board[y][x]=""
        x=x+1
        y=y
        board[y][x]=player
        root.canv.delete(ALL)
        root.canv.create_oval(x1,y1,x2,y2,fill="blue")
        Point()
        Enemy()
        PlayerCheck(x,y)

    def MoveLeft(event):
        global x1,x2,y1,y2,x,y,player
        x1=x1-20
        x2=x2-20
        y1=y1
        y2=y2
        board[y][x]=""
        x=x-1
        y=y
        board[y][x]=player
        root.canv.delete(ALL)
        root.canv.create_oval(x1,y1,x2,y2,fill="blue")
        Point()
        Enemy()
        PlayerCheck(x,y)
    

    root.canv.bind("<Up>",MoveUp)
    root.canv.bind("<Down>",MoveDown)
    root.canv.bind("<Left>",MoveLeft)
    root.canv.bind("<Right>",MoveRight)


Player
move

