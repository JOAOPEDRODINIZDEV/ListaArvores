class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def contar_nos(raiz):
    if raiz is None:
        return 0

    nos_esquerda = contar_nos(raiz.esquerda)
    nos_direita = contar_nos(raiz.direita)
    
    return nos_esquerda + nos_direita + 1



raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

total_de_nos = contar_nos(raiz)
print("Número total de nós na árvore:", total_de_nos)
