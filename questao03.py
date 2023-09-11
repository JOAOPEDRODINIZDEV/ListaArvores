class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def contem_valor(self, valor):
        return self._contem_valor_recursivo(self.raiz, valor)

    def _contem_valor_recursivo(self, no, valor):
        if no is None:
            return False

        if no.valor == valor:
            return True

        if valor < no.valor:
            return self._contem_valor_recursivo(no.esquerda, valor)
        else:
            return self._contem_valor_recursivo(no.direita, valor)


arvore = Arvore()

arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

print(arvore.contem_valor(4)) 
print(arvore.contem_valor(9))  
