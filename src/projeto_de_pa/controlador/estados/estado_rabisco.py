from modelo.rabisco import Rabisco
from .estado import Estado

class EstadoRabisco(Estado): # herda os métodos criados na classe Estado 

    def pressionar_mouse(self, x, y):
        # cria um novo rabisco e o define como a figura em construção
        self.controller.figura_atual = Rabisco(x, y, self.controller.cor_borda, self.controller.cor_preench)

    def soltar_mouse(self, x, y):

        if self.controller.figura_atual:

            if not self.controller.figura_atual.incompleta(): # impede que rabiscos incompletos sejam adicionados ao desenho
                self.controller.desenho.adicionar(self.controller.figura_atual)

            self.controller.figura_atual = None
            self.controller.view.redesenhar()