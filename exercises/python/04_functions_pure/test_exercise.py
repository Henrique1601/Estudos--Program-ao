import unittest
from exercise import inverter_ordem_palavras, remover_duplicados

class TestFunctions(unittest.TestCase):
    def test_inverter_ordem_palavras_normal(self):
        self.assertEqual(
            inverter_ordem_palavras("aprender a programar sem IA"),
            "IA sem programar a aprender"
        )

    def test_inverter_ordem_palavras_uma_palavra(self):
        self.assertEqual(inverter_ordem_palavras("Python"), "Python")

    def test_remover_duplicados_ordem(self):
        entrada = [3, 1, 2, 3, 1, 4]
        resultado = remover_duplicados(entrada)
        self.assertEqual(resultado, [3, 1, 2, 4])
        # Garante que a lista original não foi alterada (função pura)
        self.assertEqual(entrada, [3, 1, 2, 3, 1, 4])

    def test_remover_duplicados_vazio(self):
        self.assertEqual(remover_duplicados([]), [])

if __name__ == "__main__":
    unittest.main()
