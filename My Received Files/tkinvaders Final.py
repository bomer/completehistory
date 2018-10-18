## Space Invaders in TKINTER

## Imports

from random import *
from Tkinter import *
import time
import math
import tkMessageBox

##---Variables

#---Parameter variables    
width= 1000
height=600
num_of_enemies=150
size_of_enemy=20
speed=2
can_shoot=4

#---Process variables
current_x=(size_of_enemy/2)
current_y=(size_of_enemy/2)
x_count=0
count=0
count2=0
bullet_count=0
storedp_x=0
canshoot=0
playerhealth=100
current_level=1
##---Window
root=Tk()
root.title("TKInvaders")

canvas = Canvas(root, width=width, height=height, bg="black")
canvas.grid(row=0,column=0)

##---Data-structures-------

enemies=[]
player_bullets=[["X","X"],["X","X"],["X","X"],["X","X"],["X","X"],["X","X"]]
enemy_bullets=[]

##---classes------

class player:

    x=width/2
    y=height-5

class enemy:
    x=0
    y=0

    def init(self):
        
        global  current_x,current_y, x_count, width, size_of_enemy, count

        count+=1
        enemy.x=current_x
        current_x+=(2*size_of_enemy)
        x_count+=1
        
        if x_count>=width/(2*size_of_enemy):
            current_y+=(2*size_of_enemy)
            x_count=0
            current_x=(size_of_enemy/2)
            
        else:
            enemy.y=current_y

    def move(self):
        
        global  width, size_of_enemy,speed

        current=0
        
        for x in enemies:
            
            if enemies[current][1]!="X":
                if (enemies[current][2]/size_of_enemy)% 2 == 0:

                    enemies[current][1]+=speed

                    if enemies[current][1]==width - size_of_enemy:
                        enemies[current][2]+=(size_of_enemy)

                else:

                    enemies[current][1]-=speed

                    if enemies[current][1]==0:
                        enemies[current][2]+=(size_of_enemy)

                current+=1
                
            else:
                current+=1

            
class playerbullet:
    global width,height
    x=player.x
    y=height-5

    def __init__():
        global bullet_count

        player_bullets[bullet_count][0]=player.x
        player_bullets[bullet_count][1]=playerbullet.y
        print player_bullets

    
##---Secondary functions

def shoot(event):
    new_bullet_item(event)
    
    
    
    
def checkbullets():
    global size_of_enemy, num_of_enemies
    count=0
    while count<(len(player_bullets)-1):
        if player_bullets[count][1]<=0:
            player_bullets[count][1]="X"
            player_bullets[count][0]="X"

        y=0
        for x in enemies:
            if enemies[y][1]!="X" and enemies[y][0]!="X":
                if player_bullets[count][0]!="X":           
                    if player_bullets[count][0]-(enemies[y][1] + size_of_enemy)>-size_of_enemy and player_bullets[count][0]-(enemies[y][1] + size_of_enemy)<size_of_enemy:
                        if player_bullets[count][1]-(enemies[y][2] + size_of_enemy)>-size_of_enemy and player_bullets[count][1]-(enemies[y][2] + size_of_enemy)<size_of_enemy:
                            enemies[y][1]="X"
                            enemies[y][0]="X"
                            player_bullets[count][1]="X"
                            player_bullets[count][0]="X"
                            num_of_enemies-=1
                            y+=1
                        else:
                            y+=1
                    else:
                        y+=1
                else:
                    y+=1                
        if count==5:
            count=0
        else:
            count+=1

def draw_bullets():
    count=0
       
    for x in player_bullets:
        if player_bullets[count][1]!="X":

            x1=player_bullets[count][0]
            y1=player_bullets[count][1]

            x2=player_bullets[count][0] + 5
            y2=player_bullets[count][1] + 5
            build_bullet(x1,x2,y1,y2)            
            player_bullets[count][1]-=4
            count+=1
        else:
            count+=1
            
def build_bullet(x1,x2,y1,y2):
    canvas.create_rectangle(x1,y1,x2,y2, fill="white")
    

def new_bullet_item(event):
    global bullet_count

    player_bullets[bullet_count][0]=event.x
    player_bullets[bullet_count][1]=playerbullet.y
    if bullet_count!=5:
        bullet_count+=1
    else:
        bullet_count=0
##    print player_bullets 

## Mainloop functions   


def build():
    
    global num_of_enemies, size_of_enemy,can_shoot
    
    shooter=0
    count=0
    for x in range(0,num_of_enemies):
        
        if shooter==0:            
            new=enemy()
            new.init()
            addenemy=[1,enemy.x,enemy.y]
            enemies.append(addenemy)
            addenemybullet=["X","X"]
            enemy_bullets.append(addenemybullet)
            shooter+=1
            count+=1
        else:
            new=enemy()
            new.init()
            addenemy=[0,enemy.x,enemy.y]
            enemies.append(addenemy)
            if shooter==can_shoot:
                shooter=0
                count+=1
            else:
                shooter+=1
                count+=1
 
    

def DRAWENEMY():
    global size_of_enemy,canshoot
    current=0
    
    for x in enemies:
        if enemies[current][1]!="X":
            x1=enemies[current][1]
            y1=enemies[current][2]
            
            x2=enemies[current][1] + size_of_enemy
            y2=enemies[current][2] + size_of_enemy
                   
            canvas.create_rectangle(x1,y1,x2,y2,width=4,fill="green")
            current+=1
        else:
            enemies.remove(enemies[current])
            current+=1

#every 10 cycles every specified enemy will shoot

