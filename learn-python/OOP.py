class Animal:
	def __init__(self, kind, age):
		self.kind = kind
		self.age = age

	def say(self):
		print self.kind
		print self.age

animal = Animal("Dog", 3)
animal.say()