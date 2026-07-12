from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self,cor_borda,cor_preench): # guarda o que todas as figuras possuem
        self.cor_borda = cor_borda
        self.cor_preench = cor_preench

    @abstractmethod  # Método abstrato para obrigar subclasses a implementar
    def atualizar(self, event):
        pass
    
    @abstractmethod
    def desenhar(self, canvas, finalizada):
        pass

    @abstractmethod
    def incompleta(self):
        pass

class Linha(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x1 = x  # armazena coordenadas do ponto inicial
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, event):
        self.x2 = event.x  # atualiza somente o ponto final, o ponto inicial é fixo
        self.y2 = event.y

    def desenhar(self, canvas, finalizada):
        if finalizada:
            traco = ()
        else:
            traco = (4,2)  # para a linha tracejada enquanto o mouse está pressionado

        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=traco)

    def incompleta(self): # se o início e o fim forem iguais, a linha tem comprimento zero
        return (self.x1 == self.x2) and (self.y1 == self.y2)

class Retangulo(Figura):  # Atenção: Igual a Linha

    def __init__(self, x, y, cor_borda, cor_preench): 
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x1 = x # armazena coordenadas do ponto inicial
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, event):
        self.x2 = event.x # atualiza somente o ponto final, o ponto inicial é fixo
        self.y2 = event.y

    def desenhar(self, canvas, finalizada):
        if finalizada:
            traco = ()
        else:
            traco = (4,2) # para a linha tracejada enquanto o mouse está pressionado
        
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline= self.cor_borda, fill=self.cor_preench, dash=traco)

    def incompleta(self): # se o início e o fim forem iguais, não existe retângulo
        return (self.x1 == self.x2) and (self.y1 == self.y2)
    
class Oval(Figura):  # Atenção: Igual a Linha

    def __init__(self, x, y, cor_borda, cor_preench): 
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x1 = x # armazena coordenadas do ponto inicial
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, event):
        self.x2 = event.x # atualiza somente o ponto final, o ponto inicial é fixo
        self.y2 = event.y
    
    def desenhar(self, canvas, finalizada):
        if finalizada:
            traco = ()
        else:
            traco = (4,2) # para a linha tracejada enquanto o mouse está pressionado
        
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill =self.cor_preench, dash=traco)

    def incompleta(self): # se os pontos forem iguais, não existe oval
        return (self.x1 == self.x2) and (self.y1 == self.y2)