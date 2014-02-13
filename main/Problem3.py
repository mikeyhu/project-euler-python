import math
from lib import Primes

class Problem3(object):

	def solve(self,number):
		p = Primes.primes()
		next = p.next()
		largest = 0
		max = math.sqrt(number)
		while next < max:
			if number % next == 0:
				largest = next
			next = p.next()
		return largest


