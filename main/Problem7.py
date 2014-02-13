from lib import Primes

class Problem7(object):

	def solve(self,number):
		p = Primes.primes()
		for i in range(0,number):
			p.next()
		return p.next() 
