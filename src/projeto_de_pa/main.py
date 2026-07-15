from tkinter import *
from tkinter import ttk
from figuras import Linha, Retangulo, Oval, Circulo, Rabisco, Poligono

# Dicionário para traduzir as cores para o inglês
cores_pt_en = {
    'Preto': 'black',
    'Branco': 'white',
    'Vermelho': 'red',
    'Verde': 'green',
    'Azul': 'blue',
    'Amarelo': 'yellow',
    'Nenhum': '' 
}
cores_opcoes = ['Preto', 'Branco', 'Vermelho', 'Verde', 'Azul', 'Amarelo']
cores_preench_opcoes = ['Nenhum'] + cores_opcoes

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    cor_borda = cores_pt_en[cor_borda_var.get()]
    cor_preench = cores_pt_en[cor_preench_var.get()]
    
    if tipo == 'Polígono':
        # Se já estamos desenhando um polígono, apenas adiciona um ponto
        if isinstance(figura_nova, Poligono):
            figura_nova.adicionar_ponto(event.x, event.y)
        else:
            # Se for o primeiro clique, cria o polígono
            figura_nova = Poligono(event.x, event.y, cor_borda, cor_preench)
    else:
        # Para as outras formas, o comportamento original continua igual
        if tipo == 'Linha':
            figura_nova = Linha(event.x, event.y, cor_borda, cor_preench)
        elif tipo == 'Retângulo':
            figura_nova = Retangulo(event.x, event.y, cor_borda, cor_preench)
        elif tipo == 'Oval':
            figura_nova = Oval(event.x, event.y, cor_borda, cor_preench)
        elif tipo == 'Círculo':
            figura_nova = Circulo(event.x, event.y, cor_borda, cor_preench)
        elif tipo == 'Rabisco':
            figura_nova = Rabisco(event.x, event.y, cor_borda, cor_preench)

# Quando mouse é movido com o botão pressionado (Arraste)
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova:
        figura_nova.atualizar(event)
        desenhar_figuras()
        desenhar_figura_nova()

# NOVO: Quando o mouse apenas se move (sem clicar) - Faz a linha guia do Polígono seguir o cursor
def mover_mouse(event):
    global figura_nova
    if figura_nova and tipo_figura_var.get() == 'Polígono':
        figura_nova.atualizar(event)
        desenhar_figuras()
        desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    # O polígono NÃO é finalizado ao soltar o mouse, ele espera o duplo clique
    if tipo != 'Polígono':
        if figura_nova:
            if not figura_nova.incompleta(): 
                figuras.append(figura_nova) 
            figura_nova = None # Limpa a memória para o próximo desenho
        desenhar_figuras()

# NOVO: Quando rola o duplo-clique (Finaliza o Polígono de vez)
def finalizar_poligono(event):
    global figura_nova
    if isinstance(figura_nova, Poligono):
        figura_nova.finalizar_forma()
        if not figura_nova.incompleta():
            figuras.append(figura_nova)
        figura_nova = None # Limpa a memória para o próximo desenho
        desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig in figuras:
        fig.desenhar(canvas, finalizada=True)

def desenhar_figura_nova():
    if figura_nova:
        figura_nova.desenhar(canvas, finalizada=False)

def limpar_tela():
    global figuras, figura_nova
    figuras = []
    figura_nova = None
    desenhar_figuras()

#******* MAIN *******#

figuras = []       
figura_nova = None 

root = Tk()
root.title("Artes e Rabiscos")
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5} 

label = ttk.Label(frame, text='Figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root) 
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo', 'Polígono')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

label_cor_borda = ttk.Label(frame, text='Borda:')
label_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

cor_borda_var = StringVar(root)
menu_cor_borda = ttk.OptionMenu(frame, cor_borda_var, cores_opcoes[0], *cores_opcoes)
menu_cor_borda.grid(column=3, row=0, sticky=W, **paddings)

label_cor_preench = ttk.Label(frame, text='Fundo:')
label_cor_preench.grid(column=4, row=0, sticky=W, **paddings)

cor_preench_var = StringVar(root)
menu_cor_preench = ttk.OptionMenu(frame, cor_preench_var, cores_preench_opcoes[0], *cores_preench_opcoes)
menu_cor_preench.grid(column=5, row=0, sticky=W, **paddings)

btn_limpar = ttk.Button(frame, text="Limpar Tela", command=limpar_tela)
btn_limpar.grid(column=6, row=0, sticky=W, **paddings)

canvas = Canvas(frame, bg='white', width=700, height=600)
canvas.grid(column=0, row=1, columnspan=7, sticky=W, **paddings)

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
# Eventos novos ligados ao Polígono
canvas.bind('<Motion>', mover_mouse) 
canvas.bind('<Double-Button-1>', finalizar_poligono) 

root.mainloop()