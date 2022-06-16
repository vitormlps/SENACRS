## IMPORTS ## ----------------------------------------------------------------
from Objetos import *


## MAIN ## ----------------------------------------------------------------
def menu():
    return input("""
1. Catalogar aluno
2. Consultar alunos por estado
3. Consultar alunos por curso
4. Localizar aluno por nome
5. Gerar arquivo txt com todos os alunos
0. Exit

Qual opção deseja selecionar? """)

# ----------------------------------------------------------------

def catalogarAluno():
    nomeAluno = input("\nQual o nome dx alunx que deseja cadastrar? (Digite não para retornar ao menu.) ").upper()

    if isNAO(nomeAluno):
        return

    cursoAluno = verificaInput('curso')
    estado = verificaInput('estado')

    if isNAO(cursoAluno) or isNAO(estado):
        return

    objAluno = Aluno(nomeAluno, cursoAluno)

    dict_estudantes.setdefault(estado, [])
    #setdefault testa se a chava já existe ou não. Se sim, ignora o segundo parametro; se não, cria uma nova chave com o primeiro parametro e valor com o segundo.
    
    dict_estudantes[estado].append(objAluno)
    
    catalogarAluno()

# ----------------------------------------------------------------

def alunoPorEstado():
    estado = verificaInput('estado')

    if isNAO(estado):
        return
    elif estado not in dict_estudantes:
        print("Estado não possui alunos registrados.")
    else:
        for aluno in dict_estudantes.get(estado):
            print(f"Aluno: {aluno.nome} | Curso: {aluno.curso}")
    
    alunoPorEstado()

# ----------------------------------------------------------------

def alunoPorCurso():
    count = 0
    cursoAluno = verificaInput('curso')

    if isNAO(cursoAluno):
        return

    for estado, alunos in dict_estudantes.items():
        for aluno in alunos:
            if aluno.curso == cursoAluno:
                count += 1
                print(f"Aluno: {aluno.nome} | Estado: {estado}")

    if count == 0:
        print("Curso não possui alunos registrados.")
    
    alunoPorCurso()

# ----------------------------------------------------------------

def alunoPorNome():
    count = 0
    nomeAluno = input("\nQual o nome dx alunx que deseja pesquisar? ").upper()

    if isNAO(nomeAluno):
        return

    for estado, alunos in dict_estudantes.items():
        for aluno in alunos:
            if aluno.nome == nomeAluno:
                count += 1
                print(f"Aluno: {aluno.nome} | Curso: {aluno.curso} | Estado: {estado}")
    
    if count == 0:
        print("Não há alunos registrados com este nome.")
    
    alunoPorNome()

# ----------------------------------------------------------------

def arquivoAlunos():
    arquivoTxt = open("Lista_Alunos.txt","w+")

    for estado, alunos in dict_estudantes.items():
        arquivoTxt.write(f"Estado: {estado}\n")
        arquivoTxt.seek(0) #atualiza a posição do ponteiro da string/arquivo

        if f"Estado: {estado}" in arquivoTxt.read():
                arquivoTxt.seek(arquivoTxt.tell())

        for aluno in alunos:
            seek = arquivoTxt.tell() #retorna a posição do ponteiro da string/arquivo
            if f"Curso: {aluno.curso}" not in arquivoTxt.read():
                arquivoTxt.write(" "*2 + f"Curso: {aluno.curso}\n")
                arquivoTxt.write(" "*4 + f"{aluno.nome}\n")
                arquivoTxt.seek(seek)
            else:
                arquivoTxt.write(" "*4 + f"{aluno.nome}\n")

    arquivoTxt.close()
    print("Arquivo criado com sucesso!")


## AUX ## ----------------------------------------------------------------
def isNAO (conteudo):
    if conteudo in "NAOÃUMÑPE":
        return True
    return False

# ----------------------------------------------------------------

def errorMSG ():
    print("Opção inválida. Digite novamente.")

# ----------------------------------------------------------------

def verificaInput (opcao):
    if opcao == 'curso':
        conteudo = input("""\nLista de cursos:
ADS | RDS | PMM | SPI

Qual o curso destx alunx de acordo com a lista acima? """).upper()

        if conteudo not in lst_cursos and not isNAO(conteudo):
            errorMSG()
            verificaInput (opcao = 'curso')


    elif opcao == 'estado':
        conteudo = input("""\nLista de estados:
RS | SC | SP | RJ | MG      

De acordo com a lista acima, qual o estado em que estx alunx está realizando o curso? """).upper()

        if conteudo not in lst_estados and not isNAO(conteudo):
            errorMSG()
            verificaInput (opcao = 'estado')

    return conteudo


## CHAMADAS ## ----------------------------------------------------------------
lst_estados = ["RS", "SC", "SP", "RJ", "MG"]
lst_cursos = ["ADS", "RDS", "PMM", "SPI"]

dict_estudantes = dict()

dict_opcoes = {
    1: catalogarAluno,
    2: alunoPorEstado,
    3: alunoPorCurso,
    4: alunoPorNome,
    5: arquivoAlunos}
