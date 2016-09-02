#age = raw_input ("How old are you (years):   ")
#height = raw_input ("How tall are you (cm):    ")
#weight = raw_input ("How much doyou weight (kg):    ")

#print   "So you're %r old, %r tall, %r heavy." % (
#    age, height, weight)

from sys import argv

script, first, second, third = argv

print   "The scrip is called:", script
print   "First variable is:", first
print   "Second variable is:", second
print   "Third variable is:", third