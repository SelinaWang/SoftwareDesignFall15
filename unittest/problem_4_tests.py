# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def in_language(s):
	if s == '':
		return True
	elif s[0] != 'a':
		return False
	elif s[len(s)/2] != 'b':
		return False
	elif s[0:len(s)/2-1] != s[len(s)/2:len(s)-1]:
		return False
	elif s[0:len(s)/2-1] != 'a'*(len(s)/2) or s[len(s)/2:len(s)-1] != 'b'*(len(s)/2):
		return False
	else:
		return True

class InLanguageTests(unittest.TestCase):
	def test_in_language_iteration1(self):
		self.assertFalse(in_language('aaab'))
		self.assertFalse(in_language('aaaccc'))
		self.assertTrue(in_language(''))
		self.assertTrue(in_language('aaaabbbb'))

if __name__ == '__main__':
	unittest.main()