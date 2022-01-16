import unittest

import unit_convert


class TestVolume(unittest.TestCase):
    def test_ounce_and_cup(self):
        # (ounces, cups)
        tests = [
            (16, 2),
            (1, 0.125),
            (0.5, 0.0625),
            (128, 16),
            (124, 15.5),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(ounces=t[0]).cups, t[1])
                self.assertEqual(unit_convert.UnitConvert(cups=t[1]).ounces, t[0])

    def test_tsp_and_gallon(self):
        # (tsp, gal)
        tests = [
            (768, 1),
            (384, 0.5),
            (192, 0.25),
            (12, 0.015625),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(teaspoons=t[0]).gal, t[1])
                self.assertEqual(unit_convert.UnitConvert(gal=t[1]).tsp, t[0])


if __name__ == '__main__':
    unittest.main()
