from sys import argv

script, filename = argv

txt = open (filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Closed or not : ", txt.closed

print "Type the filename again:"
file_again = raw_input ("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
print "Name of the file: ", txt_again.name
print "Closed or not : ", txt_again.closed
print "Opening mode : ", txt_again.mode
print "Softspace flag : ", txt.softspace
