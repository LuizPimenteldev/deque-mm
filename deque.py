class Deque:
    def __init__(self):   # definindo a inicialização da classe.
        self.items = []   # criando a lista items.

    def adicionar_inicio(self, item):   # adicionando um novo item no início do deque.
        self.items.insert(0, item)      # o insert insere o item na lista na posição 0 e desloca os elementos pra direita.

    def adicionar_final(self, item):   # aqui tem o mesmo propósito, porém no final do deque.
        self.items.append(item)        # o append fica melhor de usar pois sempre coloca o elemento no final, e o insert é usado pra colocar na posição específica, pra evitar algum erro de alocação.
                                        # (obs poderia utilizar o insert sem problema, mas preferimos não usar, pra não ter que criar um len pros itens XD)

    def remover_inicio(self):         # remove o item no inicio 
        return self.items.pop(0)

    def remover_final(self):
        if self.esta_vazio():
            raise ValueError("O deque está vazio, não é possível remover elementos.")

        return self.items.pop()


    def tamanho(self):
        return len(self.items)

    def esta_vazio(self):
        return self.items == []


class CalculadoraMediaMovel:
    def __init__(self, k):
        if k <= 0:
            raise ValueError("O tamanho da janela (k) deve ser maior que zero.")
        
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
        if not dados_trafego:
            raise ValueError("Os dados de tráfego não podem ser vazios.")
        
        for elemento in dados_trafego:
            self.adicionar_elemento(elemento)

    def obter_medias_moveis(self):
        return self.medias_moveis


# Exemplo de uso:
dados_trafego = [120, 130, 150, 140, 160, 170, 180, 200, 190, 210]
k = 3  # Tamanho da janela

calculadora = CalculadoraMediaMovel(k)
calculadora.calcular_medias_moveis(dados_trafego)
medias_moveis = calculadora.obter_medias_moveis()

print("Médias móveis calculadas:", medias_moveis)
