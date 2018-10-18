#search

from Tkinter import*

search=""

root = Tk()
root.title("Trial")

#window
root.canv = Canvas ( root, width=100, height=100)
root.canv.grid ( row=0, column=0)

text= Text(root.canv)
text.pack(ipadx=50,ipady=50)

#search buttons

lblsearch=Label(root,text="Search")
lblsearch.grid(column=1,row=1)
entsearch=Entry(root)
entsearch.grid(column=2,row=1)

#button
def Search():
    scount=[1.0,1.1]
    count=0
    search=entsearch.get()
    sletters=[""]*len(search)
    match=0
    print search
    #print text.get(1.0,END)
    #print text.get(1.1,1.2)
    #print len(search)
    #print text.get(scount[0],scount[1])
    while count!=len(search):
        sletters[count]+=search[count]
        count+=1
    print sletters
    count=0
    
    while match!=len(search):
        print"score"
        if text.get(scount[0],scount[1])==sletters[count]:
            print"1"
            match+=1
            count+=1
            scount[0]=scount[1]
            scount[1]+=0.1
            print"2"
        else:
            print"3"
            match=0
            count=0
            scount[0]=scount[1]
            scount[1]+=0.1
            print"4"
    if match>1:
        print "word found"
    else:
        print"no find"
    
    

cmdsearch=Button(root,text="Search",command=Search)
cmdsearch.grid(column=1,row=2)


root.mainloop()
