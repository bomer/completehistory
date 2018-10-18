# Excerxise 5 question 4

from random import*
number = int(random()*100)+1

guess = int(raw_input("Please enter ur guess: "))

if (guess<number):
        print "Higher!"
if (guess>number):
    print "Lower!"

while (guess!=number):
    guess = int(raw_input("Please enter ur guess: "))
    if (guess<number):
        print "Higher!"
    if (guess>number):
        print "Lower!"    

if (guess==number):
    print
    print
    print "That is my number"
   
print
print
print "Thankyou for choosin and usin my program"
