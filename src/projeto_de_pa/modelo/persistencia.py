import pickle


def salvar_desenho(desenho, caminho):
    """Salva a lista de figuras do desenho em um arquivo usando pickle."""
    with open(caminho, "wb") as arquivo:
        pickle.dump(desenho.figuras, arquivo)


def abrir_desenho(caminho):
    """Lê a lista de figuras de um arquivo salvo usando pickle."""
    with open(caminho, "rb") as arquivo:
        return pickle.load(arquivo)