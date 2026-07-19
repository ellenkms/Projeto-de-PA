from modelo.figura2pontos import Linha
from .estado import Estado

class EstadoLinha(Estado): # herda os métodos criados na classe Estado 

    def pressionar_mouse(self, x, y):
        # cria uma nova linha e a define como a figura em construção
        self.controller.figura_atual = Linha(x, y, self.controller.cor_borda, self.controller.cor_preench)