from tkinter import *
from tkinter import ttk
# [MUDANÇA 1] Importando as classes do arquivo da Ellen
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

# Quando mouse é pressionado (Mantido original)
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    cor_borda = cores_pt_en[cor_borda_var.get()]
    cor_preench = cores_pt_en[cor_preench_var.get()]
    
    if tipo == 'Rabisco':
        figura_nova = (tipo, [(event.x, event.y)], cor_borda, cor_preench)
    else: 
        figura_nova = (tipo, (event.x, event.y, event.x, event.y), cor_borda, cor_preench)

# Quando mouse é movido com o botão pressionado (Mantido original)
def atualizar_figura_nova(event):
    global figura_nova
    tipo, valores, cor_borda, cor_preench = figura_nova
    
    if tipo == "Rabisco":
        valores.append((event.x, event.y))
        figura_nova = (tipo, valores, cor_borda, cor_preench)
        
    elif tipo == "Círculo":
        x1, y1 = valores[0], valores[1]
        raio = max(abs(event.x - x1), abs(event.y - y1))
        x2 = x1 + (raio if event.x > x1 else -raio)
        y2 = y1 + (raio if event.y > y1 else -raio)
        figura_nova = (tipo, (x1, y1, x2, y2), cor_borda, cor_preench)
        
    else: 
        figura_nova = (tipo, (valores[0], valores[1], event.x, event.y), cor_borda, cor_preench)
        
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto (Mantido original)
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

# [MUDANÇA 2] Adaptando as funções de desenho para aceitarem a nova Orientação a Objetos
def desenhar_figuras():
    canvas.delete("all")
    for fig in figuras:
        if hasattr(fig, 'desenhar'): # Se for da classe da Ellen
            fig.desenhar(canvas, finalizada=True)
        else: # Se for do modo antigo
            desenhar_forma(fig, finalizada=True)

def desenhar_figura_nova():
    if figura_nova:
        if hasattr(figura_nova, 'desenhar'):
            figura_nova.desenhar(canvas, finalizada=False)
        else:
            desenhar_forma(figura_nova, finalizada=False)

def desenhar_forma(figura, finalizada):  
    tipo, valores, cor_borda, cor_preench = figura
    traco = () if finalizada else (4, 2)
    
    if tipo == "Linha":
        canvas.create_line(*valores, fill=cor_borda, dash=traco)
    elif tipo == "Rabisco":
        canvas.create_line(valores, fill=cor_borda, dash=traco)
    elif tipo == "Retângulo":
        canvas.create_rectangle(*valores, outline=cor_borda, fill=cor_preench, dash=traco)
    elif tipo in ["Oval", "Círculo"]:
        canvas.create_oval(*valores, outline=cor_borda, fill=cor_preench, dash=traco)

def incompleta(figura):
    tipo, valores, _, _ = figura
    if tipo == "Rabisco":
        return len(valores) <= 1
    else: 
        return (valores[0], valores[1]) == (valores[2], valores[3])

def limpar_tela():
    global figuras
    figuras = []
    desenhar_figuras()

#******* MAIN *******# (Mantido original)

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
                             'Linha', 'Linha', 'Rabisco', 'Retângulo', 'Oval', 'Círculo')
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

root.mainloop()