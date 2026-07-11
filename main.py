from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    
    if tipo == 'Rabisco':
        figura_nova = (tipo, [(event.x, event.y)])
    else: 
        figura_nova = (tipo, (event.x, event.y, event.x, event.y))

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    tipo, valores = figura_nova
    
    if tipo == "Rabisco":
        valores.append((event.x, event.y))
        figura_nova = (tipo, valores)
    else: 
        figura_nova = (tipo, (valores[0], valores[1], event.x, event.y))
        
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values in figuras:
        if fig == "Linha":
            canvas.create_line(values[0], values[1], values[2], values[3])
        elif fig == "Retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3])
        else: # fig == "Rabisco"
            canvas.create_line(values)

def desenhar_figura_nova():
    if figura_nova:
        fig, values = figura_nova
        if fig == "Linha":
            canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
        elif fig == "Retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))
        else: # fig == "Rabisco"
            canvas.create_line(values, dash=(4, 2))

def incompleta(figura):
    fig, values = figura
    if fig == "Rabisco":
        return len(values) <= 1
    else: 
        return (values[0], values[1]) == (values[2], values[3])

#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5} 

label = ttk.Label(frame,  text='Figura:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root) 
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retângulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()