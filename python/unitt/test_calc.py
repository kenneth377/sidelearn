import unittest
import calc


class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,2),3)
        self.assertRaises(TypeError, calc,-1,2)

if __name__ == 'main':
    unittest.main()