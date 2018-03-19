# -*- coding: utf-8 -*-

import unittest
from counter import Calculator

class CounterTest(unittest.TestCase):
    def setup(self):
        self.cal=Calculator(8,4)
        
    def tearDown(self):
        pass
    def test_add(self):
        result=self.cal.add()
        self.assertEqual(result,12)
        
    def test_sub(self):
        result=self.cal.sub()
        self.assertEqual(result,4)        
        
    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(result,32)
        
    def test_div(self):
        result=self.cal.div()
        self.assertEqual(result,2)     
        
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CounterTest("test_add"))
    suite.addTest(CounterTest("test_sub"))
    suite.addTest(CounterTest("test_mul"))
    suite.addTest(CounterTest("test_div"))
        
    runner = unittest.TextTestResult("a","b",1)
    runner.run(suite)

