import time 

def beginningStory():
    print "There is a fat, tan guinea pig waiting at the door with a clipboard."
    print " "
    print """MYSTERY GUINEA PIG: \"Hello, welcome to Cavy House! Here, you will meet fellow guinea pigs and
     your goal is to become friends with all of them.\""""
    print " "
    print "You nod and shake his paw."
    print " "
    
    while True:
        ans = raw_input("MYSTERY GUINEA PIG: \"Are you ready?\" (Y/N): ").upper()
        time.sleep(.5)
        if ans in ["Y", "YES"]:
            print "MYSTERY GUINEA PIG: \"Good. Let's make some friends.\""
            break
        if ans in ["N", "NO"]:
            print "MYSTERY GUINEA PIG: \"Come on, are you sure?\""
        else:
            print "MYSTERY GUINEA PIG: \"I didn't get that.\""
     
    storyTime1()

def storyTime1():
    print "MYSTERY GUINEA PIG: \"First, we'll have to get acquainted. My name is Taco.\""
    charName = raw_input("TACO: \"What's yours?\" ").upper()[:20]
    
    while True:
        print "Your name is", charName, "?"
        charNameCheck = raw_input("TACO: \"Is this correct?\": ").upper()[:20]
        time.sleep(1)
        if charNameCheck in ["Y", "YES"]:
            print "TACO: \"Well it's a pleasure to meet you.\""
            time.sleep(1)
            global charName
            break
        if charNameCheck in ["N", "NO"]:
            print "TACO: \"Okay, let's start over.\"" 
            charName = raw_input("TACO: \"Type your name in again\": ").upper()[:20]
            time.sleep(1)
        else:
            print "TACO: \"You need to make a choice.\""
    
    storyTime2()
    
def storyTime2():
    time.sleep(2)
    print " "
    print "TACO: \"Okay, ", charName, " -- can you come to the desk for a second?\""
    print "You walk towards the desk. There is a FORM."
    time.sleep(1)
    print " "
    print "TACO slides the FORM to you."
    print "TACO: \"Can you fill this out? It's basically a questionnaire to get to know you better.\""
    time.sleep(1)
    print " "
    print "You take the FORM and begin to fill it out."
    time.sleep(1)
    favFruit = raw_input("a. What is your favorite fruit?: ").upper()[:20]
    time.sleep(1)
    favVegetable = raw_input("b. What is your favorite vegetable?: ").upper()[:20]
    time.sleep(1)
    favHidingSpot = raw_input("c. Where is your favorite hiding spot?: ").upper()[:20]
    print " "
    print "You look at TACO and hand the FORM over. He takes a look."
    time.sleep(1)
    print ". . . "
    time.sleep(1)
    print ". . ."
    time.sleep(1)
    print ". . ."
    time.sleep(1)
    print "TACO: \"So your favorite fruit is", favFruit, "and your favorite vegetable is", favVegetable, "and your favorite hiding spot is", favHidingSpot, "?"
    
    while True:
        print "TACO: \"Just to make sure, you like", favFruit, "." 
        favFruitCheck = raw_input("TACO: \"Is that right?\" (Y/N): ").upper()[:20]
        time.sleep(1)
        if favFruitCheck in ["Y", "YES"]:
            print "TACO: \"Great! It's mine too.\""
            global favFruit
            break
        if favFruitCheck in ["N", "NO"]:
            print "TACO: \"Okay, let's start over.\"" 
            favFruit = raw_input("TACO: \"What's your favorite fruit?\": ").upper()[:20]
        else:
            print "TACO: \"I didn't get that.\""
    
    time.sleep(1)
    
    while True: 
        print "\"And you like", favVegetable, "too?\""
        favVegetableCheck = raw_input("TACO: \"Is this correct?\" (Y/N): ").upper()[:20]
        time.sleep(1)
        if favVegetableCheck in ["Y", "YES"]:
            print "TACO: \"You're making me hungry!\""
            global favVegetable
            break
        if favVegetableCheck in ["N", "NO"]:
            print "TACO: \"Okay, let's start over.\"" 
            favVegetable = raw_input("TACO: \"What's your favorite vegetable?\": ").upper()[:20]
        else:
            print "TACO: \"I didn't get that.\""

    time.sleep(1)

    while True: 
        print "\"And your hiding spot is", favHidingSpot, ".\""
        favHidingSpotCheck = raw_input("TACO: \"Is that correct?\" (Y/N): ").upper()[:20]
        time.sleep(1)
        if favHidingSpotCheck in ["Y", "YES"]:
            print "TACO: \"Sounds cozy!\""
            global favHidingSpot
            break
        if favHidingSpotCheck in ["N", "NO"]:
            print "TACO: \"Okay, let's start over.\"" 
            favHidingSpot = raw_input("TACO: \"What's your favorite hiding spot?\": ").upper()[:20]
        else:
            print "TACO: \"I didn't get that.\""
    
    storyTime3()
    
def storyTime3():        
	print "TACO: \"Alright, so I think we're all done here.\""
	print "TACO hands you the CAVY HOUSE KEY."
	charItemList = ["CAVY HOUSE KEY"]
	time.sleep(1)
	print "You now have the following in your possession: ", charItemList
	print " "
	print "You are about to head out the door when TACO comes waddling after you."
	print " "
	print "TACO: \"I almost forgot! Here's a small gift for you to welcome you to our little home.\""
	print "You receive CARROT STICK."
	time.sleep(!)
	charItemList.append("CARROT STICK")
	print " "
	print "You now have the following in your posession: ", charItemList
	
def main():
    beginningStory()
    
main()