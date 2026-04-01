# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(8,15,17),'Right','8,15,17 should be Right')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 should be Equilateral')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,3),'Isoceles','5,5,3 should be Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles','5,3,5 should be Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,5),'Isoceles','3,5,5 should be Isoceles')

    # Scalene triangle (expected to fail in your original table)
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','10,1,1 should be NotATriangle')


    def testInvalidInputZeroA(self):
        self.assertEqual(classifyTriangle(0,8,9),'InvalidInput','0,8,9 should be InvalidInput')

    def testInvalidInputZeroB(self):
        self.assertEqual(classifyTriangle(8,0,9),'InvalidInput','8,0,9 should be InvalidInput')

    def testInvalidInputZeroC(self):
        self.assertEqual(classifyTriangle(8,9,0),'InvalidInput','8,9,0 should be InvalidInput')

    def testInvalidInputNegativeA(self):
        self.assertEqual(classifyTriangle(-3,4,5),'InvalidInput','-3,4,5 should be InvalidInput')

    def testInvalidInputTooLargeA(self):
        self.assertEqual(classifyTriangle(221,4,5),'InvalidInput','221,4,5 should be InvalidInput')

    def testInvalidInputTooLargeB(self):
        self.assertEqual(classifyTriangle(4,221,5),'InvalidInput','4,221,5 should be InvalidInput')

    def testInvalidInputTooLargeC(self):
        self.assertEqual(classifyTriangle(4,5,221),'InvalidInput','4,5,221 should be InvalidInput')

    def testInvalidInputFloatA(self):
        self.assertEqual(classifyTriangle(3.3,4,5),'InvalidInput','3.3,4,5 should be InvalidInput')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

