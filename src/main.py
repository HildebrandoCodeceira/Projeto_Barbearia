from cliente import Cliente
from servico import Servico
from agendamento import Agendamento
from datetime import datetime

cliente1 = Cliente("João Silva", "11999999999")
servico1 = Servico("Corte Masculino", 40.0, 30)
data = datetime(2025, 7, 1, 14, 0)
agendamento1 = Agendamento(cliente1, servico1, data)

print(agendamento1.confirmar_agenda())
print(agendamento1.cancelar_agenda())
