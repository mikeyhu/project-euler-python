import unittest
from main import Problem5

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.problem = Problem5.Problem5()

	def test_smallest_number_divisible_by_1_to_10_should_be_2520(self):
		self.assertEqual(2520,self.problem.solve(10))

	def test_smallest_number_divisible_by_1_to_20_should_be_232792560(self):
		self.assertEqual(232792560,self.problem.solve(20))

