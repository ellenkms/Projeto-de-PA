from .figura import Figura

class Poligono(Figura):
    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench)
        # Começa com dois vértices no mesmo lugar (o ponto inicial e a guia móvel)
        self.vertices = [(x, y), (x, y)]

    def atualizar(self, x, y):
        # A guia móvel segue o mouse sem fixar o ponto
        self.vertices[-1] = (x, y)

    def adicionar_ponto(self, x, y):
        # Fixa o ponto clicado e cria uma nova guia móvel
        self.vertices[-1] = (x, y)
        self.vertices.append((x, y))

    def finalizar_forma(self):
        # Remove a guia móvel para o desenho fechar bonitinho no último clique
        if len(self.vertices) >= 2: 
            self.vertices.pop()

    def incompleta(self):
        return len(self.vertices) < 3