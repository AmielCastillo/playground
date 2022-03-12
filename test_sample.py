"""
Test helper functions
"""

import unittest
from sample import increment_by_two, increment_by_three

class TestSampleMethods(unittest.TestCase):
   """
   Test harness
   """
   self.assertEqual(increment_by_two(-2),0)
   self.assertEqual(increment_by_two(0),1)
   self.assertEqual(increment_by_two(3),5)
    
if __name__ == '__main__':
  unittest.main()
