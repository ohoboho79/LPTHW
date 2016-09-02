from sys import argv

script, age, height, weight = argv

print   "The scrip is called:", script
print   "First variable is:", age
print   "Second variable is:", height
print   "Third variable is:", weight

age = raw_input ("How old are you (years):   ")
height = raw_input ("How tall are you (cm):    ")
weight = raw_input ("How much doyou weight (kg):    ")

print   "So you're %r old, %r tall, %r heavy." % (
    age, height, weight)