class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def travessia_pre_ordem(raiz):
    if raiz is None:
        return []
    
    resultado = [raiz.valor] 
    resultado += travessia_pre_ordem(raiz.esquerda)  
    resultado += travessia_pre_ordem(raiz.direita)  
    
    return resultado

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)


resultado_pre_ordem = travessia_pre_ordem(raiz)
print(resultado_pre_ordem)
