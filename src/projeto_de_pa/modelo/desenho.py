class Desenho:

    def __init__(self):
        self.figuras = []  
    
    def adicionar(self, figura):
        self.figuras.append(figura)
    
    def limpar(self):
        self.figuras.clear()

    def remover(self, figura):
        self.figuras.remove(figura)