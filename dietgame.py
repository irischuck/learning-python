from sys import exit

def week1():
    print "Which food will you eat every day of Week 1?"
    print "Apples, oranges, or bananas?"

    choice = raw_input("> ")
    if choice == "apples":
        print "Good, you'll keep the doctor away."
        week2(choice)
    elif choice == "oranges":
        print "Good, you'll have plenty of vitamin C."
        week2(choice)
    elif choice == "bananas":
        end_diet_bananas()
    else:
        end_diet()

def week2(myChoice):
    print "You had %s last week" % myChoice + "."
    print "What beverage will you drink every day of Week 2?"
    print "Coffee or tea?"

    choice = raw_input("> ")
    if choice == "tea":
        end_diet_tea()
    elif choice == "coffee":
        end_diet_coffee()
    else:
        end_diet()

def end_diet():
    print "Wow. You suck at maintaining a diet."
    replay()

def end_diet_tea():
    print "Great choice! Congratulations, you have successfully finished your diet."
    replay()

def end_diet_coffee():
    print "Too much coffee is bad for the heart."
    print "You have failed your diet."
    replay()

def end_diet_bananas():
    print "Your bananas were stolen by minions."
    print "You were unable to start your diet."
    replay()

def start():
    print "Do you want to start the Diet game?"
    choice = raw_input("> ")
    if choice == "yes":
        week1()
    elif choice == "no":
        nodiet()
    else:
        nodiet()

def restart():
    choice = raw_input("> ")
    if choice == "yes":
        week1()
    elif choice == "no":
        end()
    else:
        nodiet()

def nodiet():
    print "You should try harder in life."
    replay()

def replay():
    print "Would you like to play again?"
    print "To play again, type 'yes'."
    print "To end, type 'no'."
    restart()

def end():
    exit()

start ()
