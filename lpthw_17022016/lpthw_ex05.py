# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
age = 35 # not a lie
inch_height = float (74.00) #inches
height = float (inch_height * 2.54)
lbs_weight = 180.00 #lbs
weight = lbs_weight * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)