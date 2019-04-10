#while-loops

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" %i
    numbers.append(i)


    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" %i

    print "The numbers: "

    for num in numbers:
        print num


'''Study drills
1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable
2. Now use this function to rewrite the script to try differnt Numbers
3. Add another variabel tot he function arguments that you can pass in that lets you cahge the +1 on line 8, 
'''
