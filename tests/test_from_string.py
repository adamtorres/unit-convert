import unittest

import unit_convert


class TestFromString(unittest.TestCase):
    def run_tests(self, tests, exactly_equal=True):
        for t in tests:
            src_unit, src_value = next(iter(t[0].items()))
            for dest_unit, dest_value in t[1].items():
                with self.subTest(src_unit=src_unit, src_value=src_value, dest_unit=dest_unit, dest_value=dest_value):
                    uc = unit_convert.from_string(f"{src_value}{src_unit}")
                    if exactly_equal:
                        self.assertEqual(getattr(uc, dest_unit), dest_value)
                    else:
                        self.assertAlmostEqual(getattr(uc, dest_unit), dest_value)

    def test_from_string_distance(self):
        tests = [
            ({"feet": 10000},  {"meters": 3048, "kilometers": 3.048, "inches": 120000}),
        ]
        self.run_tests(tests)

    def test_from_string_multiple_types(self):
        tests = [
            ({"ounces": 32},  {"pounds": 2, "cups": 4}),
            ({"m": 15}, {"hours": 0.25, "feet": 49.21259842})
        ]
        self.run_tests(tests, exactly_equal=False)


if __name__ == '__main__':
    unittest.main()
