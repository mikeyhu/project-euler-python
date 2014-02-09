import math

class Problem4(object):

	def solve(self,number):
		highest = 0
		for i in range(1,number):
			for j in range(1,number):
				current = i * j
				if current > highest and self.isPalindrome(current):
					highest = current
		return highest

	def isPalindrome(self,number):
		chars = list(str(number))
		for i in range(0,len(chars)/2):
			if chars[i] != chars[len(chars)-1-i]:
				return False
		return True

