from computador import Computador

class Desktop(Computador):

    def __init__(self):
        super().__init__()
        self._potenciaDaFonte = ''
    
    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    @potenciaDaFonte.setter
    def potenciaDaFonte(self, novaPotencia):
        self._potenciaDaFonte = novaPotencia

    def getInformacoes(self):
        return self.modelo, self.cor, self.preco, self.potenciaDaFonte

    def cadastrar(self, novoModelo, novaCor, novoPreco, novaFonte):
        self.modelo = novoModelo
        self.cor = novaCor
        self.preco = novoPreco
        self.potenciaDaFonte = novaFonte