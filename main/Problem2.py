class Problem2(object):

	def solve(self,max):
		sum = 0
		fib = self.fibGenerator()
		next = fib.next()
		while next < max:
			if next % 2 == 0 :
				sum += next
			next = fib.next()
		return sum

	def fibGenerator(self):
		a, b = 0, 1
		yield 0
		while True:
			a, b = b, a + b
			yield a
