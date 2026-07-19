from modelo.poligono import Poligono
from .estado import Estado

class EstadoPoligono(Estado): # herda os métodos criados na classe Estado 

    def pressionar_mouse(self, x, y):

        if self.controller.figura_atual is None: # se não existe polígono sendo desenhado, cria um novo

            self.controller.figura_atual = Poligono(x, y, self.controller.cor_borda, self.controller.cor_preench)

        else: # se já existe, adiciona um novo vértice
            self.controller.figura_atual.adicionar_ponto(x, y)
    
    def soltar_mouse(self, x, y):
        # o polígono não é finalizado ao soltar o mouse
        pass

    def finalizar(self): # finaliza o polígono adicionando-o ao desenho
        
        if self.controller.figura_atual:
            self.controller.figura_atual.finalizar_forma() # remove a guia móvel do último vértice

            if not self.controller.figura_atual.incompleta(): # impede que polígonos incompletos sejam adicionados ao desenho
                self.controller.desenho.adicionar(self.controller.figura_atual)

            self.controller.figura_atual = None
            self.controller.view.redesenhar()