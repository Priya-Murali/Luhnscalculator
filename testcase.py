#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from luhnscalculator import getLuhnssum,checkIsValidSequence,getCheckDigit
import unittest
# from sernova_technicaltest import luhnsCalc, checkIsValidSequence, getCheckDigit

class TestLuhnsFunctions(unittest.TestCase):

    def test_luhnsCalc(self):
        self.assertEqual(getLuhnssum('5146713835430'), 47)
        with self.assertRaises(Exception):
            getLuhnssum('')
        with self.assertRaises(Exception):
            getLuhnssum('123abc')

    def test_checkIsValidSequence(self):
        self.assertFalse(checkIsValidSequence('1234'))
        self.assertTrue(checkIsValidSequence('1234567897'))

    def test_getCheckDigit(self):
        self.assertEqual(getCheckDigit('123456789'), 7)
        self.assertEqual(getCheckDigit('12345678978'), 3)
        self.assertEqual(getCheckDigit(''), 0)

if __name__ == '__main__':
    unittest.main()
