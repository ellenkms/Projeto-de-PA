from modelo.figura2pontos import Retangulo
from .estado import Estado

class EstadoRetangulo(Estado): # herda os métodos criados na classe Estado

    def pressionar_mouse(self, x, y):
        # cria um novo retângulo e o define como a figura em construção
        self.controller.figura_atual = Retangulo(x, y, self.controller.cor_borda, self.controller.cor_preench)