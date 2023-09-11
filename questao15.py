class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

def encontrar_nos_filhos(no):
    return no.filhos

raiz = NoArvore(1)
raiz.filhos.append(NoArvore(2))
raiz.filhos.append(NoArvore(3))
raiz.filhos[0].filhos.append(NoArvore(4))
raiz.filhos[0].filhos.append(NoArvore(5))
raiz.filhos[1].filhos.append(NoArvore(6))

nos_filhos_do_2 = encontrar_nos_filhos(raiz.filhos[0])
valores_dos_nos_filhos_do_2 = [no.valor for no in nos_filhos_do_2]
print("Nós filhos do nó 2:", valores_dos_nos_filhos_do_2)
