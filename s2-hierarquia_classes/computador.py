from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):
    def __init__(self):
        self._modelo = ''
        self._cor = ''
        self._preco = 0
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, novoModelo):
        self._modelo = novoModelo
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, novaCor):
        self._cor = novaCor
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novoPreco):
        self._preco = novoPreco

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco

    @abstractmethod
    def cadastrar(self):
        pass
