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

    def test_gallon_and_kiloliter(self):
        # (gal, kl)
        tests = [
            (264.172, 1),
        ]
        for t in tests:
            with self.subTest(t=t):
                # Using assertAlmostEqual as the conversions give a pile of decimal places.  Rounding to two decimal
                # places for the tests.
                self.assertAlmostEqual(unit_convert.UnitConvert(gallons=t[0]).kiloliters, t[1], 2)
                self.assertAlmostEqual(unit_convert.UnitConvert(kiloliters=t[1]).gal, t[0], 2)

    def test_ml_and_ounce(self):
        # (ml, ounce)
        tests = [
            (500, 16.907),
            (750, 25.3605),
            (7640614, 258359.89416)
        ]
        for t in tests:
            with self.subTest(t=t):
                # Using assertAlmostEqual as the conversions give a pile of decimal places.  Rounding to two decimal
                # places for the tests.
                self.assertAlmostEqual(unit_convert.UnitConvert(ml=t[0]).oz, t[1], 2)
                self.assertAlmostEqual(unit_convert.UnitConvert(oz=t[1]).ml, t[0], 2)


if __name__ == '__main__':
    unittest.main()
