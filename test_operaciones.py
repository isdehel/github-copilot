import unittest
from operaciones import suma, resta, multiplicacion, division

class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(3, 5), 8)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(0, 5), -5)
        self.assertEqual(resta(-3, -7), 4)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 5), 20)
        self.assertEqual(multiplicacion(-2, 3), -6)
        self.assertEqual(multiplicacion(0, 10), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()