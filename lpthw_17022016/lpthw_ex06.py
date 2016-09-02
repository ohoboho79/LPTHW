#Decler variable of type "string"
x = "There are %d types of people." %10

#Decler variable of type "string"
binary = "binary"

#Decler variable of type "string"
do_not = "don't"

#Decler variable of type "string"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "Isaid: %r." %x
print "I also said: '%s'." %y

#Decler variable of type "boollean"
hilarious = False

#Decler variable of type "string"
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

#Decler variables of type "string"
w = "This joke is the left side of ..."
e = " a string with a right side."

#Concatenation of two strings
print w+e