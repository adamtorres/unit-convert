import unittest

import unit_convert


class TestMass(unittest.TestCase):
    def test_gram_and_kilogram(self):
        # (gram, kilogram)
        tests = [
            (10000, 10),
            (10, 0.010),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(g=t[0]).kg, t[1])
                self.assertEqual(unit_convert.UnitConvert(kg=t[1]).g, t[0])

    def test_gram_and_tonnes(self):
        # (gram, tonnes)
        tests = [
            (10000, 0.01),
            (10000000, 10),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(g=t[0]).tonnes, t[1])
                self.assertEqual(unit_convert.UnitConvert(tonnes=t[1]).g, t[0])

    def test_kilogram_and_tonnes(self):
        # (kilogram, tonnes)
        tests = [
            (10, 0.01),
            (10000, 10),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(kg=t[0]).tonnes, t[1])
                self.assertEqual(unit_convert.UnitConvert(tonnes=t[1]).kg, t[0])

    def test_kilogram_and_tons(self):
        # (kilogram, tons)
        tests = [
            (10, 0.0110231),
            (10000, 11.02311),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(kg=t[0]).tonnes, t[1])
                self.assertEqual(unit_convert.UnitConvert(tonnes=t[1]).kg, t[0])


if __name__ == '__main__':
    unittest.main()
