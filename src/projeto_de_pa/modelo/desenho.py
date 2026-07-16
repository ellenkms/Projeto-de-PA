class Desenho:

    def __init__(self):
        self.figuras = []  # armazena todas as figuras do desenho
    
    def adicionar(self, figura):
        self.figuras.append(figura) # adiciona uma figura à lista
    
    def limpar(self):
        self.figuras.clear() # remove todas as figuras da lista