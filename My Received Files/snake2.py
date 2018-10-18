#Snake Attempt2

from Tkinter import *
from random import *
import time
import tkMessageBox

root=Tk()
root.title=("SnaKe")

cnvSnake=Canvas(root,width=640,height=480)
cnvSnake.grid(row=0,column=0)


class player:
    x=320
    y=460
    lose=0
    direction="N"
    color="blue"

class point:
    x=randrange(20,320)
    y=randrange(20,460)
    p=0
    color="yellow"

def Getpoint():
    for x in range(0,21):
        if player.x and player.y==point.x+x and point.y:
            print"lose2"
            print player.x,player.y
            print point.x+x,point.y
            player.lose=1
        elif player.x and player.y==point.x and point.y+x:
            print"lose3"
            player.lose=1
        elif player.x and player.y==point.x+x and point.y+x:
            print "lose4"
            player.lose=1
    


def Lose():
    if player.x<0 or player.x>640 or player.y<0 or player.y>480:
        player.lose=1
        print "lose1"
        tkMessageBox.showinfo("Game Over         ","BL")

def Redraw():
    cnvSnake.delete(ALL)

def DrawPoint():
    cnvSnake.create_oval(point.x,point.y,point.x+20,point.y+20,fill=point.color)

def DrawPlayer():
    cnvSnake.create_oval(player.x,player.y,player.x+20,player.y+20,fill=player.color)

def MoveUp(Event):
    player.direction="N"
    player.y+=-10
def MoveDown(Event):
    player.direction="S"
    player.y+=10
def MoveLeft(Event):
    player.direction="W"
    player.x+=-10
def MoveRight(Event):
    player.direction="E"
    player.x+=10

def Kill(Event):
    root.destroy()

    
cnvSnake.bind("<Up>",MoveUp)
cnvSnake.bind("<Left>",MoveLeft)
cnvSnake.bind("<Right>",MoveRight)
cnvSnake.bind("<Down>",MoveDown)
cnvSnake.bind("<k>",Kill)
    
while player.lose!=1:
    print
    if player.direction=="N":
        player.y+=-10
    elif player.direction=="S":
        player.y+=10
    elif player.direction=="E":
        player.x+=10
    elif player.direction=="W":
        player.x+=-10
    Redraw()
    DrawPlayer()
    DrawPoint()
    time.sleep(0.05)
    Lose()
    Getpoint()
root.mainloop()
