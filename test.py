import unittest
from main import NumericFormatter, NumericError


class TestNumericFormatter(unittest.TestCase):
    def test_parseInt(self):
        self.assertEqual(NumericFormatter().parseInt("123321"), 123321)
        self.assertEqual(NumericFormatter().parseInt("-100"), -100)
        self.assertEqual(NumericFormatter().parseInt("+100"), 100)
        self.assertEqual(NumericFormatter().parseInt("+0"), 0)
        self.assertEqual(NumericFormatter().parseInt("+0"), 0)
        self.assertEqual(NumericFormatter().parseInt("00321"), 321)
        self.assertEqual(NumericFormatter().parseInt("-01"), -1)

        self.assertRaises(NumericError, NumericFormatter().parseInt, "10.1")
        self.assertRaises(NumericError, NumericFormatter().parseInt, "qwe")
        self.assertRaises(NumericError, NumericFormatter().parseInt, "--10")
        self.assertRaises(NumericError, NumericFormatter().parseInt, "++1")
        self.assertRaises(NumericError, NumericFormatter().parseInt, "100e")


if __name__ == '__main__':
    unittest.main()
