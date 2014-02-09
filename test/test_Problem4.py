import unittest
from main import Problem4

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.problem = Problem4.Problem4()

	def test_largest_palindrome_from_2_digit_product_should_be_9009(self):
		self.assertEqual(9009,self.problem.solve(100))

	def test_largest_palindrome_from_3_digit_product_should_be_906609(self):
		self.assertEqual(906609,self.problem.solve(1000))

