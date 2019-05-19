#Doing things with lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list. Let's fix that."
#turns a variable into a list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Bannana", "Girl", "Boy"]

while len(stuff) != 10:
    #now next_one is just the word boy
    next_one = more_stuff.pop()
    print "Adding:", next_one
    added something after the word boy
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things stuff."
#this prints the second item Left to Right (oranges)
print stuff[1]
#this prints the first item right to left
print stuff[-1] #whoa fancy
#prints corn
print stuff.pop()
joins lists together
print ' '.join(stuff) #what? cool!
joins # with the list between 3:5
print '#'.join(stuff[3:5]) #super stellar!

'''
Study Drills

1. Take each function that is called, and go through the steps outlined above to translate threm to what Python does
done
2.Translate these two ways to view the function calls. For example, " ".join(things) reads as, "join
things with '' between them. "Meanwhile, join ('', things) means, "Call join with '' and things." Understand
how they are really the same thing.
done
3. Go read about "object oriented programming" online. Confused? I was too. Do not worry. You will learn enough to be
dangerous, and you can slowly learn more later.
done
4. Read up on what a class is in Python. Do not read about how other languages.
done
5. What's the relationship between dir(something) and the "class" of something?
The "dir" stands for dictionary, which are unordered lists. A dictionary is an ordered list. Class can be ordered.
6. If you do not have any idea what I am talking about, do not worry. Programmers like to feel smart, so they
invented object-oriented programming, named it OOP, and then used  it way too much. If you think that's hard,
you should try to use "functional programing."

'''
