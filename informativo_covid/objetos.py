# IMPORTS ## ----------------------------------------------------------------
from dataclasses import dataclass

# CLASSES ## ----------------------------------------------------------------
"""
Dataclass foi adicionado ao Python na versão 3.7 (PEP 557)

É um módulo que proporciona um decorador e funções pra gerar
automaticamente metodos especiais como __init__() e __repr__()
https://peps.python.org/pep-0557/#specification
"""

#frozen (emula objetos "read-only") e eq (compara a classe como se fosse uma tupla) tornam a dataclass hashable por virar imutável
#https://docs.python.org/3/library/dataclasses.html

@dataclass(frozen=True, eq=True)
class Estado():
    """Define objetos estado"""
    __nome: str
    __uf: str

    @property
    def nome(self) -> str:
        """Nome do estado"""
        return self.__nome

    @property
    def uf(self) -> str:
        """UF do estado"""
        return self.__uf


@dataclass
class Cidade():
    """Define objetos cidade"""
    __nome: str
    __qtCasos: int = 0

    @property
    def nome(self) -> str:
        """Nome da cidade"""
        return self.__nome

    @property
    def casos(self) -> int:
        """Quantidade de casos registrados"""
        return self.__qtCasos

    def atualizaCasos(self, novosCasos) -> None:
        """Atualiza quantidade de casos de uma cidade"""
        self.__qtCasos += novosCasos
