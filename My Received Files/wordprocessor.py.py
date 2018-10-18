#word processor
from Tkinter import *

root = Tk()
#Canvas
root.canv = Canvas ( root, width=150, height=150,
scrollregion=(0, 0, 150, 100) )
root.canv.grid ( row=0, column=0)

lbltextsize=Label(root,text="Text size: ")
lbltextsize.grid(column=0,row=1,rowspan=6)

#text box
textWidget = Text(root.canv)
textWidget.pack(ipadx=100,ipady=50)

#scroll bar
root.canv = Canvas ( root, width=150, height=150,
scrollregion=(0, 0, 150, 550) )
root.canv.grid ( row=0, column=0)
root.scrollY = Scrollbar ( root, orient=VERTICAL,
command=root.canv.yview )
root.scrollY.grid ( row=0, column=1, sticky=N+S )

root.scrollX = Scrollbar ( root, orient=HORIZONTAL,
    command=root.canv.xview )
root.scrollX.grid ( row=1, column=0, sticky=E+W )

root.canv["xscrollcommand"]  =  root.scrollX.set
root.canv["yscrollcommand"]  =  root.scrollY.set



def Files():
    menu=Menu(root)
    root.config(menu=menu)
    filemenu=Menu(menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=New)
    filemenu.add_command(label="Open", command=Open)
    filemenu.add_command(label="Save", comman=Save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=Exit)

def New():
    root=Tk()
    Canvas()
    root.mainloop()

def Open():
    print "open"
    load=raw_input("Wat would you like to load (Do not include extension .txt) : ")
    textWidget.delete(1.0, END)
    f=open(load+".txt","r")
    textWidget.insert(END, f)    
    f.close()
    

def Save():
    print"Saved"
    save=raw_input("Wat would you like to save it under: ")
    text=textWidget.get(1.0, END)
    f=open(save+".txt","w")
    f.write(text)
    f.close()

def Exit():
    root.destroy()

Canvas()
Files()
root.mainloop()
