def cheese_and_crackers(cheese_count, boxes_of_crakers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crakers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our scrpit:"
amount_of_cheese = 10
amount_of_crakers = 50

cheese_and_crackers(amount_of_crakers, amount_of_crakers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "We can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crakers + 1000)

print 'We can pass a function as arguments.'
print 'We can now ask the user for the number of cheese and crackers'
cheese_and_crackers(int(raw_input("Cheese amount:")), int(raw_input("Crackers amount:")))

print 'We can assign the function to a variable and simply call it by its new name'
foo = cheese_and_crackers
foo(20,30)

print 'We can call the function in a loop, calling it 10 times'
#for i in range(10):
    #cheese_and_crackers(int(raw_input("Cheese amount:")) - i,  #int(raw_input("Crackers amount:")) + i)
    
print 'We can call the function in a loop, calling it 10 times'
amount_of_cheese = int(raw_input("Cheese amount:"))
amount_of_crakers = int(raw_input("Crackers amount:"))
for i in range(10):
    cheese_and_crackers(amount_of_cheese - i, amount_of_crakers  + i)