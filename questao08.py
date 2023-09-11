class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def travessia_em_niveis(raiz):
    if raiz is None:
        return []
    
    resultado = []  
    fila = [raiz]  
    
    while fila:
        no_atual = fila.pop(0) 
        resultado.append(no_atual.valor)  
        
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)
    
    return resultado


raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)


resultado_em_niveis = travessia_em_niveis(raiz)
print(resultado_em_niveis)
