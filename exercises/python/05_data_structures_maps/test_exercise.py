import unittest
from exercise import contar_frequencia_palavras, agrupar_por_tamanho

class TestDataStructures(unittest.TestCase):
    def test_contar_frequencia_palavras(self):
        resultado = contar_frequencia_palavras("O pato viu outro pato.")
        self.assertEqual(resultado, {"o": 1, "pato": 2, "viu": 1, "outro": 1})

    def test_contar_frequencia_pontuacao(self):
        resultado = contar_frequencia_palavras("Sim! Sim, claro? Claro.")
        self.assertEqual(resultado, {"sim": 2, "claro": 2})

    def test_agrupar_por_tamanho(self):
        resultado = agrupar_por_tamanho(["sol", "lua", "marte", "ceu"])
        self.assertEqual(resultado, {
            3: ["sol", "lua", "ceu"],
            5: ["marte"]
        })

    def test_agrupar_por_tamanho_vazio(self):
        self.assertEqual(agrupar_por_tamanho([]), {})

if __name__ == "__main__":
    unittest.main()
