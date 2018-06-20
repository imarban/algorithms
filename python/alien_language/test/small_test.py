from alien_language.alien import words_match
import unittest

__author__ = 'igomez'


class TestSmall(unittest.TestCase):
    def test_long(self):
        self.assertEqual(words_match(
            ["nwlrbbmqbh", "cdarzowkky", "hiddqscdxr", "jmowfrxsjy", "bldbefsarc", "bynecdyggx", "xpklorelln",
             "mpapqfwkho", "pkmcoqhnwn", "kuewhsqmgb", "buqcljjivs", "wmdkqtbxix", "mvtrrbljpt", "nsnfwzqfjm",
             "afadrrwsof", "sbcnuvqhff", "bsaqxwpqca", "cehchzvfrk", "mlnozjkpqp", "xrjxkitzyx", "acbhhkicqc",
             "oendtomfgd", "wdwfcgpxiq", "vkuytdlcgd", "ewhtacioho", "rdtqkvwcsg", ],
            "(aknw)(glmw)(jlue)(kruw)(bci)(xbu)(mue)(qemn)(tyab)(hmrd)"), 1)


if __name__ == '__main__':
    unittest.main()
