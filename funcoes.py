## IMPORTS ## ----------------------------------------------------------------
from objetos import *
from interface import *

## MAIN ## ----------------------------------------------------------------
def cadastrarEstados():
    Print.frases("estado") #"Quais estados (...)"

    while True:
        estadoNome = Input.inputEstado() #"Digite o nome do estado (...)"

        if verificarString(estadoNome):
            if verificarNAO(estadoNome):
                break #volta para a Aplicação
            elif verificarDuplicado(estadoNome, lst_estados):
                Print.avisos("duplicado")
            else:
                estadoUF = Input.inputUF() #"Digite a UF"
                if verificarString(estadoUF):
                    if len(estadoUF) != 2:
                        Print.avisos("erroUF")
                    elif verificarDuplicado(estadoUF, lst_estados):
                        Print.avisos("duplicado")
                    else:
                        estado = Estados(estadoNome, estadoUF) #se estiver tudo certo, cria objeto estado
                        lst_estados.append(estado) #add estado a lista de estados
                else:
                    Print.avisos("erro")
        else:
            Print.avisos("erro")

#----------------------------------------------------------------

def cadastrarCidades():
    Print.frases("cidade") #"Quais cidades (...)"

    while True:
        cidadeNome = Input.inputCidade() #"Digite o nome da cidade (...)"

        if verificarNAO(cidadeNome):
            break #volta para a Aplicação
        elif verificarDuplicado(cidadeNome, lst_cidades):
            Print.avisos("duplicado")

        elif verificarString(cidadeNome):
            cidade = Cidades(cidadeNome)
            lst_cidades.append(cidade)
        else:
            Print.avisos("erro")

#----------------------------------------------------------------

def relacionarEstadosECidades():
    lst_relacao = list()

    Print.frases("relacao")

    print("Lista de estados:")
    for num in range(len(lst_estados)):
        print(f"{num} - {lst_estados[num].get_nome()}")

    print("\nLista de cidades:")
    for num in range(len(lst_cidades)):
        print(f"{num} - {lst_cidades[num].get_nome()}") #condiciona o user a digitar o que eu quero
    
    while True:
        relacaoEstado = Input.inputEstado()

        if verificarNAO(relacaoEstado):
            break #volta para a Aplicação

        for estado in lst_estados:
            if relacaoEstado == estado.get_nome():
                relacaoPosicao = Input.inputRelacao() #vai digitar "0,1,2,3,4,n"
                lst_relacao = verificarRelacao(relacaoPosicao, lst_relacao) #retorna uma lista com as posições das cidades na lst_cidades

                for posicao in lst_relacao:
                    estado.add_cidades_estado(lst_cidades[posicao])
                
                print(f"Cidades relacionadas ao estado {relacaoEstado}.\n")

                #for i in range(len(estado.get_relacao())):
                #    print(estado.get_relacao(i))

                break #volta para o while
            elif relacaoEstado not in lst_estados:
                Print.avisos("!estado")

#----------------------------------------------------------------

def relatorioEstados():
    print("Relatório de Estados:")
    
    qtdTotalCasos = 0

    for estado in lst_estados:
        for cidade in estado.get_relacao():
            qtdTotalCasos += cidade.get_casos()
        
        print(f"{estado.get_nome()} / {estado.get_UF()} | Total de casos: {qtdTotalCasos}")
    
    Print.frases("enter")

#----------------------------------------------------------------

def relatorioCidades():
    print("Relatório de Cidades:")
    
    for cidade in lst_cidades:
        print(f"{cidade.get_nome()} | Casos registrados: {cidade.get_casos()}")
    
    Print.frases("enter")

#----------------------------------------------------------------

def atualizarCasos():
    count = 0
    Print.avisos("acumulo")

    print("\nLista de cidades:")
    for num in range(len(lst_cidades)):
        print(f"{num} - {lst_cidades[num].get_nome()}")

    while True:
        cidadeNome = Input.inputCidade() #"Digite cidade (...)"

        if verificarNAO(cidadeNome):
            break #volta para a aplicação

        for cidade in lst_cidades:
            if cidade.get_nome() == cidadeNome:
                print(f"Atualmente em {cidade.get_nome()} há {cidade.get_casos()} casos.")
                while True:
                    casos = input("Qual o valor a ser somado? ")

                    if verificarNumero(casos):
                        cidade.atualizarCasos(int(casos))
                        print(f"Número de casos atualizado para {cidade.get_nome()}.\n")
                        break
                    else:
                        Print.avisos("erro")
            else:
                count+=1
                if count >= len(lst_cidades):
                    Print.avisos("!lista")      

## VERIFICAÇÕES ## ----------------------------------------------------------------
def verificarDuplicado(variavel, conteudo):
    for var in conteudo:
        if var == variavel: #verificação geral (principalmente objetos)
            return True
        elif variavel.isalpha() and var.get_nome() == variavel: #verificação para nomes de cidades e estados
            return True
        elif hasattr(var, "get_UF"): #metodo "hasattr" para verificar se objeto tem atributo
            if len(variavel) == 2 and var.get_UF() == variavel: #verificação para UFs
                return True

def verificarRelacao(posicao, lst_relacao):
    count = 0
    posicao = posicao.replace(" ","") #retirar espaços em branco
    lst_posicoes = posicao.split(",") #quebra o conteúdo separado por virgula em uma lista
    for var in lst_posicoes:
        if var.isdigit(): #verifica se é número
            lst_relacao.append(int(var))
        else:
            count+=1
            if count >= len(lst_posicoes):
                Print.avisos("erro")
    return lst_relacao

def verificarNumero(var): #verifica se a frase é numero e se é maior que zero
    if var.isdigit() == False:
        Print.avisos("erro")
    elif int(var) < 0:
        Print.avisos("negativo")
    else:
        return True

def verificarString(var): #verifica se a frase só tem letras | replace para retirar espaços no momento da verificação
    if var.replace(" ","").isalpha():
        return True

def verificarNAO(var):
    if var.strip() in ('N','NAO','NÃO'):
        return True
        