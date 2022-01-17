import unittest

import unit_convert


class TestData(unittest.TestCase):
    def test_byte_and_kilobyte(self):
        # (bytes, kilobytes)
        tests = [
            (1024, 1),
            (1536, 1.5),
            (1948160, 1902.5),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertEqual(unit_convert.UnitConvert(bytes=t[0]).kb, t[1])
                self.assertEqual(unit_convert.UnitConvert(kilobytes=t[1]).b, t[0])

    def test_byte_and_megabyte(self):
        # (bytes, megabytes)
        tests = [
            (1024, 0.0009765625),
            (1536, 0.00146484375),
            (1948160, 1.85791015625),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertAlmostEqual(unit_convert.UnitConvert(bytes=t[0]).mb, t[1])
                self.assertAlmostEqual(unit_convert.UnitConvert(megabytes=t[1]).b, t[0])

    def test_byte_and_gigabyte(self):
        # (bytes, gigabytes)
        tests = [
            (16471199580, 15.339999999850988),
            (201326592, 0.1875),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertAlmostEqual(unit_convert.UnitConvert(bytes=t[0]).gb, t[1])
                self.assertAlmostEqual(unit_convert.UnitConvert(gigabytes=t[1]).b, t[0])

    def test_kilobyte_and_gigabyte(self):
        # (kilbytes, gigabytes)
        tests = [
            (16085155, 15.339999198913574),
            (196608, 0.1875),
        ]
        for t in tests:
            with self.subTest(t=t):
                self.assertAlmostEqual(unit_convert.UnitConvert(kilobytes=t[0]).gb, t[1])
                self.assertAlmostEqual(unit_convert.UnitConvert(gigabytes=t[1]).kb, t[0])


if __name__ == '__main__':
    unittest.main()
