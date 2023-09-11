class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

def encontrar_nos_no_nivel(raiz, nivel_alvo):
    nos_no_nivel = []

    def buscar_nos_no_nivel_atual(no, nivel_atual):
        if nivel_atual == nivel_alvo:
            nos_no_nivel.append(no.valor)
        elif nivel_atual < nivel_alvo:
            for filho in no.filhos:
                buscar_nos_no_nivel_atual(filho, nivel_atual + 1)

    buscar_nos_no_nivel_atual(raiz, 1)  

    return nos_no_nivel

raiz = No(1)
raiz.filhos.append(No(2))
raiz.filhos.append(No(3))
raiz.filhos.append(No(4))
raiz.filhos[0].filhos.append(No(5))
raiz.filhos[0].filhos.append(No(6))
raiz.filhos[2].filhos.append(No(7))
raiz.filhos[2].filhos.append(No(8))

nos_no_nivel_2 = encontrar_nos_no_nivel(raiz, 2)
print("Nós no nível 2:", nos_no_nivel_2)
