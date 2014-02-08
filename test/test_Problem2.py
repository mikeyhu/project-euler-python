import unittest
from main import Problem2

class TestProblem1(unittest.TestCase):

	def test_sum_even_fib_numbers_less_than_100(self):
		p1 = Problem2.Problem2()
		self.assertEqual(44,p1.solve(100))

	def test_sum_even_fib_numbers_less_than_4000000(self):
		p1 = Problem2.Problem2()
		self.assertEqual(4613732,p1.solve(4000000))
