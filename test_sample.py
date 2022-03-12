"""
Test helper functions
"""

import unittest
from sample import increment_by_two

class TestSampleMethods(unittest.TestCase):
    """
    Test harness
    """
    unittest.TestCase.assertEqual(increment_by_two(-2),0)
    unittest.TestCase.assertEqual(increment_by_two(0),1)
    unittest.TestCase.assertEqual(increment_by_two(3),5)

if __name__ == '__main__':
    unittest.main()
