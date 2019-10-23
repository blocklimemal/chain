from vehicle import Vehicle

class Car(Vehicle):
	pessengers= []
	def __init__(self,pessenger):
		super().__init__(pessenger)
		self.pessengers.append(pessenger)
	def __repr__(self):
		return '{}'.format(self.pessengers)


car =Car(['name'])

print( car.__repr__());
 
