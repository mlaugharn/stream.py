class Stream:
	def __init__(self, map_function = None, filter_function = None):
		self.map_function, self.filter_function = map_function, filter_function
		if self.map_function == None: self.map_function = lambda x: x
		if self.filter_function == None: self.filter_function = lambda x: True

	def pluck(self, n):
		"""Yields the first n numbers that, once mapped by map_function, pass filter_function"""
		i = 0
		while n > 0:
			computation = self.map_function(i)
			if self.filter_function(computation):
				yield computation
				n -= 1
			i += 1
