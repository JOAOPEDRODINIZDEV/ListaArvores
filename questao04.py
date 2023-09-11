class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def altura_arvore(raiz):
    if raiz is None:
        return 0

    altura_esquerda = altura_arvore(raiz.esquerda)
    altura_direita = altura_arvore(raiz.direita)

    return max(altura_esquerda, altura_direita + 1)

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)
raiz.esquerda.esquerda.esquerda = No(4)
raiz.esquerda.direita.direita = No(8)
altura = altura_arvore(raiz)
print("Altura da árvore:", altura)
