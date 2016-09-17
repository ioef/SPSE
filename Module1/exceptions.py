#!/usr/bin/env python

number1 = raw_input("Give the first number:")
number2 = raw_input("Give the second number:")

try:
	result = float(number1) / float(number2)
	print ("The Result of Division %s / %s is %s" % (number1, number2, result))

except ZeroDivisionError as im:
 
	print "Error: %s" %im

except ValueError  as im2:
	print "Error: %s" %im2

finally:
	print "Closing Program"
