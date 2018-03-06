import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2,result)
	def test_add2(self):
		result = rpn.calculate("1 1 + 2 +")
		self.assertEqual(4,result)
	def test_sub(self):
		result = rpn.calculate("4 1 -")
		self.assertEqual(3,result)
	def test_red(self):
		with self.assertRaises(TypeError):
			result =rpn.calculate("1 2 3 +")
	def test_mul(self):
		result = rpn.calculate("1 1 *")
		self.assertEqual(1,result)
	def test_div(self):
		result = rpn.calculate("4 1 /")
		self.assertEqual(4,result)
	def test_trigo(self):
		result = rpn.calculate("0 cos")
		self.assertEqual(1,result)
	def test_anglemode(self):
		result = rpn.calculate("deg 90 sin rad 0 cos +")
		self.assertEqual(2,result)
	def test_cpy(self):
		result = rpn.calculate("1 cpy -")
		self.assertEqual(0,result)
	def test_fact(self):
		result = rpn.calculate("2 3 ^")
		self.assertEqual(8,result)
