import itertools

class Problem5(object):

	def solve(self,number):
		uniqueProducts = self.products(number)

		for x in itertools.count(1):
			valid = True
			for i in uniqueProducts:
				if not x % i == 0:
					valid = False
			if valid:
				return x

	def products(self,number):
		result = []
		for i in range(number,1,-1):
			add = True
			for j in result:
				if j % i == 0:
					add = False
			if add:
				result.append(i)
		return result


