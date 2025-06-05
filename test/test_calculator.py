import unittest

from src.calculator import suma, resta, multiplicacion, division

class CalculatorTest(unittest.TestCase): 

    #Prueba unitaria par la funcion suma
    def test_sum(self):
        self.assertEqual(suma(4, 3), 7)

    #Prueba unitaria para la funcion resta
    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

    #Prueba unitaria para la funcion multiplicacion
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)
    
    #Prueba unitaria para la funcion division
    def test_division(self):
        self.assertEqual(division(12, 4), 3)