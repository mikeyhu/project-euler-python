class Problem6(object):

	def solve(self,number):
		sumOfSquares = 0
		squareOfSums = 0
		for i in range(1,number+1):	
			sumOfSquares += i*i
			squareOfSums += i
		return (squareOfSums * squareOfSums) - sumOfSquares
