from .estados.estado_linha import EstadoLinha
from .estados.estado_retangulo import EstadoRetangulo
from .estados.estado_oval import EstadoOval
from .estados.estado_circulo import EstadoCirculo
from .estados.estado_rabisco import EstadoRabisco
from .estados.estado_poligono import EstadoPoligono


class Controlador:
    def __init__(self, desenho):
        self.desenho = desenho # guarda a referência para o objeto Desenho do model
        self.figura_atual = None # ainda não começou a desenhar, então não existe figura
        self.estado = EstadoLinha(self) # define o estado inicial como linha
        self.cor_borda = "black"
        self.cor_preench = ""
        self.view = None  # a View será associada depois

    def definir_view(self, view): # conecta controller e view
        self.view = view

    def selecionar_figura(self, tipo): # altera o estado conforme a figura selecionada
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

    # Altera as cores da borda e do preenchimento
    def alterar_cor_borda(self, cor):
        self.cor_borda = cor

    def alterar_cor_preench(self, cor):
        self.cor_preench = cor

    def limpar(self): # Limpa o desenho
        self.desenho.limpar()
        if self.view:
            self.view.redesenhar() # atualiza a View após limpar o desenho

    # Quando pressiona o mouse
    def pressionar_mouse(self, x, y): # inicia a criação da figura selecionada
        self.estado.pressionar_mouse(x, y)

    # Quando o mouse é movimentado
    def mover_mouse(self, x, y):
        self.estado.mover_mouse(x, y)

    # Quando solta o botão
    def soltar_mouse(self, x, y):
        self.estado.soltar_mouse(x, y)
    
    def finalizar_poligono(self): # finaliza o polígono adicionando-o ao desenho
        self.estado.finalizar()

    def obter_figuras(self): # retorna todas as figuras armazenadas no desenho
        return self.desenho.figuras