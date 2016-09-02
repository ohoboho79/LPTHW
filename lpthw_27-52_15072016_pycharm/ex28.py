
print "1:","(True and True) is True:", True and True
#True

print "2:", "(False and True) is False:", False and True
#False

print "3:", "(1 == 1 and 2 == 1) is False:",1 == 1 and 2 == 1
#False

print "4:", "(\"test\" == \"test\") is True:", "test" == "test"
#True

print "5:", "(1 == 1 or 2 != 1) is True:", 1 == 1 or 2 != 1
#True

print "6:", "(True and 1 == 1) is True:", True and 1 == 1
#True

print "7:","(False and 0 != 0) is False:", False and 0 != 0
#False

print "8:", "(True or 1 == 1) is True:", True or 1 == 1
#True
 
print "9:", "(\"test\" == \"testing\") is False:", "test" == "testing"
#False

print "10:", "(1 != 0 and 2 == 1) is False:", 1 != 0 and 2 == 1
#False

print "11:", "(\"test\" != \"testing\") is True:", "test" != "testing"
#True

print "12:","(\"test\" == 1) is False:", "test" == 1
#False

print "13:", "(not (True and False)) is True:", not (True and False)
#True

print "14:", "(not (1 == 1 and 0 != 1)) is False:", not (1 == 1 and 0 != 1)
#False

print "15:", "(not (10 == 1 or 1000 == 1000)) is False", not (10 == 1 or 1000 == 1000)
#False

print "16:", "(not (1 != 10 or 3 == 4)) is False:", not (1 != 10 or 3 == 4)
#False

print "17:", "(not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")) is True:", not ("testing" == "testing" and "Zed" == "Cool Guy")
#True

print "18:", "(1 == 1 and (not (\"testing\" == 1 or 1 == 0))) is True:", 1 == 1 and (not ("testing" == 1 or 1 == 0))
#True and (not False)
#True and True
#True

print "19:", "(\"chunky\" == \"bacon\" and (not (3 == 4 or 3 == 3))) is False:", "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
#False and (not True)
#False


print "20:", "(3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\"))) is False:", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
#True and (not True)
#False
