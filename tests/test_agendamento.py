import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cliente import Cliente
from servico import Servico
from agendamento import Agendamento

class TestAgendamento(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Maria Oliveira", "11888888888")
        self.servico = Servico("Barba", 25.0, 20)
        self.data_hora = datetime(2025, 7, 2, 15, 30)
        self.agendamento = Agendamento(self.cliente, self.servico, self.data_hora)

    def test_confirmar_agenda(self):
        esperado = "Agendado: Maria Oliveira (11888888888) para Barba - R$25.00 (20 min) em 02/07/2025 15:30"
        self.assertEqual(self.agendamento.confirmar_agenda(), esperado)

    def test_cancelar_agenda(self):
        esperado = "Agendamento de Maria Oliveira (11888888888) cancelado."
        self.assertEqual(self.agendamento.cancelar_agenda(), esperado)

if __name__ == '__main__':
    unittest.main()
