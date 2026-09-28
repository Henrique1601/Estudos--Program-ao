import unittest
from exercise import calcular_retangulo, converter_temperatura

class TestVariables(unittest.TestCase):
    def test_calcular_retangulo(self):
        area, perimetro = calcular_retangulo(5.0, 2.0)
        self.assertEqual(area, 10.0)
        self.assertEqual(perimetro, 14.0)

    def test_calcular_retangulo_quadrado(self):
        area, perimetro = calcular_retangulo(4.0, 4.0)
        self.assertEqual(area, 16.0)
        self.assertEqual(perimetro, 16.0)

    def test_converter_temperatura_zero(self):
        self.assertEqual(converter_temperatura("0"), 32.0)

    def test_converter_temperatura_positiva(self):
        self.assertEqual(converter_temperatura("100"), 212.0)

    def test_converter_temperatura_decimal(self):
        self.assertEqual(converter_temperatura("25.5"), 77.9)

if __name__ == "__main__":
    unittest.main()
