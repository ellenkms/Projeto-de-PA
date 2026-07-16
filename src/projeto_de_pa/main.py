import sys
import os
from tkinter import Tk

# Garante que o Python encontre as pastas modelo, controlador e visao
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelo.desenho import Desenho
from controlador.controller import Controlador
from visao.view import View

def main():
    root = Tk()
    root.title("Artes e Rabiscos - Padrão MVC")

    # 1. Inicializa o Model
    desenho_model = Desenho()

    # 2. Inicializa o Controller passando o Model
    controlador = Controlador(desenho_model)

    # 3. Inicializa a View passando o root do Tkinter e o Controller
    app_view = View(root, controlador)

    # Roda o loop principal da aplicação
    root.mainloop()

if __name__ == "__main__":
    main()