from tkinter import *
from tkinter import filedialog, ttk


class View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Conecta a View de volta no Controller
        self.controller.definir_view(self)

        # Dicionários para traduzir o que o usuário vê (PT) para o que o controller entende (EN e sem acento)
        self.traduzir_figura = {
            "Linha": "linha",
            "Rabisco": "rabisco",
            "Retângulo": "retangulo",
            "Oval": "oval",
            "Círculo": "circulo",
            "Polígono": "poligono",
        }
        self.traduzir_cor = {
            "Preto": "black",
            "Branco": "white",
            "Vermelho": "red",
            "Verde": "green",
            "Azul": "blue",
            "Amarelo": "yellow",
            "Nenhum": "",
        }

        self.cores_opcoes = [
            "Preto",
            "Branco",
            "Vermelho",
            "Verde",
            "Azul",
            "Amarelo",
        ]
        self.cores_preench_opcoes = ["Nenhum"] + self.cores_opcoes

        self.paddings = {
            "padx": 5,
            "pady": 5,
        }  # Espaçamento padrão utilizado nos componentes da interface
        self.frame = self.criar_frame()

        # Cria os menus de seleção e botões de ação
        self.tipo_figura_var = self.criar_menu_figuras()
        self.cor_borda_var = self.criar_menu_borda()
        self.cor_preench_var = self.criar_menu_preench()

        self.criar_botoes_persistencia()
        self.criar_botao_limpar()

        self.canvas = self.criar_canvas()
        self.registrar_eventos()  # Associa os eventos do mouse aos métodos da View

        self.frame.pack()

    def criar_frame(self):
        return Frame(self.root)

    def criar_menu_figuras(self):
        # Cria o menu responsável pela seleção da figura
        label = ttk.Label(self.frame, text="Figura:")
        label.grid(column=0, row=0, sticky=W, **self.paddings)

        tipo_figura_var = StringVar(self.root, "Linha")

        option_menu = ttk.OptionMenu(
            self.frame,
            tipo_figura_var,
            "Linha",
            *self.traduzir_figura.keys(),
            command=self.notificar_ferramenta,
        )
        option_menu.grid(column=1, row=0, sticky=W, **self.paddings)

        return tipo_figura_var

    def criar_menu_borda(self):
        # Cria o menu responsável pela seleção da cor da borda
        label_cor_borda = ttk.Label(self.frame, text="Borda:")
        label_cor_borda.grid(column=2, row=0, sticky=W, **self.paddings)

        cor_borda_var = StringVar(self.root, "Preto")

        menu_cor_borda = ttk.OptionMenu(
            self.frame,
            cor_borda_var,
            self.cores_opcoes[0],
            *self.cores_opcoes,
            command=self.notificar_cor_borda,
        )
        menu_cor_borda.grid(column=3, row=0, sticky=W, **self.paddings)

        return cor_borda_var

    def criar_menu_preench(self):
        # Cria o menu para selecionar a cor do preenchimento
        label_cor_preench = ttk.Label(self.frame, text="Fundo:")
        label_cor_preench.grid(column=4, row=0, sticky=W, **self.paddings)

        cor_preench_var = StringVar(self.root, "Nenhum")

        menu_cor_preench = ttk.OptionMenu(
            self.frame,
            cor_preench_var,
            self.cores_preench_opcoes[0],
            *self.cores_preench_opcoes,
            command=self.notificar_cor_preench,
        )
        menu_cor_preench.grid(column=5, row=0, sticky=W, **self.paddings)

        return cor_preench_var

    def criar_botoes_persistencia(self):
        # Adiciona os botões de Salvar e Abrir arquivo
        btn_salvar = ttk.Button(
            self.frame, text="Salvar", command=self.acionar_salvar
        )
        btn_salvar.grid(column=6, row=0, sticky=W, **self.paddings)

        btn_abrir = ttk.Button(
            self.frame, text="Abrir", command=self.acionar_abrir
        )
        btn_abrir.grid(column=7, row=0, sticky=W, **self.paddings)

    def criar_botao_limpar(self):
        # O botão chama o método do Controller
        btn_limpar = ttk.Button(
            self.frame, text="Limpar Tela", command=self.controller.limpar
        )
        btn_limpar.grid(column=8, row=0, sticky=W, **self.paddings)

    def criar_canvas(self):
        # Cria o local onde as figuras serão desenhadas
        canvas = Canvas(self.frame, bg="white", width=700, height=600)
        canvas.grid(column=0, row=1, columnspan=9, sticky=W, **self.paddings)
        return canvas

    # --- Handlers de Ação de Persistência ---
    def acionar_salvar(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".pnt",
            filetypes=[
                ("Arquivos de Desenho", "*.pnt"),
                ("Todos os arquivos", "*.*"),
            ],
        )
        if caminho:
            self.controller.salvar_desenho(caminho)

    def acionar_abrir(self):
        caminho = filedialog.askopenfilename(
            filetypes=[
                ("Arquivos de Desenho", "*.pnt"),
                ("Todos os arquivos", "*.*"),
            ]
        )
        if caminho:
            self.controller.abrir_desenho(caminho)

    def registrar_eventos(self):
        # --- Vinculação dos Eventos de Mouse ---
        self.canvas.bind("<ButtonPress-1>", self.capturar_clique)
        self.canvas.bind("<B1-Motion>", self.capturar_arrasto)
        self.canvas.bind("<Motion>", self.capturar_movimento_solto)
        self.canvas.bind("<ButtonRelease-1>", self.capturar_soltura)
        self.canvas.bind("<Double-Button-1>", self.capturar_duplo_clique)

    # --- Métodos de comunicação ---
    def notificar_ferramenta(self, valor_selecionado):
        tipo = self.traduzir_figura[valor_selecionado]
        self.controller.selecionar_figura(tipo)

    def notificar_cor_borda(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_borda(cor)

    def notificar_cor_preench(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_preench(cor)

    # --- Handlers de Eventos de Mouse ---
    def capturar_clique(self, event):
        self.controller.pressionar_mouse(event.x, event.y)

    def capturar_arrasto(self, event):
        self.controller.mover_mouse(event.x, event.y)

    def capturar_movimento_solto(self, event):
        self.controller.mover_mouse(event.x, event.y)

    def capturar_soltura(self, event):
        self.controller.soltar_mouse(event.x, event.y)

    def capturar_duplo_clique(self, event):
        self.controller.finalizar_poligono()

    # --- MOTOR DE DESENHO ---
    def redesenhar(self):
        self.canvas.delete("all")

        for fig in self.controller.obter_figuras():
            self._renderizar_figura(fig, finalizada=True)

        fig_atual = self.controller.figura_atual
        if fig_atual:
            self._renderizar_figura(fig_atual, finalizada=False)

    def _renderizar_figura(self, fig, finalizada):
        nome_classe = fig.__class__.__name__

        if nome_classe == "Linha":
            self.canvas.create_line(
                fig.x1, fig.y1, fig.x2, fig.y2, fill=fig.cor_borda, width=2
            )

        elif nome_classe == "Retangulo":
            self.canvas.create_rectangle(
                fig.x1,
                fig.y1,
                fig.x2,
                fig.y2,
                outline=fig.cor_borda,
                fill=fig.cor_preench,
                width=2,
            )

        elif nome_classe == "Oval":
            self.canvas.create_oval(
                fig.x1,
                fig.y1,
                fig.x2,
                fig.y2,
                outline=fig.cor_borda,
                fill=fig.cor_preench,
                width=2,
            )

        elif nome_classe == "Circulo":
            self.canvas.create_oval(
                fig.x - fig.raio,
                fig.y - fig.raio,
                fig.x + fig.raio,
                fig.y + fig.raio,
                outline=fig.cor_borda,
                fill=fig.cor_preench,
                width=2,
            )

        elif nome_classe == "Rabisco":
            for i in range(len(fig.pontos) - 1):
                x1, y1 = fig.pontos[i]
                x2, y2 = fig.pontos[i + 1]
                self.canvas.create_line(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=fig.cor_borda,
                    width=2,
                    capstyle=ROUND,
                    smooth=True,
                )

        elif nome_classe == "Poligono":
            if len(fig.vertices) >= 3 and finalizada:
                coordenadas_planas = [
                    coord for vertice in fig.vertices for coord in vertice
                ]
                self.canvas.create_polygon(
                    coordenadas_planas,
                    outline=fig.cor_borda,
                    fill=fig.cor_preench,
                    width=2,
                )
            else:
                for i in range(len(fig.vertices) - 1):
                    x1, y1 = fig.vertices[i]
                    x2, y2 = fig.vertices[i + 1]
                    self.canvas.create_line(
                        x1, y1, x2, y2, fill=fig.cor_borda, width=2
                    )