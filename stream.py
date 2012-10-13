class Stream:
	def __init__(self, mapFunction=None, filterFunction=None):
		self.mapFunction = mapFunction
		self.filterFunction = filterFunction
		if self.mapFunction == None:
			self.mapFunction = lambda x: x
		if self.filterFunction == None:
			self.filterFunction = lambda x: True

	def pluck(self, cardinality):
		"""Returns a list of the first cardinality numbers that, once mapped by mapFunction, pass filterFunction"""
		self.currentTestedInt = 0
		self.matchedRealNumbers = []
		while len(self.matchedRealNumbers) < cardinality:
			if self.filterFunction(self.mapFunction(self.currentTestedInt)) == True:
				self.matchedRealNumbers.append(self.mapFunction(self.currentTestedInt))
			self.currentTestedInt += 1
		return self.matchedRealNumbers