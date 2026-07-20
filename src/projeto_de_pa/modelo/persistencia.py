import pickle


def salvar_desenho(desenho, caminho_arquivo):
    with open(caminho_arquivo, "wb") as arquivo:
        pickle.dump(desenho.figuras, arquivo)


def carregar_desenho(caminho_arquivo):
    with open(caminho_arquivo, "rb") as arquivo:
        return pickle.load(arquivo)