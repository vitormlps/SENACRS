## IMPORTS ## ----------------------------------------------------------------
from Main import *

## MAIN ## ----------------------------------------------------------------
def aplicacao():
    opcao = menu()

    if not opcao.isdigit() or int(opcao) >= 6:
        print("Opção inválida. Digite novamente.")
    else:
        opcao = int(opcao)
        if 1 <= opcao <= 5:
            dict_opcoes.get(opcao)()
        elif opcao == 0:
            return

    aplicacao()


## CHAMADAS ## ----------------------------------------------------------------
print("\nBem vindx ao catálogo de alunos!")
aplicacao()
