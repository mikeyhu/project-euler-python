class Problem1(object):

	def solve(self,max):
		sum = 0
		for number in range(1,max):
			if number % 3 == 0 or number % 5 == 0 :
				sum += number
		return sum
