class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def travessia_pos_ordem(raiz):
    if raiz is None:
        return []
    
    resultado = []  
    resultado += travessia_pos_ordem(raiz.esquerda)  
    resultado += travessia_pos_ordem(raiz.direita)  
    resultado.append(raiz.valor)  
    
    return resultado


raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

resultado_pos_ordem = travessia_pos_ordem(raiz)
print(resultado_pos_ordem)
