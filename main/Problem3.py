import math

class Problem3(object):

	def solve(self,number):
		p = self.primes()
		next = p.next()
		largest = 0
		max = math.sqrt(number)
		while next < max:
			if number % next == 0:
				largest = next
			next = p.next()
		return largest

	
	def primes(self):
		def isPrime(self, previous, number):
			for prime in previous:
				if number % prime == 0:
					return False
			return True
		a = []
		next = 2
		yield 1
		while True:
			while not isPrime(self,a,next):
				next+=1
			yield next
			a.append(next)
			next+=1

