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
        # O 'command' avisa automaticamente o controller quando o usuário muda a opção
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

        # O botão já chama direto o método do Controller
        btn_limpar = ttk.Button(frame, text="Limpar Tela", command=self.controller.limpar)
        btn_limpar.grid(column=6, row=0, sticky=W, **paddings)

        # --- Canvas ---
        self.canvas = Canvas(frame, bg='white', width=700, height=600)
        self.canvas.grid(column=0, row=1, columnspan=7, sticky=W, **paddings)

        frame.pack()

    # --- Métodos de comunicação (A View avisa o Controller das mudanças) ---
    def notificar_ferramenta(self, valor_selecionado):
        tipo = self.traduzir_figura[valor_selecionado]
        self.controller.selecionar_figura(tipo)

    def notificar_cor_borda(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_borda(cor)

    def notificar_cor_preench(self, valor_selecionado):
        cor = self.traduzir_cor[valor_selecionado]
        self.controller.alterar_cor_preench(cor)

    # Criamos o método vazio só para o programa não dar erro se o Controller chamar
    def redesenhar(self):
        pass