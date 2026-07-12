from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self,cor_borda,cor_preench):
        self.cor_borda = cor_borda
        self.cor_preench = cor_preench
        self.finalizada = False

    @abstractmethod
    def atualizar(self, event):
        pass
    
    @abstractmethod
    def desenhar(self, canvas, finalizada):
        pass

    @abstractmethod
    def incompleta(self):
        pass

class Linha(Figura):

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, event):
        self.x2 = event.x
        self.y2 = event.y

    def desenhar(self, canvas, finalizada):
        if finalizada:
            traco = ()
        else:
            traco = (4,2)

        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=traco)

    def incompleta(self):
        return (self.x1 == self.x2) and (self.y1 == self.y2)