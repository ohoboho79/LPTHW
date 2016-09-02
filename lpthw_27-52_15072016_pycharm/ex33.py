i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i =i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

#Study drills
#1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#2. Use this function to rewrite the script to try different numbers.

def convert (n):
    i = 0
    numList = []

    while i < n:
        print "List item: %d" % i
        numList.append(i)
        i = i + 1
        print numList

print "\nConvert"
n = int(raw_input("Input n: "))
convert(n)
print "Convert"

#3. Add another variable to the function arguments that you can pass in that lets you change
# the + 1 on line 8 so you can change how much it increments by.
#4. Rewrite the script again to use this function to see what effect that has.

def convert1 (n, m):
    i = 0
    numList1 = []

    while i < n:
        print "List item: %d" % i
        numList1.append(i)
        i = i + m
        print numList1

print "\nConvert1"
n = int(raw_input("Input n: "))
m = int(raw_input("Input m: "))
convert1(n, m)
print "Convert1"

#5. Write it to use for-loops and range.
# Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?

def convert2 (n, m):
    numList2 = range(0, n, m)

    #6print "List item: %d" % i
    for i in numList2:
        print "Adding %d to the list." % i
        print numList2

print "\nConvert2"
n = int(raw_input("Input n: "))
m = int(raw_input("Input m: "))
convert2(n, m)
print "Convert2"
