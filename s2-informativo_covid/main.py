# IMPORTS ## ----------------------------------------------------------------
import sys
from informativo import *

"""
Type hints foi adicionado ao Python na versão 3.5 (PEP 484)

Adiciona semântica a annotations
https://peps.python.org/pep-0484/
"""

# MAIN ## ----------------------------------------------------------------
def main() -> None:
    """Inicializador"""

    info = Informativo()
    editor = ManipuladorTxt()
    dictOpcoes = {1: info.cadastraEstados,
                2: info.cadastraCidades,
                3: info.relataEstados,
                4: info.relataCidades,
                5: info.atualizaCasosEmCidades}

    info.setDictCovid(editor.lerArquivoTxt(info.dictCovid))

    while True:
        printMenu()
        opcao = isNum(input("Qual opção deseja? "))
        if opcao >= 6:
            print("Opção inválida. Digite novamente.")

        elif 1 <= opcao <= 5:
            if 2 <= opcao <= 5 and (len(info.dictCovid) <= 0):
                print("Ainda não existem Estados no Informativo.")
            else:
                dictOpcoes[opcao]()

        else:
            editor.gravarArquivoTxt(info.dictCovid)
            print("Hasta la vista, baby.\n")
            sys.exit()


# RUN ## ----------------------------------------------------------------
if __name__ == '__main__':
    print("""
######################################################
## Bem vindx ao informativo brasileiro de COVID-19! ##
######################################################
    """)
    main()
