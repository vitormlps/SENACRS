## IMPORTS ## ----------------------------------------------------------------

## CHAMADAS ## ----------------------------------------------------------------
lst_estados = list()
lst_cidades = list()

## Classes ## ----------------------------------------------------------------

class Estados():
    def __init__(self, nome_estado, uf_estado):
        self.__nome_estado = nome_estado
        self.__uf_estado = uf_estado
        self.__cidades_estado = list()

    def get_nome(self):
        return self.__nome_estado

    def get_UF(self):
        return self.__uf_estado
    
    def get_relacao(self):
        return self.__cidades_estado
    
    def add_cidades_estado(self, cidade):
        self.__cidades_estado.append(cidade)

#----------------------------------------------------------------

class Cidades():
    def __init__(self, nome_cidade):
        self.__nome_cidade = nome_cidade
        self.__qt_casos = 0
    
    def get_nome(self):
        return self.__nome_cidade
    
    def get_casos(self):
        return self.__qt_casos

    def atualizarCasos(self, novosCasos):
        self.__qt_casos += novosCasos
