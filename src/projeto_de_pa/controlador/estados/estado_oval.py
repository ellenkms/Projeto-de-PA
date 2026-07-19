from modelo.figura2pontos import Oval
from .estado import Estado

class EstadoOval(Estado): # herda os métodos criados na classe Estado 

    def pressionar_mouse(self, x, y):
        # cria um novo oval e o define como a figura em construção
        self.controller.figura_atual = Oval(x, y, self.controller.cor_borda, self.controller.cor_preench)