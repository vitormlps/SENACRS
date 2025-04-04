from computador import Computador

class Notebook(Computador):

    def __init__(self):
        super().__init__()
        self.__tempoDeBateria = 0

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self, novaBateria):
        self.__tempoDeBateria = novaBateria
    
    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self.tempoDeBateria

    def cadastrar(self, novoModelo, novaCor, novoPreco, novaBateria):
        self.modelo = novoModelo
        self.cor = novaCor
        self.preco = novoPreco
        self.tempoDeBateria = novaBateria