class Deque:
    def __init__(self):   # definindo a inicialização da classe.
        self.items = []   # criando a lista items.

    def adicionar_inicio(self, item):   # adicionando um novo item no início do deque.
        self.items.insert(0, item)      # o insert insere o item na lista na posição 0 e desloca os elementos pra direita.

    def adicionar_final(self, item):   # aqui tem o mesmo propósito, porém no final do deque.
        self.items.append(item)        # o append fica melhor de usar pois sempre coloca o elemento no final, e o insert é usado pra colocar na posição específica, pra evitar algum erro de alocação.
                                        # (obs poderia utilizar o insert sem problema, mas preferimos não usar, pra não ter que criar um len pros itens XD).

    def remover_inicio(self):         # remove o item no inicio da lista na posição 0
        if self.esta_vazio():
            raise ValueError("O deque está vazio, não é possível remover elementos.")    # cria um condição para caso a lista não tenha items encerre o processo.
        return self.items.pop(0)       

    def remover_final(self):         # remove o item no final da lista
        if self.esta_vazio():
            raise ValueError("O deque está vazio, não é possível remover elementos.")    # //  //

        return self.items.pop()


    def tamanho(self):                # retorna o número de itens no deque.
        return len(self.items)

    def esta_vazio(self):             # verifica se o deque está vazio.
        return self.items == []


class CalculadoraMediaMovel:        # definindo a inicialização da 2a classe, recebendo o parâmetro k que será o tamanho da janela para o cálculo das médias.
    def __init__(self, k):         
        if k <= 0:                  # k precisa ser maior que zero, já evita esse erro.
            raise ValueError("O tamanho da janela (k) deve ser maior que zero.") 
        
        self.deque = Deque()      # armazena os elementos da janela deslizante.
        self.k = k                # atribuindo a janela K em self.k.
        self.soma_janela = 0      # armazena a soma dos elementos da janela deslizante.
        self.medias_moveis = []   # armazena as médias móveis calculadas.

    def adicionar_elemento(self, elemento):            #  adiciona um novo elemento à janela deslizante e calcula a média móvel correspondente.
        if self.deque.tamanho() == self.k:                   # Se a janela já estiver cheia (ou seja, se o deque tiver k elementos), removemos o elemento mais antigo da janela e atualizamos a soma da janela.
            self.soma_janela -= self.deque.remover_inicio()

        self.deque.adicionar_final(elemento)                # Adiciona o novo elemento à janela e atualizamos a soma da janela.
        self.soma_janela += elemento

        if self.deque.tamanho() == self.k:                  # Se a janela estiver cheia, calculamos a média móvel como a soma da janela dividida pelo tamanho da janela (k) e
            media = self.soma_janela / self.k                #  a adicionamos à lista de médias móveis. Caso contrário, adicionamos None à lista.
            self.medias_moveis.append(media)
        else:
            self.medias_moveis.append(None)

    def calcular_medias_moveis(self, dados_trafego):        # aqui recebe uma lista de dados de tráfego e calcula as médias móveis para cada elemento da lista.
        if not dados_trafego:                                 # como a lista não pode tá vazia, cria essa condição. 
            raise ValueError("Os dados de tráfego não podem ser vazios.")
        
        for elemento in dados_trafego:                    #  itera sobre cada elemento da lista de dados de tráfego e adiciona o elemento à janela deslizante e calcular a média móvel correspondente.
            self.adicionar_elemento(elemento)

    def obter_medias_moveis(self):                         # retorna a lista de médias móveis calculadas.
        return self.medias_moveis



dados_trafego = [120, 130, 150, 140, 160, 170, 180, 200, 190, 210]       #  dados do trafégo.
k = 3                                                                     # Tamanho da janela.

calculadora = CalculadoraMediaMovel(k)                                   # instância pra a calculadora com a janela k inserida.
calculadora.calcular_medias_moveis(dados_trafego)                        # cálculo da média 
medias_moveis = calculadora.obter_medias_moveis()                        # média calculada

print("Médias móveis calculadas:", medias_moveis)                        # print do cálculo
