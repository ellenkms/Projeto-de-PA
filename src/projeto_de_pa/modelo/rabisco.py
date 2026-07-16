from .figura import Figura

class Rabisco(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.pontos = [(x, y)] # armazena o primeiro ponto do Rabisco em uma lista para adicionar novos pontos
        
    def atualizar(self, x, y):
        self.pontos.append((x, y)) # adiciona novos pontos na lista

    def incompleta(self):
        return len(self.pontos) <= 1 # se houver menos de dois pontos o Rabisco está incompleto