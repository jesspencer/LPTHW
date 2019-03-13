#!/usr/bin/env python2.7

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

'''
Study Drills
3. Write at least one more function of your own design, and run it 10 different ways
'''

def jessica_work_schedule(mon, tues, wed):
    print "This is Jessica's schedule for Monday is %s" % mon
    print "This is Jessica's work schedule for Tuesday %s" % tues
    print "This is Jessica's work schedule for Wednesday %s" % wed
    print "She only works three days \n"


print "We can just give the numbers directly"
jessica_work_schedule(5-10, 10-3, 3-11)

print "Or, lets use variables for our script"
mon = '5-10'
tues = '10-2'
wed = '3-11'

print "We can also do math with the schedules:"
jessica_work_schedule(5 + 0,  4 + 1, 7 +1)

print "And we can combine the two, variables and math:"
jessica_work_schedule(str(mon) + 4, str(tues) + 3, str(wed) + 3)
