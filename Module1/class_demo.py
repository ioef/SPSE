#!/usr/bin/env python

class Calculator:

	def __init__(self,numA,numB):
		self.a = numA
		self.b = numB


	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a*self.b



class Scientific(Calculator):
	
	def power(self):
		return pow(self.a, self.b)

	def add(self):
		#this broken method overrides the correct one
		return self.a + self.b + 2


calc = Calculator(10,20)

print 'a:%s b:%s'%(calc.a,calc.b)
print 'a + b: %s' %calc.add()
print 'a * b: %s' %calc.mul()

print

newPower = Scientific(2,3)

print 'a:%s b:%s'%(newPower.a,newPower.b)
print 'a + b: %s' %newPower.add()
print 'a^i: %s' %newPower.power()



