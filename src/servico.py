class Servico:
    def __init__(self, nome, preco, duracao):
        self.nome = nome
        self.preco = preco
        self.duracao = duracao  # duração em minutos

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f} ({self.duracao} min)"
