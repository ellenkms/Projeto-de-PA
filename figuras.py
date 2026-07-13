from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self, cor_borda, cor_preench): # guarda os atributos comuns a todas as figuras
        self.cor_borda = cor_borda
        self.cor_preench = cor_preench

    @abstractmethod  # Método abstrato para obrigar subclasses a implementar
    def atualizar(self, event):
        pass
    
    @abstractmethod
    def desenhar(self, canvas, finalizada): 
        # desenha a figura no canvas
        pass

    def traco(self, finalizada): 
        # Retorna o estilo do traço: contínuo quando a figura está finalizada e tracejado enquanto está sendo desenhada.
        if finalizada:
            return ()
        return (4, 2)

    @abstractmethod
    def incompleta(self): 
        # informa se a figura ainda não existe
        pass



class Figura2Pontos(Figura, ABC):  # herda da classe Figura
    """reúne os comportamentos comuns de Linha, Retângulo e Oval."""

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x1 = x  # armazena coordenadas do ponto inicial
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, event):
        self.x2 = event.x  # atualiza somente o ponto final, o ponto inicial é fixo
        self.y2 = event.y

    def incompleta(self): # se os pontos forem iguais, a figura não existe
        return (self.x1 == self.x2) and (self.y1 == self.y2)



class Linha(Figura2Pontos): # herda da classe Figura2Pontos

    def desenhar(self, canvas, finalizada):

        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=self.traco(finalizada))

class Retangulo(Figura2Pontos): # herda da classe Figura2Pontos

    def desenhar(self, canvas, finalizada):
        
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preench, dash=self.traco(finalizada))

class Oval(Figura2Pontos): # herda da classe Figura2Pontos

    def desenhar(self, canvas, finalizada):
        
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preench, dash=self.traco(finalizada))
    
class Circulo(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.x = x  # armazena as coordenadas do ponto central
        self.y = y
        self.raio = 0 

    def atualizar(self, event):
        self.raio = max(abs(event.x - self.x), abs(event.y - self.y))  # atualiza somente o raio, o ponto central é fixo

    def desenhar(self, canvas, finalizada):

        canvas.create_oval(self.x - self.raio, self.y - self.raio, self.x + self.raio, self.y + self.raio, outline=self.cor_borda, fill=self.cor_preench, dash=self.traco(finalizada)) 

    def incompleta(self):  # se o raio for igual a zero, não houve movimento e o círculo não existe
        return self.raio == 0

class Rabisco(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench) # chama o construtor de Figura
        self.pontos = [(x, y)] # armazena o primeiro ponto do Rabisco em uma lista para adicionar novos pontos
        
    def atualizar(self, event):
        self.pontos.append((event.x, event.y)) # adiciona novos pontos na lista
    
    def desenhar(self, canvas, finalizada):
        
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=self.traco(finalizada))
    
    def incompleta(self):
        return len(self.pontos) <= 1 # se houver menos de dois pontos o Rabisco está incompleto

class Poligono(Figura): # herda da classe Figura

    def __init__(self, x, y, cor_borda, cor_preench):
        super().__init__(cor_borda, cor_preench)  # chama o construtor de Figura
        self.vertices = [(x, y)] # armazena o primeiro vértice em uma lista para adicionar novos vértices

    def atualizar(self, event):
        self.vertices.append((event.x, event.y)) # adiciona novos vértices na lista
    
    def desenhar(self, canvas, finalizada):

        canvas.create_polygon(self.vertices, outline=self.cor_borda, fill=self.cor_preench, dash=self.traco(finalizada))

    def incompleta(self):
        return len(self.vertices) <= 2 # se houver menos de três vértices o Polígono está incompleto