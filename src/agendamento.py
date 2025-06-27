from datetime import datetime

class Agendamento:
    def __init__(self, cliente, servico, data_hora):
        self.cliente = cliente
        self.servico = servico
        self.data_hora = data_hora

    def confirmar_agenda(self):
        return f"Agendado: {self.cliente} para {self.servico} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

    def cancelar_agenda(self):
        return f"Agendamento de {self.cliente} cancelado."
