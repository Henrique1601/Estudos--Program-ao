import unittest
from exercise import somar_impares, encontrar_maior

class TestLoops(unittest.TestCase):
    def test_somar_impares_misto(self):
        self.assertEqual(somar_impares([1, 2, 3, 4, 5]), 9)

    def test_somar_impares_vazio(self):
        self.assertEqual(somar_impares([]), 0)

    def test_somar_impares_apenas_pares(self):
        self.assertEqual(somar_impares([2, 4, 6, 8]), 0)

    def test_encontrar_maior_positivo(self):
        self.assertEqual(encontrar_maior([10, 45, 2, 99, 14]), 99)

    def test_encontrar_maior_negativo(self):
        self.assertEqual(encontrar_maior([-50, -10, -2, -80]), -2)

    def test_encontrar_maior_vazio_lanca_erro(self):
        with self.assertRaises(ValueError):
            encontrar_maior([])

if __name__ == "__main__":
    unittest.main()
