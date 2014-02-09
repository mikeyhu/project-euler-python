import unittest
from main import Problem3

class TestProblem3(unittest.TestCase):

	def test_largest_prime_factor_of_13195(self):
		p = Problem3.Problem3()
		self.assertEqual(29,p.solve(13195))

#	def test_largest_prime_factor_of_600851475143(self):
#		p = Problem3.Problem3()
#		self.assertEqual(6857,p.solve(600851475143))
