# Choice Nutrition
from Tkinter import *
from random import *
import tkMessageBox



main = Tk()
main.title("CHOICE Nutrition")

X=0
Y=0
infovalue = 0

#Radio Buttons
v = IntVar()
Iblfoodone=Label(main,text="1. How often do you eat fast food?:",fg="blue")
Iblfoodone.grid(column=0,row=30)

rbn1=Radiobutton(main, text="Never", variable=v, value=1).grid(column=1,row=30)
rbn2=Radiobutton(main, text="Once a month", variable=v, value=2).grid(column=1,row=31)
rbn3=Radiobutton(main, text="Once a week", variable=v, value=3).grid(column=1,row=32)


Iblfoodtwo=Label(main,text="2. What would you generally eat for a snack?:",fg="blue")
Iblfoodtwo.grid(column=0,row=33)

rbn4=Radiobutton(main, text="A piece of fruit", variable=v, value=4).grid(column=1,row=33)
rbn5=Radiobutton(main, text="A museli bar", variable=v, value=5).grid(column=1,row=34)
rbn6=Radiobutton(main, text="Something sweet", variable=v, value=6).grid(column=1,row=35)


Iblfoodthree=Label(main,text="3. How many meals a day would you consume?:",fg="blue")
Iblfoodthree.grid(column=0,row=36)

rbn7=Radiobutton(main, text="4-5", variable=v, value=7).grid(column=1,row=36)
rbn8=Radiobutton(main, text="2-3", variable=v, value=8).grid(column=1,row=37)
rbn9=Radiobutton(main, text="1", variable=v, value=9).grid(column=1,row=38)

#BMI Calculator
IblHeight=Label(main,text="Height:",fg="blue")
IblHeight.grid(column=0,row=0)
entHeight=Entry(main)
entHeight.grid(column=1,row=0)
IblWeight=Label(main,text="Weight:",fg="blue")
IblWeight.grid(column=0,row=1)
entWeight=Entry(main)
entWeight.grid(column=1,row=1)



def callback(event):
    print "You clicked on ",event.x,event.y
    global x,y
    if 7<event.x and event.x<126 and 79<event.y and event.y<131:
        graphics.delete(ALL)
        graphics.create_image(5,5,anchor=NW,image=mainscreen)
        rbn1=Radiobutton(main, text="Never", variable=v, value=1).grid(column=1,row=30)

    elif 128<event.x and event.x<249 and 80<event.y and event.y<131:
        graphics.delete(ALL)
        graphics.create_image(5,5,anchor=NW,image=mainscreen)

    elif 255<event.x and event.x<373 and 80<event.y and event.y<132:
        graphics.delete(ALL)
        graphics.create_image(5,5,anchor=NW,image=infoscreenone)
        infovalue = infovalue + 1
        if infovalue==1 and 452<event.x and event.x<496 and 449<event.y and event.y<496:
            graphics.delete(ALL)
            graphics.create_image(5,5,anchor=NW,image=infoscreentwo)
            infovalue=infovalue+1
            if infovalue==2 and 452<event.x and event.x<496 and 449<event.y and event.y<496:
                graphics.delete(ALL)
                graphics.create_image(5,5,anchor=NW,image=infoscreenthree)
            elif infovalue==2 and 393<event.x and event.x<434 and 446<event.y and event.y496:
                graphics.delete(ALL)
                graphics.create_image(5,5,anchor=NW,image=infoscreentwo)
            else:
                print "no noob again"
        else:
            print "no noob"
    else:
        print "out of margin"

#Canvas
graphics = Canvas(main,width=500,height=500)
graphics.grid(row=0,column=0, columnspan=15, rowspan=60)

#Background
mainscreen = PhotoImage(file="mainscreen.gif")
graphics.create_image(5,5,anchor=NW,image=mainscreen)

#Import Images
titlebar = PhotoImage(file="titlebar.gif")
dietbutton = PhotoImage(file="dietbutton1.gif")
exercisebutton = PhotoImage(file="exercisebutton1.gif")
infobutton = PhotoImage(file="infobutton1.gif")
mychoicebutton = PhotoImage(file="mychoicebutton1.gif")
plain = PhotoImage(file="plain.gif")
painting = PhotoImage(file="painting.gif")
infoscreenone = PhotoImage(file="inforestaurant copy.gif")
infoscreentwo = PhotoImage(file="inforestaurant2 copy.gif")
infoscreenthree = PhotoImage(file="inforestaurant3 copy.gif")


#Place Images







main.bind("<Button-1>",callback)

main.mainloop()
