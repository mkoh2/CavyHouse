def beginningStory():
    print """Hello, welcome to Cavy House! Here, you will meet fellow guinea pigs and
     your goal is to become friends with all of them."""

    while True:
        ans = raw_input("Are you ready? (Y/N): ").upper()
        if ans in ["Y", "YES"]:
            print "Good. Let's make some friends."
            break
        if ans in ["N", "NO"]:
            print "Come on, are you sure?"
        else:
            print "You need to make a choice."
     
    storyTime1()

def storyTime1():
    print "First, we'll have to get acquainted. My name is Taco."
    charName = raw_input("What's yours? ").upper()[:20]
    
    while True:
        print charName
        charNameCheck = raw_input("Is this correct?: ").upper()
        if charNameCheck in ["Y", "YES"]:
            print "Well it's a pleasure to meet you."
            global charName
            break
        if charNameCheck in ["N", "NO"]:
            print "Okay, let's start over." 
            charName = raw_input("Type your name in again: ").upper()[:20]
        else:
            print "You need to make a choice."
    
    storyTime2()
    
def storyTime2():
    print "Okay, ", charName, " -- time to meet some guinea pigs!"

beginningStory()