from modelo.circulo import Circulo
from .estado import Estado

class EstadoCirculo(Estado): # herda os métodos criados na classe Estado 

    def pressionar_mouse(self, x, y): # inicia a criação do círculo
        # cria um novo círculo e o define como a figura em construção
        self.controller.figura_atual = Circulo(x, y, self.controller.cor_borda, self.controller.cor_preench) 