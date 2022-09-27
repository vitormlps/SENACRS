from cidade import Cidade
from estado import Estado
from funcionalidades import isChar, isNAO, isNum, enter


class Informativo:

    nVoltar = "('n' para voltar)"

    def __init__(self) -> None:
        self.__dictCovid: dict[Estado, list[Cidade]] = {}

    @property
    def dictCovid(self) -> dict[Estado, list[Cidade]]:
        """Get Informativo"""
        return self.__dictCovid

    @dictCovid.setter
    def dictCovid(self, arquivo: dict[Estado, list[Cidade]]) -> None:
        """Set Informativo"""
        self.__dictCovid = arquivo

    def cadastraEstados(self) -> None:
        """Gera objetos Estado com entradas de dados"""
        print("\nQual estado você gostaria de cadastrar?")
        estadoNome = isChar(
            input(f"Digite o nome do estado {self.nVoltar}: "), self.dictCovid
        )
        if isNAO(estadoNome):
            return

        estadoUF = isChar(
            input(f"Digite o nome da UF {self.nVoltar}: "), self.dictCovid
        )
        if isNAO(estadoUF):
            return

        self.dictCovid.setdefault(Estado(estadoNome, estadoUF), [])
        print("Estado cadastrado com sucesso!")

        return self.cadastraEstados()

    def cadastraCidades(self) -> None:
        """Gera objetos Cidade com entradas de dados"""

        self.printEstados()

        estadoNome = input(
            f"\nEm qual estado quer registrar cidades? {self.nVoltar}: "
        ).upper()

        if isNAO(estadoNome):
            return

        found = False
        for estado in self.dictCovid.keys():
            if estado.nome == estadoNome:
                found = True
                print("\nQual cidade você gostaria de cadastrar?")
                cidadeNome = isChar(
                    input(f"Digite o nome da cidade {self.nVoltar}: "), self.dictCovid
                )

                if isNAO(cidadeNome):
                    return

                self.dictCovid[estado].append(Cidade(cidadeNome))
                print("Cidade cadastrada com sucesso!")

        if found:
            print("Entrada não existe.")

        return self.cadastraCidades()

    def atualizaCasosEmCidades(self) -> None:
        """Entrega novo dado para atualizar o atributo 'qtCasos' de Cidades"""

        print("\nAVISO! O valor a ser inserido irá ACUMULAR ao atual.")
        self.printCidades()

        found = False
        cidadeNome = input(f"Digite o nome da cidade {self.nVoltar}: ").upper()

        if isNAO(cidadeNome):
            return

        for lstCidades in self.dictCovid.values():
            for cidade in lstCidades:
                if cidade.nome == cidadeNome:
                    found = True
                    print(f"Atualmente em {cidade.nome} há {cidade.casos} casos.")

                    cidade.atualizaCasos(isNum(input("Qual o valor a ser somado? ")))
                    print(f"Número de casos atualizado para {cidade.nome}.\n")
                    break

        if found:
            print("Entrada não existe.")

        return self.atualizaCasosEmCidades()

    def relataEstados(self) -> None:
        """Apresenta em tela os dados de Estados"""

        print("\nRelatório de Estados:")
        for estado, lstCidades in self.dictCovid.items():
            qtdTotalCasos = 0
            for cidade in lstCidades:
                qtdTotalCasos += cidade.casos

            print(f"{estado.nome} / {estado.uf} | Total de casos: {qtdTotalCasos}")

        enter()

    def relataCidades(self) -> None:
        """Apresenta em tela os dados de Cidades"""

        print("\nRelatório de Cidades:")

        for lstCidades in self.dictCovid.values():
            for cidade in lstCidades:
                print(f"{cidade.nome} | Casos registrados: {cidade.casos}")

        enter()

    def printEstados(self):
        print("Lista de estados:")
        for estado in self.dictCovid.keys():
            print(f"{estado.nome} / {estado.uf}")

    def printCidades(self):
        print("Lista de cidades:")
        for lstCidades in self.dictCovid.values():
            for cidade in lstCidades:
                print(cidade.nome)
