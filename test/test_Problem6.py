import unittest
from main import Problem6

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.problem = Problem6.Problem6()

	def test_difference_between_sum_of_squares_and_square_of_sums_1_to_10(self):
		self.assertEqual(2640,self.problem.solve(10))

	def test_difference_between_sum_of_squares_and_square_of_sums_1_to_100(self):
		self.assertEqual(25164150,self.problem.solve(100))
