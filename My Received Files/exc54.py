# Excerxise 5 question 4

from random import*
number = int(random()*10)+1

guess = int(raw_input("Please enter ur guess: "))

while (guess!=number):
    guess = int(raw_input("Please enter ur guess: "))
    if (guess==number):
        print "That is my number"
    elif (guess<number):
        print "Higher!"
    else:
        print "Lower!"
        guess = int(raw_input("Please enter ur guess: "))


print
print
print "Thankyou for choosin and usin my program"
