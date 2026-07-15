from .figura import Figura

class Circulo(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x = x  # armazena as coordenadas do ponto central
        self.y = y
        self.raio = 0 

    def atualizar(self, x, y):
        self.raio = max(abs(x - self.x), abs(y - self.y))  # atualiza somente o raio, o ponto central é fixo
        
    def incompleta(self):  # se o raio for igual a zero, não houve movimento e o círculo não existe
        return self.raio == 0
