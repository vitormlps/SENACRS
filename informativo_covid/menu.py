from time import sleep


def printMenu() -> None:
    print(
        """
MENU
1- Cadastrar Estados
2- Cadastrar Cidades
3- Relatório de Estados
4- Relatório de Cidades
5- Atualizar números de casos nas Cidades
0- Finalizar o Programa
   """
    )


def progressBar() -> None:
    progresso = "#"
    for num in range(11):
        progresso += "#" * num
        print(f"\r{progresso}", end="")
        sleep(0.05)
