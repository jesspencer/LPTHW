#!usr/bin/env python2.7

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches talls." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eys and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is trickey, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

'''
study Drills

1 change all the variables so that there isn't the my_in front.

2 try more formate characters. %r is a very useful one. It's like saying print this no matter what

'''

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# try to get this right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
'''
3 write measurements that convert inches and pounds to centimeters

'''
inch = 1 #inch
a_centimeter = 2.54 #centimeters needed for 1 inch
twelve_inches = 12

print "\n"
print "Converting and Measuring"

print "A single inch is %r in centimeters." % a_centimeter
print "Then twelve inches is %d in centimeters" % (twelve_inches * a_centimeter)
