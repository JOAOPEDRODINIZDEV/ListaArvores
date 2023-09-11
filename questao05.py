class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def travessia_em_ordem(raiz):
    resultado = []
    if raiz:
        resultado = travessia_em_ordem(raiz.esquerda)
        resultado.append(raiz.valor)
        resultado += travessia_em_ordem(raiz.direita)
    return resultado



raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

resultado_em_ordem = travessia_em_ordem(raiz)
print(resultado_em_ordem)