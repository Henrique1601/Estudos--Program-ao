import unittest
from exercise import eh_bissexto, classificar_triangulo

class TestConditionals(unittest.TestCase):
    def test_eh_bissexto_normal(self):
        self.assertTrue(eh_bissexto(2024))
        self.assertFalse(eh_bissexto(2023))

    def test_eh_bissexto_seculares(self):
        self.assertFalse(eh_bissexto(1900))
        self.assertTrue(eh_bissexto(2000))

    def test_triangulo_equilatero(self):
        self.assertEqual(classificar_triangulo(5, 5, 5), "equilatero")

    def test_triangulo_isosceles(self):
        self.assertEqual(classificar_triangulo(5, 5, 8), "isosceles")
        self.assertEqual(classificar_triangulo(8, 5, 5), "isosceles")

    def test_triangulo_escaleno(self):
        self.assertEqual(classificar_triangulo(3, 4, 5), "escaleno")

    def test_triangulo_invalido_desigualdade(self):
        self.assertEqual(classificar_triangulo(1, 2, 10), "invalido")

    def test_triangulo_invalido_negativo(self):
        self.assertEqual(classificar_triangulo(-1, 5, 5), "invalido")
        self.assertEqual(classificar_triangulo(0, 5, 5), "invalido")

if __name__ == "__main__":
    unittest.main()
