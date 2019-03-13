#!/usr/bin/env python2.7

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do thse two on one line too, how?
indata = open(from_file).read()

print "Does the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

"""
Study Drills
2. Try to make it more friendly to use by removing features
"""
