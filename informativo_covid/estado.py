from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Estado:
    """Define objetos estado"""

    __nome: str
    __uf: str

    @property
    def nome(self) -> str:
        """Nome do estado"""
        return self.__nome

    @nome.setter
    def nome(self, novoNome) -> None:
        self.__nome = novoNome

    @property
    def uf(self) -> str:
        """UF do estado"""
        return self.__uf

    @uf.setter
    def uf(self, novoUf) -> None:
        self.__uf = novoUf
