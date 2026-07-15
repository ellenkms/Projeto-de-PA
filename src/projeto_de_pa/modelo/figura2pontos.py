from .figura import Figura
from abc import ABC

class Figura2Pontos(Figura, ABC):  # herda da classe Figura
    """reúne os comportamentos comuns de Linha, Retângulo e Oval."""

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x1 = x  # armazena coordenadas do ponto inicial
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        """Tirei o event pra ficar só no controller"""
        self.x2 = x  # atualiza somente o ponto final, o ponto inicial é fixo
        self.y2 = y

    def incompleta(self): # se os pontos forem iguais, a figura não existe
        return (self.x1 == self.x2) and (self.y1 == self.y2)


class Linha(Figura2Pontos): # herda da classe Figura2Pontos
    pass 

class Retangulo(Figura2Pontos): # herda da classe Figura2Pontos
    pass

class Oval(Figura2Pontos): # herda da classe Figura2Pontos
    pass