from t9_spelling.T9 import to_t9

__author__ = 'igomez'
import unittest


class TestSmall(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(to_t9('yes'), '999337777')
        self.assertEqual(to_t9('no'), '66 666')
        self.assertEqual(to_t9('allyour'), '2555 55599966688777')
        self.assertEqual(to_t9('baseare'), '22 2777733277733')
        self.assertEqual(to_t9('belongto'), '2233555666 6648666')
        self.assertEqual(to_t9('nexttimewontyou'), '6633998 84446339666 66899966688')

    def test_with_one_space(self):
        self.assertEqual(to_t9('foo bar'), '333666 666022 2777')
        self.assertEqual(to_t9('hello world'), '4433555 555666096667775553')

    def test_with_two_spaces(self):
        self.assertEqual(to_t9('foo  bar'), '333666 6660 022 2777')


if __name__ == '__main__':
    unittest.main()
