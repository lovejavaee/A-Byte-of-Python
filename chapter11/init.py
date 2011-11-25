class person:
	def __init__(self, taste):
		self.name = taste
	def sayname(self):
		print 'my name is ',self.name

p = person('sonic')
p.sayname()
