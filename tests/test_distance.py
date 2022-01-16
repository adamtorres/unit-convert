import unittest

import unit_convert


class TestDistance(unittest.TestCase):
    def test_feet_and_meter(self):
        # (feet, meter)
        tests = [
            (10000, 3048),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(feet=t[0]).meters, t[1])
                self.assertEqual(unit_convert.UnitConvert(meters=t[1]).feet, t[0])


if __name__ == '__main__':
    unittest.main()
