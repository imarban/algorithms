from t9_spelling.T9 import to_t9

__author__ = 'igomez'
import unittest


class TestLarge(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(to_t9(' a a a'), '020202')
        self.assertEqual(to_t9('a  a  a'), '20 020 02')
        self.assertEqual(to_t9('a  bb  ccc'), '20 022 220 0222 222 222')
        self.assertEqual(
            to_t9('hddqnetqpduyzoejlmymlfvlkdg emmhhrearl uthlnjnewxfmraboxsmtrf  '),
            '443 3776633877 7388999 9999666335 55569996555333888555 55340336 644 44777332777555088 84455566566339 9933367772 22666997777687773330 0')


if __name__ == '__main__':
    unittest.main()
