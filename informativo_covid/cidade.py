from dataclasses import dataclass


@dataclass
class Cidade:
    """Define objetos cidade"""

    __nome: str
    __qtdeCasos: int = 0

    @property
    def nome(self) -> str:
        """Nome da cidade"""
        return self.__nome

    @nome.setter
    def nome(self, novoNome) -> None:
        self.__nome = novoNome

    @property
    def casos(self) -> int:
        """Quantidade de casos registrados"""
        return self.__qtdeCasos

    @casos.setter
    def atualizaCasos(self, novosCasos) -> None:
        """Atualiza quantidade de casos de uma cidade"""
        self.__qtdeCasos += novosCasos
