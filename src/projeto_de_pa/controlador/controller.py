from modelo.persistencia import abrir_desenho, salvar_desenho

from .estados.estado_circulo import EstadoCirculo
from .estados.estado_linha import EstadoLinha
from .estados.estado_oval import EstadoOval
from .estados.estado_poligono import EstadoPoligono
from .estados.estado_rabisco import EstadoRabisco
from .estados.estado_retangulo import EstadoRetangulo


class Controlador:

    def __init__(self, desenho):
        self.desenho = desenho
        self.figura_atual = None
        self.estado = EstadoLinha(self)
        self.cor_borda = "black"
        self.cor_preench = ""
        self.view = None

    def definir_view(self, view):
        self.view = view

    def selecionar_figura(self, tipo):
        if tipo == "linha":
            self.estado = EstadoLinha(self)
        elif tipo == "retangulo":
            self.estado = EstadoRetangulo(self)
        elif tipo == "oval":
            self.estado = EstadoOval(self)
        elif tipo == "circulo":
            self.estado = EstadoCirculo(self)
        elif tipo == "rabisco":
            self.estado = EstadoRabisco(self)
        elif tipo == "poligono":
            self.estado = EstadoPoligono(self)

    def alterar_cor_borda(self, cor):
        self.cor_borda = cor

    def alterar_cor_preench(self, cor):
        self.cor_preench = cor

    def limpar(self):
        self.desenho.limpar()
        if self.view:
            self.view.redesenhar()

    def pressionar_mouse(self, x, y):
        self.estado.pressionar_mouse(x, y)

    def mover_mouse(self, x, y):
        self.estado.mover_mouse(x, y)

    def soltar_mouse(self, x, y):
        self.estado.soltar_mouse(x, y)

    def finalizar_poligono(self):
        self.estado.finalizar()

    def obter_figuras(self):
        return self.desenho.figuras

    def salvar_desenho(self, caminho):
        if caminho:
            salvar_desenho(self.desenho, caminho)

    def abrir_desenho(self, caminho):
        if caminho:
            self.desenho.figuras = abrir_desenho(caminho)
            if self.view:
                self.view.redesenhar()