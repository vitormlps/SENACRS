import sys
from informativo import Informativo
from manipulador_txt import ManipuladorTxt
from menu import printMenu
from funcionalidades import isNum


def main() -> None:
    """Inicializador"""

    info = Informativo()
    editor = ManipuladorTxt()
    dictOpcoes = {
        1: info.cadastraEstados,
        2: info.cadastraCidades,
        3: info.relataEstados,
        4: info.relataCidades,
        5: info.atualizaCasosEmCidades,
    }

    info.dictCovid = editor.lerArquivoTxt(info.dictCovid)

    while True:
        printMenu()
        opcao = isNum(input("Qual opção deseja? "))

        if opcao >= 6:
            print("Opção inválida. Digite novamente.")

        elif 1 <= opcao <= 5:
            print("Ainda não existem Estados no Informativo.") if 2 <= opcao <= 5 and (
                len(info.dictCovid) <= 0
            ) else dictOpcoes[opcao]()

        else:
            editor.gravarArquivoTxt(info.dictCovid)
            print("Hasta la vista, baby.\n")
            sys.exit()


if __name__ == "__main__":
    print(
        """
######################################################
## Bem vindx ao informativo brasileiro de COVID-19! ##
######################################################
    """
    )
    main()
