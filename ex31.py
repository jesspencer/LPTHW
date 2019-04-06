print "You enter a dark room with two doors. Do you go through door #1 or door #2 or #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jackets chothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
    print "You stare at Mrs. Hill."
    print "1. Meet Nina Simone."
    print "2. Meet Madona."
    print "3. Meet Seal."
    print "4. Meet death. Look death in the face!"

    celebrity = raw_input("> ")

    if celebrity == "1":
        print "Your making beautiful music with the great creater. Good Job!"
    elif celebrity == "2":
        print "You and Seal are getting married. Congradulations!"
    else:
        print "You have stared death in the face! Done good!"

else:
    print "You stumble around and fall on a knife and die. Good job!"

''' Study Drills
Make new parts of the game and change what decisions to make. Expand the game out ad much as you can before it gets ridculous.
'''
