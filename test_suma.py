import unittest
from suma import sumar

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()