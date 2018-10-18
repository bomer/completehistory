# Assignment 2
# Thai21

flag=21
player=1

while flag>0:
    flag=flag-take
    player=1
    print "There are",flag,"flags left"
    print "It is player",player,"move"
    take=int(raw_input("Please take 1, 2 or 3 flags: "))
    if flag<=0:
        print "Player 1 Wins"
    flag=flag-take
    player=2
    print "There are",flag,"flags left"
    print "It is player",player,"move"
    take=int(raw_input("Please take 1, 2 or 3 flags: "))
    if flag <=0:
        print "Player 2 Wins"

#if flag<=0:
 #   if player==2:
  #      print "Player 2 Wins"
   # else:
    #    print "Player 344352Wins"
 
