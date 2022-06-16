## IMPORTS ## ----------------------------------------------------------------
from interface import *
from funcoes import * #cadastrarEstados, cadastrarCidades, relacionarEstadosECidades, relatorioEstados, relatorioCidades, atualizarCasos

## MAIN ## ----------------------------------------------------------------
class Aplicacao():
    Print.bemVindo() #"Bem vindx (...)""
    
    while True:
        Print.menu() #"1- Cadastrar Estados (...)""
        
        opcao = Input.opcaoMenu() #"Qual opção você deseja?"

        if opcao == "1":
            cadastrarEstados()
        
        elif opcao == "2":
            cadastrarCidades()
        
        elif opcao == "3":
            relacionarEstadosECidades()
        
        elif opcao == "4":
            relatorioEstados()
        
        elif opcao == "5":
            relatorioCidades()
        
        elif opcao == "6":
            atualizarCasos()
        
        elif opcao == "0":
            Print.avisos("fim")
            break
        
        else:
            Print.avisos("erro")

## CHAMADAS ## ----------------------------------------------------------------
Aplicacao()
input()