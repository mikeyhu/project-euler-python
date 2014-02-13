def primes():
	def isPrime(previous, number):
		for prime in previous:
			if number % prime == 0:
				return False
		return True
	a = []
	next = 2
	yield 1
	while True:
		while not isPrime(a, next):
			next+=1
		yield next
		a.append(next)
		next+=1