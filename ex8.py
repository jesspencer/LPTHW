#!usr/bin/env Python2

formatter = "%r %r %r %r" # variable

print formatter % (1,2,3,4) # this line prints 1,2,3,4
print formatter % ("one", "two", "three", "four") # this line prints one two three four
print formatter % (True, False, False, True)  # this line prints T,F,F,T
print formatter % (formatter, formatter, formatter, formatter) # line prints %r in group of 4
print formatter % ( # this prints the following for lines
    "I had this thing.",
    "That you could tye up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

'''
Study Drills
1   Do you checks
--done
2   Notice that the last line of output uses both single-quotes and double-quotes
for individual pieces. Why do you think that is?
--not sure why the last line uses single and double qutoes
'''
