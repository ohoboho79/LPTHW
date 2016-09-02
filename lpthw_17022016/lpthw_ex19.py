def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print 'We can call the function in a loop, calling it 10 times'
for i in range(10):
    cheese_and_crackers(20 + i+1,30 - i-1)
    
print "User input:"
cheese = int(raw_input("amount_of_cheese:"))
crackers = int(raw_input("amount_of_crackers:"))
for i in range (10):
    cheese_and_crackers(cheese +i+1, crackers -i-1)

