#text buttons, etc.

from Tkinter import*
import tkFont

root=Tk()

root.canv = Canvas ( root, width=150, height=150)
root.canv.grid ( row=0, column=0)

textWidget = Text(root.canv,font=font)
textWidget.pack(ipadx=50,ipady=50)

font=tkFont.Font(size=size,weight=weight,slant=slant,underline=underline,family=family)

#prefill
enttextsize.insert(1,10)
entbold.insert(1,"bold")
entitalic.insert(1,"italic")
entunderline.insert(1,0)
entfamily.insert(1,"modern")

#get
size=int(enttextsize.get())
weight=entbold.get()
slant=entitalic.get()
underline=int(entunderline.get())
family=entfamily.get()

#text size
lbltextsize=Label(root,text="Text size: ")
lbltextsize.grid(column=1,row=9)
enttextsize=Entry(root)
enttextsize.grid(column=2,row=9)

#text bold
lblbold=Label(root,text="Bold")
lblbold.grid(column=1,row=8)
entbold=Entry(root)
entbold.grid(column=2,row=8)

#text text family
lblfamily=Label(root,text="Family")
lblfamily.grid(column=1,row=7)
entfamily=Entry(root)
entfamily.grid(column=2,row=7)

#text italic
lblitalic=Label(root,text="Italic")
lblitalic.grid(column=1,row=6)
entitalic=Entry(root)
entitalic.grid(column=2,row=6)

#text underline
lblunderline=Label(root,text="Underline")
lblunderline.grid(column=1,row=5)
entunderline=Entry(root)
entunderline.grid(column=2,row=5)

font=tkFont.Font(size=size,weight=weight,slant=slant,underline=underline,family=family)


root.mainloop()
