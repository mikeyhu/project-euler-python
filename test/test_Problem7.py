import unittest
from main import Problem7

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.problem = Problem7.Problem7()

	def test_sixth_prime_should_be_13(self):
		self.assertEqual(13,self.problem.solve(6))

#	def test_10001_prime_should_be_104743(self):
#		self.assertEqual(104743,self.problem.solve(10001))