def ENEMYSHOOT():
    global canshoot
    count=0
    bullet_count=0
    if canshoot==100:
        for x in enemies:
            if enemies[count][0]==1 and enemies[count][1]!="X":
               enemy_bullets[bullet_count][0]=enemies[count][1]
               enemy_bullets[bullet_count][1]=enemies[count][2]

               count+=1
               bullet_count+=1
            else:
                count+=1
                canshoot+=1

        canshoot=0

    else:
        canshoot+=1
        DRAW_ENEMY_BULLETS()
        
def DRAW_ENEMY_BULLETS():
    
    count=0

    for x in enemy_bullets:
        if enemy_bullets[count][1]!="X":

            x1=enemy_bullets[count][0]
            y1=enemy_bullets[count][1]

            x2=enemy_bullets[count][0] + 5
            y2=enemy_bullets[count][1] + 5
            BUILD_ENEMY_BULLETS(x1,x2,y1,y2) 
            enemy_bullets[count][1]+=8
            count+=1
        else:
            count+=1

def BUILD_ENEMY_BULLETS(x1,x2,y1,y2):
    canvas.create_rectangle(x1,y1,x2,y2, fill="white")
    
def ENEMY_BULLETS_CHECK():
    
    global size_of_enemy, height, playerhealth  
    count=0


    for x in enemy_bullets:
        if enemy_bullets[count][1]>height and enemy_bullets[count][1]!="X":
            enemy_bullets[count][1]="X"
            enemy_bullets[count][0]="X"

            
        elif enemy_bullets[count][1]!="X":        
            if player.x-(enemy_bullets[count][0])>-15 and player.x-(enemy_bullets[count][0])<15:
                if player.y-(enemy_bullets[count][1])>-15 and player.y-(enemy_bullets[count][1])<15:
                    playerhealth-=10
                    enemy_bullets[count][1]="X"
                    enemy_bullets[count][0]="X"
                    count+=1
                else:
                    count+=1
            else:
                count+=1
        
def TRACKPLAYER(event):
    global storedp_x
    
    player.x=event.x
    event.x=storedp_x
    
    
def DRAWPLAYER():
    n=canvas.create_rectangle(player.x-16,player.y,player.x+16,player.y-16,fill="red",tags="player")    
    
def ANIMATEPLAYER(event):
    TRACKPLAYER(event)
    DRAWPLAYER()

def DRAWHEALTH():
    global playerhealth
    canvas.create_rectangle(10,20,110,5,fill="red")
    canvas.create_rectangle(10,20,playerhealth+10,5,fill="green")

##---Leveling---##


def level2():
    global width, height, num_of_enemies, size_of_enemy, speed, can_shoot, playerhealth
    
    num_of_enemies=200
    playerhealth=100
    size_of_enemy=15
    can_shoot=3
    speed=2
    build()
    DRAWENEMY()
    Main()
    
def level3():
    global width, height, num_of_enemies, size_of_enemy, speed, playerhealth
    
    num_of_enemies=220
    playerhealth=100
    size_of_enemy=10
    can_shoot=2
    speed=1
    build()
    DRAWENEMY()
    Main()

def next_level():
    global width, height, playerhealth, num_of_enemies, size_of_enemy, speed, x_count, count, count2, bullet_count, storedp_x, current_level,current_x,current_y

    x_count=0
    count=0
    count2=0
    bullet_count=0
    storedp_x=0
    current_x=(size_of_enemy/2)
    current_y=(size_of_enemy/2)
        
    if current_level==1:
        playerhealth=100
        del enemies[:]
        print enemies
        current_level+=1
        level2()
        

    elif current_level==2:
        del enemies[:]
        print enemies
        current_level+=1
        level3()

    else:
        print "YOU HAVE SUCCESSFULLY DEFENDED"

def reset():
    
    global width, height, num_of_enemies, size_of_enemy, x_count, count, count2, storedp_x, current_level, current_x, current_y

    del enemies[:]
    
    x_count=0
    count=0
    count2=0
    storedp_x=0
    current_x=(size_of_enemy/2)
    current_y=(size_of_enemy/2)    
    current_level=1
    
    num_of_enemies=200
    size_of_enemy=20

    can_shoot=4
        
    build()
    DRAWENEMY()
    Main()



    

#----RUN---------


def ANIMATE():
    
    canvas.delete(ALL)
    new=enemy()
    new.move()
    DRAWHEALTH() 
    DRAWENEMY()  
    DRAWPLAYER()
    draw_bullets()
    checkbullets()
    ENEMYSHOOT()
    ENEMY_BULLETS_CHECK()


def Main():
    global playerhealth, height, num_of_enemies
    build()
    print enemies
    DRAWENEMY()
    finished="untrue"
    while finished!="true":
        
        while num_of_enemies!=0 and playerhealth!=0 and enemies[len(enemies)-1][2]<height:
            ANIMATE()
            time.sleep(0)
            print ""
                
        count=0
        
        for x in enemies:
            if enemies[count][2]>height:
                tkMessageBox.showinfo(
                    "---GAME OVER---",
                    ("The Invaders have Landed"),
                    )
                finished="true"
                
            else:
                count+=1
                
            
        if playerhealth==0:
            tkMessageBox.showinfo(
                "---GAME OVER---",
                ("You have been killed"),
                )
            
            finished="true"
                
        elif len(enemies)==0:
            tkMessageBox.showinfo(
                "---YOU WIN!---",
                ("You have Defeated this wave of invaders!"),
                )
            
            time.sleep(2)
            next_level()
            
    finished="untrue"
##    reset()
    
canvas.bind("<Motion>",TRACKPLAYER)
canvas.bind("<Button-1>",shoot)

Main()

mainloop ()



# runs at an average 30fps
