from abc import ABC, abstractmethod

class Estado(ABC):

    def __init__(self, controller):
        self.controller = controller # guarda a referência para o controlador

    @abstractmethod
    def pressionar_mouse(self, x, y): # inicia o desenho da figura selecionada
        pass
    
    def mover_mouse(self, x, y):

        if self.controller.figura_atual: # só atualiza se existe uma figura sendo construída
            self.controller.figura_atual.atualizar(x, y)
            self.controller.view.redesenhar() # atualiza a view para mostrar as mudanças
    
    def soltar_mouse(self, x, y):

        if self.controller.figura_atual:
            self.controller.figura_atual.atualizar(x, y)

            if not self.controller.figura_atual.incompleta(): # impede que figuras incompletas sejam adicionadas ao desenho
                self.controller.desenho.adicionar(self.controller.figura_atual)

            self.controller.figura_atual = None
            self.controller.view.redesenhar()

    def finalizar(self):
        # utilizado apenas pelo estado do polígono
        pass