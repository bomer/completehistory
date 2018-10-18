#checkers command line

board=[["B"," ","B"," ","B"," ","B"," "],
       [" ","B"," ","B"," ","B"," ","B"],
       ["B"," ","B"," ","B"," ","B"," "],
       [" "," "," "," "," "," "," "," "],
       [" "," "," "," "," "," "," "," "],
       [" ","R"," ","R"," ","R"," ","R"],
       ["R"," ","R"," ","R"," ","R"," "],
       [" ","R"," ","R"," ","R"," ","R"]]

turn="R"
Rpieces=12
Bpieces=12
x=0
y=0
px=0
py=0
a=1

def Board(board):
    print "A",board[0][0:8]
    print "B",board[1][0:8]
    print "C",board[2][0:8]
    print "D",board[3][0:8]
    print "E",board[4][0:8]
    print "F",board[5][0:8]
    print "G",board[6][0:8]
    print "H",board[7][0:8]
    print"    1","   2","   3","   4","   5","   6","   7","   8"

def Value(movea):
    global x,y,px,py
    if movea[0]=="A":
        y=0
    elif movea[0]=="B":
        y=1
    elif movea[0]=="C":
        y=2
    elif movea[0]=="D":
        y=3
    elif movea[0]=="E":
        y=4
    elif movea[0]=="F":
        y=5
    elif movea[0]=="G":
        y=6
    elif movea[0]=="H":
        y=7
    x=int(movea[1])-1
    if px==0 and py==0:
        px=x
        py=y

def Check(px,py,x,y):
    if turn=="R":
        if board[y][x]==" ":
           if x==px+1 and y==py-1 and board[y][x]==" ":
                return 1
           elif x==px-1 and y==py-1 and board[y][x]==" ":
                return 1
           else:
                return 0
    elif turn=="B":
        if board[y][x]==" ":
           if x==px+1 and y==py+1 and board[y][x]==" ":
                return 1
           elif x==px-1 and y==py+1 and board[y][x]==" ":
                return 1
           else:
                return 0

def Take(board,turn):
    for a in range(0,8):
        for b in range(0,8):
            if turn=="B":
                if board[a][b]=="B":
                    if b<7:
                        if board[b+1][a+1]=="R":
                            print "yes2"
                    if b>0:
                        if board[b-1][a+1]=="R":
                            print"yes"
            elif turn=="R":
                if board[a][b]=="R":
                    if b<7:
                        if board[b+1][a-1]=="B":
                            print "yes3"
                    if b>0:
                        if board[b-1][a-1]=="B":
                            print "yes1"
                
def Turn(turn):
    if turn=="R":
        print "Red's turn"
    else:
        print "Blacks turn"

                   
while Bpieces!=0 and Rpieces!=0:
    Board(board)
    Take(board,turn)
    print
    Turn(turn)
    print
    px=0
    py=0
    if turn=="R":
        move1=raw_input("What piece would you like to move: ")
        Value(move1)
        while board[py][px]!=turn:
            px=0
            py=0
            print"Not yours!"
            move1=raw_input("What piece would you like to move: ")
            Value(move1)
        a+=1
        move2=raw_input("Where would you like to move it: ")
        Value(move2)
        while not Check(px,py,x,y):
            x=0
            y=0
            print"Not free!"
            move2=raw_input("Where would you like to move it: ")
            Value(move2)
        board[py][px]=" "
        board[y][x]=turn
        turn="B"

    else:
        move1=raw_input("What piece would you like to move: ")
        Value(move1)
        while board[py][px]!=turn:
            px=0
            py=0
            print"Not yours!"
            move1=raw_input("What piece would you like to move: ")
            Value(move1)
        a+=1
        move2=raw_input("Where would you like to move it: ")
        Value(move2)
        while not Check(px,py,x,y):
            x=0
            y=0
            print"Not free!"
            move2=raw_input("Where would you like to move it: ")
            Value(move2)
        board[py][px]=" "
        board[y][x]=turn
        turn="R"
