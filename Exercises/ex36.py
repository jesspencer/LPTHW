from sys import exit
# Branches and Fuctions Game.

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input('>')

    if next == "none":
        print "None is not an option here. Choose!"
        exit(0)

    if next < 50:
        print " Nice, you're not greedy, you win!"
        exit(0)
    else:
        print "Dead! you greedy bastard!"
#defining START
def start():
    print "You are in a dark room."
    print "There are two red doors on your left and two yellow doors on your right."
    print "Which do you take?"

    next = raw_input('>')

    #defining LEFT and RIGHT

    if next == "left":
        rose_garden()
    elif next == "right":
        space_ship()
    elif next == "none":
        print gold_room()
    else:
        dead()

def dead():
    print "YOU DIED!"
    print "Awe, Good Job!"
    exit(0)

def rose_garden():
    print "There is a garden here."
    print "The garden is past another gate."
    print "Do you open the other gate or stay in garden?"

    next = raw_input(">")

    if next == "open door":
        bear_room()
    elif next == "stay":
        print "You stayed, enjoy the flowerse. Later!"
    else:
        print "Dead, you stumble around in the room until you starve."

def space_ship():
    print "There is a space ship here."
    print "A person on the ship wants your name."
    print "Do you tell them your name yes or no ?"

    next = raw_input('>')

    if next == "no":
        dead()
    elif next == " yes":
        gold_room()
    else:
        rose_garden()

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next == raw_input('>')

    if next == "take honey":
        print " The bear looks at you then slaps your face off."
    elif next == "taunt bear" and not bear_moved:
        print "The bear has moved from the door. You can go through it now."
        bear_moved = True
    elif next == "taunt bear" and bear_moved:
        print "The bear gets pissed off and chews your left off."
    elif next == "open door" and bear_moved:
        space_ship()
    else:
        print " I got no idea what that means."
#STARTs
start()
'''
1. Draw a map of the game and how you flow through it
map: First the user sees doors to left and door on right
    Second, if the user picks left door
    Then user is take to the rose_garden path
    And if the user choses right then the user is taken to space_ship path
    Also if the user choses none then the user dies
    Lastly if the user does not enter left righ nor none then the user dies

2. Fix all mistakes
done
3. Write comments for the functions you do not understand. Remember doc comments?
done
4. Add more to the game.
done; created more to the game "my_game"
5. The gold_room has a wierd way of getting you to type a number. What are all of the bugs?
Can you make it better by just checking if there is a 1 or 0 are in the number?

'''
