class Deque:
    def __init__(self):
        self.items = []

    def adicionar_inicio(self, item):
        self.items.insert(0, item)

    def adicionar_final(self, item):
        self.items.append(item)

    def remover_inicio(self):
        return self.items.pop(0)

    def tamanho(self):
        return len(self.items)

    def esta_vazio(self):
        return self.items == []


class CalculadoraMediaMovel:
    def __init__(self, k):
        self.deque = Deque()
        self.k = k
        self.soma_janela = 0
        self.medias_moveis = []

    def adicionar_elemento(self, elemento):
        if self.deque.tamanho() == self.k:
            self.soma_janela -= self.deque.remover_inicio()

        self.deque.adicionar_final(elemento)
        self.soma_janela += elemento

        if self.deque.tamanho() == self.k:
            media = self.soma_janela / self.k
            self.medias_moveis.append(media)
        else:
            self.medias_moveis.append(None)

    def calcular_medias_moveis(self, dados_trafego):
        for elemento in dados_trafego:
            self.adicionar_elemento(elemento)

    def obter_medias_moveis(self):
        return self.medias_moveis


# Exemplo de uso:
dados_trafego = [120, 130, 150, 140, 160, 170, 180, 200, 190, 210]
k = 9  # Tamanho da janela

calculadora = CalculadoraMediaMovel(k)
calculadora.calcular_medias_moveis(dados_trafego)
medias_moveis = calculadora.obter_medias_moveis()

print("Médias móveis calculadas:", medias_moveis)
