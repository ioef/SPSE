#!/usr/bin/python

"""
	5.9.2016
	SPSE
"""


def main():
	employees=[]
	names = raw_input("Please enter an employee Name (Q to quit): ")
	while names !='Q':
	        employees.append(names)
		names=raw_input("Please enter another employee Name(Q to quit):")	
	else:
		print "Thank you for your submission"
		print "Your current employees are:%s"%employees
	


if __name__ == '__main__' : 
	main()

