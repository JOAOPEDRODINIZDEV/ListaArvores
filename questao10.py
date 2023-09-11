class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_valor_maximo(raiz):
    if raiz is None:
        return float('-inf')   

    valor_max_esquerda = encontrar_valor_maximo(raiz.esquerda)
    valor_max_direita = encontrar_valor_maximo(raiz.direita)

    return max(raiz.valor, valor_max_esquerda, valor_max_direita)


raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.direita = No(20)

maximo_valor = encontrar_valor_maximo(raiz)
print("Valor máximo na árvore:", maximo_valor)
