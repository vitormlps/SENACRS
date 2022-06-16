## IMPORTS ## ----------------------------------------------------------------

## PRINTS ## ----------------------------------------------------------------
class Print():
    def bemVindo():
        print("\nBem vindx ao informativo brasileiro de COVID-19!")

    def menu():
        print("""
        1- Cadastrar Estados
        2- Cadastrar Cidades
        3- Relacionar Estado com Cidade
        4- Relatório de Estados
        5- Relatório de Cidades
        6- Atualizar números de casos nas Cidades
        0- Finalizar o Programa
        """)

    def avisos(opcao):
        if opcao == "erro":
            print("Erro! Por favor digite novamente.")
        elif opcao == "erroUF":
            print("UF não pode ter mais de 2 letras. Por favor digite novamente.")
        elif opcao == "fim":
            print("Obrigado por utilizar o informativo. Até mais!")
        elif opcao == "duplicado":
            print("Por favor não insira informações duplicadas!")
        elif opcao == "acumulo":
            print("\nAVISO! O valor a ser inserido irá ACUMULAR ao atual.")
        elif opcao == "!lista":
            print("\nA Cidade ou Estado não foi inserido no sistema.")
        elif opcao == "negativo":
            print("A quantidade não pode ser negativa.")
        elif opcao == "!estado":
            print("Estado não encontrado.")

    def frases(opcao):
        if opcao == "estado":
            print("\nQuais estados você gostaria de cadastrar?")
        elif opcao == "cidade":
            print("\nQuais cidades você gostaria de cadastrar?")
        elif opcao == "relacao":
            print("Quais cidades gostaria de relacionar a qual estado?\n")
        elif opcao == "enter":
            input("Aperte ENTER para retornar ao menu.")


## INPUTS ## ----------------------------------------------------------------        
class Input():
    def opcaoMenu():
        opcao = input("Qual opção você deseja? ")
        return opcao
    
    def inputEstado():
        nome = input("Digite o nome do estado(digite 'n' para voltar ao menu principal): ").upper()
        return nome
    
    def inputUF():
        uf = input("Digite a UF: ").upper()
        return uf
    
    def inputCidade():
        nome = input("Digite o nome da cidade(digite 'n' para voltar ao menu principal): ").upper()
        return nome
    
    def inputRelacao():
        numeros = input("\nQuais cidades deseja relacionar? Digite as posições (números) das cidades, separadas por vírgula: ")
        return numeros