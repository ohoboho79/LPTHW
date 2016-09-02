from sys import argv

script, filename = argv

print "Opening the file ..."
target = open(filename, 'r')
print "Opening mode : ", target.mode
print target.read()

target.close()

print "Closed or not : ", target.closed
