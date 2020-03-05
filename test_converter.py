import unittest
import converter

class Test(unittest.TestCase):
    def test_yard_to_meter(self):
        self.assertAlmostEqual(converter.yard_to_meter(1), 0.91)
        with self.assertRaises(ValueError):
            result = converter.yard_to_meter(True)
        with self.assertRaises(ValueError):
            result = converter.yard_to_meter('')

    def test_meter_to_yard(self):
        self.assertAlmostEqual(converter.meter_to_yard(1), 1.09361)
        with self.assertRaises(ValueError):
            result = converter.meter_to_yard(True)
        with self.assertRaises(ValueError):
            result = converter.meter_to_yard('')



if __name__ == '__main__':
    unittest.main()