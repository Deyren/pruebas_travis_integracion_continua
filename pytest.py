import unittest
import main


class TestMyModule(unittest.TestCase):

	def test_sum(self):
		self.assertEqual(main.al_cuadrado(2), 4)
		self.assertEqual(main.al_cuadrado(3),9)


if __name__ == "__main__":
	unittest.main()

# nigga