from operator import mul

class Problem8(object):

	def solve(self, input, consecutive):
		s = self.slidingGenerator(input,consecutive)
		return sorted([self.product(x) for x in s if x != None], reverse=True)[0]

	def product(self, numbersAsString):
		return reduce(mul, [int(n) for n in numbersAsString])

	def slidingGenerator(self, input, size):
		for i in range(0,len(input)-size+1):
			yield input[i:i+size]
		yield None