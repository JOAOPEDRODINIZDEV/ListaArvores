class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_caminho_ate_no(raiz, valor_alvo):
    def buscar_caminho_atual(no, valor_alvo, caminho_atual):
        if no is None:
            return []

        caminho_atual.append(no.valor)
        
        if no.valor == valor_alvo:
            return caminho_atual.copy()

        caminho_esquerda = buscar_caminho_atual(no.esquerda, valor_alvo, caminho_atual.copy())
        caminho_direita = buscar_caminho_atual(no.direita, valor_alvo, caminho_atual.copy())

        if caminho_esquerda:
            return caminho_esquerda
        if caminho_direita:
            return caminho_direita
        
        return []

    caminho = buscar_caminho_atual(raiz, valor_alvo, [])
    return caminho if caminho else None  

raiz = No(2)
raiz.esquerda = No(3)
raiz.direita = No(4)
raiz.esquerda.esquerda = No(5)
raiz.esquerda.direita = No(6)
raiz.direita.direita = No(7)

caminho_ate_5 = encontrar_caminho_ate_no(raiz, 5)
print("Caminho até o nó 5:", caminho_ate_5)
