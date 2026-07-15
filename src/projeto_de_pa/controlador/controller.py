from modelo.figura2pontos import Linha
from modelo.figura2pontos import Retangulo
from modelo.figura2pontos import Oval
from modelo.circulo import Circulo
from modelo.rabisco import Rabisco
from modelo.poligono import Poligono


class Controlador:
    def __init__(self, desenho):
        self.desenho = desenho # guarda a referência para o objeto Desenho do model
        self.figura_atual = None # ainda não começou a desenhar, então não existe figura
        self.tipo_figura = "linha" # define a figura inicial padrão
        self.cor_borda = "black"
        self.cor_preench = ""
        self.view = None  # a View será associada depois

    def definir_view(self, view): # conecta controller e view
        self.view = view

    def selecionar_figura(self, tipo): # Define a figura que será desenhada 
        self.tipo_figura = tipo

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
    def pressionar_mouse(self, x, y): # inicia o desenho da figura selecionada
        
        if self.tipo_figura == "poligono":
            if self.figura_atual is None: # se não existe polígono sendo desenhado, cria
                self.figura_atual = Poligono(x, y, self.cor_borda, self.cor_preench)
            else: # se já existe, adiciona um novo vértice
                self.figura_atual.adicionar_ponto(x, y)

        elif self.tipo_figura == "linha":
            self.figura_atual = Linha(x, y, self.cor_borda, self.cor_preench)

        elif self.tipo_figura == "retangulo":
            self.figura_atual = Retangulo(x, y, self.cor_borda, self.cor_preench)

        elif self.tipo_figura == "oval":
            self.figura_atual = Oval(x, y, self.cor_borda, self.cor_preench)

        elif self.tipo_figura == "circulo":
            self.figura_atual = Circulo(x, y, self.cor_borda, self.cor_preench)

        elif self.tipo_figura == "rabisco":
            self.figura_atual = Rabisco(x, y, self.cor_borda, self.cor_preench)

    # Quando o mouse é movimentado
    def mover_mouse(self, x, y):

        if self.figura_atual: # só atualiza se existe uma figura sendo construída
            self.figura_atual.atualizar(x, y)
            if self.view:
                self.view.redesenhar() # atualiza a view para mostrar as mudanças

    # Quando solta o botão
    def soltar_mouse(self):

        if self.tipo_figura == "poligono": # o polígono não termina quando solta o botão
            return
        
        if self.figura_atual:
            if not self.figura_atual.incompleta(): # evita figuras inválidas
                self.desenho.adicionar(self.figura_atual)
            self.figura_atual = None
            if self.view:
                self.view.redesenhar()
    
    def finalizar_poligono(self): # finaliza o polígono adicionando-o ao desenho
        if self.tipo_figura == "poligono" and self.figura_atual:
            self.figura_atual.finalizar_forma() # remove a guia móvel do último vértice
            if not self.figura_atual.incompleta():
                self.desenho.adicionar(self.figura_atual)
            self.figura_atual = None
            if self.view:
                self.view.redesenhar()

    def obter_figuras(self): # retorna todas as figuras armazenadas no desenho
        return self.desenho.figuras