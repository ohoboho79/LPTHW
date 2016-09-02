people = int (raw_input("People:"))
cats = int (raw_input("Cats:"))
dogs = int (raw_input("Dogs:"))

if people < cats:
    print "Too many cats! The worls is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 15
cats = dogs + 1
people -= cats

if people >= dogs:
    print "People are greater then or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if people != cats and dogs == cats:
    print "Egati bozata."
else:
    print "Kauza parcuca."
print dogs, cats, people