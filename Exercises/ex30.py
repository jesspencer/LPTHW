people = 30
cars = 400
buses = 1500

# compares the variabble 400 : 30
if cars < people:
    print "We should take the cars."
#if 400 is greater than 30 print "We should not take the cars"
elif cars > people:
    print "We should not take the cars."
#if 400 is not greater than 30 and also 400 and is not less than 30 then print "we cant decide"
else:
    print "We can't decide."
# compares 1500 to 400; if 1500 is greater than 400 print too many buses
if buses > cars:
    print "That's too many buses."
# prints the statement if 1500 is less than 400 and also 1500 is greater than 400
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

'''Study Drills
1. Try to guess what elif and else are doing.
Ans: The 'if' part is turning the statement into a conditional one; the 'else: and elif' is the 'then' part of the conditional

2. Change the numbers of cars, people, and buses, and then trace through each if-statement to see what will be printed.
Ans:changed the numbers and got new answers to the expressions

3. Try some more complex boolean expressions like cars > people and buses < cars.
Done
4. Above each line, write an English description of what the line does.
Done
'''
