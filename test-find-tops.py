# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:29:28 2021

@author: kmate
"""

import Program1
import unittest

class TestProgram1(unittest.TestCase):
    """Test Program1 module."""
    def test_top_fun_with_six_tops_first_lower_than_second(self):
        case1 = [2, 4, 3, 5, 3, 4, 1, 0, 7, 5, 8, 2, 3, 1]
        self.assertEqual(Program1.tops(case1), [4, 5, 4, 7, 8, 3])
        
    def test_top_fun_with_four_tops_first_higher_than_second(self):
        case2 = [4, 2, 3, 1, 5, 2]
        self.assertEqual(Program1.tops(case2), [4, 3, 5])
    
    def test_top_fun_last_number_is_top(self):
        case3 = [4, 2, 3, 1, 8]
        self.assertEqual(Program1.tops(case3), [4, 3, 8])
    
    def test_top_fun_last_number_is_not_top(self):
        case4 = [4, 2, 3, 2, 1]
        self.assertEqual(Program1.tops(case4), [4, 3])
    
    # def test_top_fun_last_number_is_not_top_should_not_raise_error(self):
    #     case4 = [4, 2, 3, 2, 1, 5]
    #     self.assertRaises(IndexError, Program1.tops(case3))
            
        
if __name__ == '__main__':
    unittest.main(verbosity=2)