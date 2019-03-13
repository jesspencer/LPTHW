#!/usr/bin/env python2.7

from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write theese to the file."

target.write("%r \n %r \n %r ") % (line1, line2, line3)

print "And finally, we close it."
target.close()

"""
Study Drills

3. There is too much repetition in this file. Use strings, formats, and escapes to
print out line1, line2, and line3 with just one target.write() command instead
of six.
"""
