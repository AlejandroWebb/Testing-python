import unittest

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.calculator import suma, resta

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)
#Prueva initaria para  la funcion suma
   
    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)