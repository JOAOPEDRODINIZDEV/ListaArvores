class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def verificar_arvore_de_busca_valida(raiz):
    def em_ordem_valida(no, min_valor=float('-inf'), max_valor=float('inf')):
        if no is None:
            return True
        
        if no.valor <= min_valor or no.valor >= max_valor:
            return False
        
        return (em_ordem_valida(no.esquerda, min_valor, no.valor) and
                em_ordem_valida(no.direita, no.valor, max_valor))
    
    return em_ordem_valida(raiz)

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.direita = No(20)

e_valida = verificar_arvore_de_busca_valida(raiz)
print("A árvore é uma árvore de busca válida?", e_valida)
