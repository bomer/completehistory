# Weather report

weather=raw_input("Please enter the weather, Sunny, Overcast or Raining: ")

if (weather=="Sunny"):
    Answer=raw_input("Do you want to go to the beach?: ")
    if (Answer=="yes"):
        print "Have fun"
    elif (Answer=="no"):
        print "good, because the beach sucks, i hate sand"
elif (weather=="Overcast"):
    Answer2=raw_input("Do you wanna go to the movies?: ")
    if(Answer2=="yes"):
        print "good choice, because movies pwn!"
    elif(Answer2=="no"):
        print "I HATE U, WATCH A MOVIE!"
elif (weather=="Raining"):
    print "sucked in, rain is shit, but at least u can watch a movie, or play a game, SO DO IT!"
