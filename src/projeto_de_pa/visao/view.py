from tkinter import *
from tkinter import ttk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        # Conecta a View de volta no Controller
        self.controller.definir_view(self) 

        # Dicionários para traduzir o que o usuário vê (PT) para o que o controller entende (EN e sem acento)
        self.traduzir_figura = {
            'Linha': 'linha', 'Rabisco': 'rabisco', 'Retângulo': 'retangulo',
            'Oval': 'oval', 'Círculo': 'circulo', 'Polígono': 'poligono'
        }
        self.traduzir_cor = {
            'Preto': 'black', 'Branco': 'white', 'Vermelho': 'red',
            'Verde': 'green', 'Azul': 'blue', 'Amarelo': 'yellow', 'Nenhum': ''
        }

        self.cores_opcoes = ['Preto', 'Branco', 'Vermelho', 'Verde', 'Azul', 'Amarelo']
        self.cores_preench_opcoes = ['Nenhum'] + self.cores_opcoes

        self.configurar_interface()

    def configurar_interface(self):
        frame = Frame(self.root)
        paddings = {'padx': 5, 'pady': 5}

        # --- Menus ---
        label = ttk.Label(frame, text='Figura:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root, 'Linha')
        option_menu = ttk.OptionMenu(frame, self.tipo_figura_var, 'Linha', *self.traduzir_figura.keys(), command=self.notificar_ferramenta)
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        label_cor_borda = ttk.Label(frame, text='Borda:')
        label_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

        self.cor_borda_var = StringVar(self.root, 'Preto')
        menu_cor_borda = ttk.OptionMenu(frame, self.cor_borda_var, self.cores_opcoes[0], *self.cores_opcoes, command=self.notificar_cor_borda)
        menu_cor_borda.grid(column=3, row=0, sticky=W, **paddings)

        label_cor_preench = ttk.Label(frame, text='Fundo:')
        label_cor_preench.grid(column=4, row=0, sticky=W, **paddings)

        self.cor_preench_var = StringVar(self.root, 'Nenhum')
        menu_cor_preench = ttk.OptionMenu(frame, self.cor_preench_var, self.cores_preench_opcoes[0], *self.cores_preench_opcoes, command=self.notificar_cor_preench)
        menu_cor_preench.grid(column=5, row=0, sticky=W, **paddings)

        # O botão chama o método do Controller
        btn_limpar = ttk.Button(frame, text="Limpar Tela", command=self.controller.limpar)
        btn_limpar.grid(column=6, row=0, sticky=W, **paddings)

        # --- Canvas ---
        self.canvas = Canvas(frame, bg='white', width=700, height=600)
        self.canvas.grid(column=0, row=1, columnspan=7, sticky=W, **paddings)

        # --- Vinculação dos Eventos de Mouse ---
        self.canvas.bind('<ButtonPress-1>', self.capturar_clique)
        self.canvas.bind('<B1-Motion>', self.capturar_arrasto)
        self.canvas.bind('<Motion>', self.capturar_movimento_solto)
        self.canvas.bind('<ButtonRelease-1>', self.capturar_soltura)
        self.canvas.bind('<Double-Button-1>', self.capturar_duplo_clique)

        frame.pack()

    # --- Métodos de comunicação (A View avisa o Controller das mudanças de estado) ---
    def notificar_ferramenta(self, valor_selecionado):
        tipo = self.traduzir_figura[valor_selecionado]
        self.controller.selecionar_figura(tipo)

    def notificar_cor_borda(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_borda(cor)

    def notificar_cor_preench(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_preench(cor)

    # --- Handlers de Eventos (Repassam apenas coordenadas x e y para o controller) ---
    def capturar_clique(self, event):
        self.controller.pressionar_mouse(event.x, event.y)

    def capturar_arrasto(self, event):
        self.controller.mover_mouse(event.x, event.y)

    def capturar_movimento_solto(self, event):
        self.controller.mover_mouse(event.x, event.y)

    def capturar_soltura(self, event):
        self.controller.soltar_mouse()

    def capturar_duplo_clique(self, event):
        self.controller.finalizar_poligono()

    # --- MOTOR DE DESENHO (Obrigatório do MVC) ---
    def redesenhar(self):
        # 1. Limpa o Canvas completamente
        self.canvas.delete("all")

        # 2. Desenha as figuras que já estão finalizadas e salvas no Modelo
        for fig in self.controller.obter_figuras():
            self._renderizar_figura(fig, finalizada=True)

        # 3. Desenha a figura que está sendo criada/arrastada neste instante (se houver)
        fig_atual = self.controller.figura_atual
        if fig_atual:
            self._renderizar_figura(fig_atual, finalizada=False)

    def _renderizar_figura(self, fig, finalizada):
        nome_classe = fig.__class__.__name__

        if nome_classe == 'Linha':
            self.canvas.create_line(fig.x1, fig.y1, fig.x2, fig.y2, fill=fig.cor_borda, width=2)

        elif nome_classe == 'Retangulo':
            self.canvas.create_rectangle(fig.x1, fig.y1, fig.x2, fig.y2, outline=fig.cor_borda, fill=fig.cor_preench, width=2)

        elif nome_classe == 'Oval':
            self.canvas.create_oval(fig.x1, fig.y1, fig.x2, fig.y2, outline=fig.cor_borda, fill=fig.cor_preench, width=2)

        elif nome_classe == 'Circulo':
            self.canvas.create_oval(
                fig.x - fig.raio, fig.y - fig.raio,
                fig.x + fig.raio, fig.y + fig.raio,
                outline=fig.cor_borda, fill=fig.cor_preench, width=2
            )

        elif nome_classe == 'Rabisco':
            for i in range(len(fig.pontos) - 1):
                x1, y1 = fig.pontos[i]
                x2, y2 = fig.pontos[i+1]
                self.canvas.create_line(x1, y1, x2, y2, fill=fig.cor_borda, width=2, capstyle=ROUND, smooth=True)

        elif nome_classe == 'Poligono':
            if len(fig.vertices) >= 3 and finalizada:
                coordenadas_planas = [coord for vertice in fig.vertices for coord in vertice]
                self.canvas.create_polygon(coordenadas_planas, outline=fig.cor_borda, fill=fig.cor_preench, width=2)
            else:
                for i in range(len(fig.vertices) - 1):
                    x1, y1 = fig.vertices[i]
                    x2, y2 = fig.vertices[i+1]
                    self.canvas.create_line(x1, y1, x2, y2, fill=fig.cor_borda, width=2)