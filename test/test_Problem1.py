import unittest
from main import Problem1

class TestProblem1(unittest.TestCase):

	def test_sum_of_natural_numbers_below_10_that_are_multiples_of_3_or_5(self):
		p1 = Problem1.Problem1()
		self.assertEqual(23,p1.solve(10))

	def test_sum_of_natural_numbers_below_1000_that_are_multiples_of_3_or_5(self):
		p1 = Problem1.Problem1()
		self.assertEqual(233168,p1.solve(1000))
