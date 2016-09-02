people = 15
cars = 10
trucks = 4

if cars > people:
    print "We should take cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
elif (people < trucks or trucks > 5) and (cars != 10 or cars>=20):
    print "Smehoria."
else:
    print "Fine, let's stay home than."
