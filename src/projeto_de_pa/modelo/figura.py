from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self, cor_borda, cor_preench): # guarda os atributos comuns a todas as figuras
        self.cor_borda = cor_borda
        self.cor_preench = cor_preench

    @abstractmethod  # Método abstrato para obrigar subclasses a implementar
    def atualizar(self, x, y):
        """Tirei o event pra ficar só no controller"""
        pass

    @abstractmethod
    def incompleta(self): 
        # informa se a figura ainda não existe
        pass