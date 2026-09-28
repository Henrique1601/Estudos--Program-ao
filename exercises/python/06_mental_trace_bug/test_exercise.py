import unittest
from exercise import registrar_participante, somar_fatias_janela

class TestMentalTraceBug(unittest.TestCase):
    def test_registrar_participante_independencia(self):
        # Cada chamada sem o segundo argumento deve ter sua própria lista!
        p1 = registrar_participante("Alice")
        p2 = registrar_participante("Bob")
        
        self.assertEqual(p1, ["Alice"])
        self.assertEqual(p2, ["Bob"])

    def test_somar_fatias_janela(self):
        valores = [1, 2, 3, 4]
        resultado = somar_fatias_janela(valores, 2)
        # Janelas de tamanho 2: [1,2]=3, [2,3]=5, [3,4]=7
        self.assertEqual(resultado, [3, 5, 7])

    def test_somar_fatias_janela_tamanho_tres(self):
        valores = [10, 20, 30, 40, 50]
        resultado = somar_fatias_janela(valores, 3)
        # [10+20+30=60, 20+30+40=90, 30+40+50=120]
        self.assertEqual(resultado, [60, 90, 120])

if __name__ == "__main__":
    unittest.main()
