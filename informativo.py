# IMPORTS ## ----------------------------------------------------------------
from time import sleep
import os.path
from objetos import Estado, Cidade

# MAIN ## ----------------------------------------------------------------
class Informativo:
   def __init__(self) -> None:
      self.__dictCovid: dict[Estado, list[Cidade]] = {}


   @property
   def dictCovid(self) -> dict[Estado, list[Cidade]]:
      """Get Informativo"""
      return self.__dictCovid


   def setDictCovid(self, arquivo: dict[Estado, list[Cidade]]) -> None:
      """Set Informativo"""
      self.__dictCovid = arquivo


   def cadastraEstados(self) -> None:
      """Gera objetos Estado com entradas de dados"""
      print("\nQual estado você gostaria de cadastrar?")
      estadoNome = isChar(input("Digite o nome do estado('n' para voltar): "), self.dictCovid)
      if isNAO(estadoNome):
         return

      estadoUF = isChar(input("Digite o nome da UF('n' para voltar): "), self.dictCovid)
      if isNAO(estadoUF):
         return

      estado = Estado(estadoNome, estadoUF)
      self.dictCovid.setdefault(estado, [])
      print("Estado cadastrado com sucesso!")

      return self.cadastraEstados()


   def cadastraCidades(self) -> None:
      """Gera objetos Cidade com entradas de dados"""

      print("Lista de estados:")
      for estado in self.dictCovid.keys():
         print(f"{estado.nome} / {estado.uf}")
      
      estadoNome = input("\nEm qual estado quer registrar cidades?('n' para voltar): ").upper()
      if isNAO(estadoNome):
         return

      count = 0
      for estado in self.dictCovid.keys():
         if estado.nome == estadoNome:
            count += 1
            print("\nQual cidade você gostaria de cadastrar?")
            cidadeNome = isChar(input("Digite o nome da cidade('n' para voltar): "), self.dictCovid)
            if isNAO(cidadeNome):
                  return

            cidade = Cidade(cidadeNome)
            self.dictCovid[estado].append(cidade)
            print("Cidade cadastrada com sucesso!")

      if count == 0:
         print("Entrada não existe.")

      return self.cadastraCidades()


   def atualizaCasosEmCidades(self) -> None:
      """Entrega novo dado para atualizar o atributo 'qtCasos' de Cidades"""

      print("\nAVISO! O valor a ser inserido irá ACUMULAR ao atual.\nLista de cidades:")
      for lstCidades in self.dictCovid.values():
         for cidade in lstCidades:
            print(cidade.nome)

      count = 0
      cidadeNome = input("Digite o nome da cidade('n' para voltar): ").upper()
      if isNAO(cidadeNome):
         return

      for lstCidades in self.dictCovid.values():
         for cidade in lstCidades:
            if cidade.nome == cidadeNome:
               count += 1
               print(f"Atualmente em {cidade.nome} há {cidade.casos} casos.")
               cidade.atualizaCasos(isNum(input("Qual o valor a ser somado? ")))
               print(f"Número de casos atualizado para {cidade.nome}.\n")
               break

      if count == 0:
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

      input("ENTER para retornar ao menu.")


   def relataCidades(self) -> None:
      """Apresenta em tela os dados de Cidades"""

      print("\nRelatório de Cidades:")

      for lstCidades in self.dictCovid.values():
         for cidade in lstCidades:
            print(f"{cidade.nome} | Casos registrados: {cidade.casos}")

      input("ENTER para retornar ao menu.")


# MANIPULACAO DE ARQUIVO ## ----------------------------------------------------------------
class ManipuladorTxt:
   """Manipula o arquivo 'dados.txt'"""

   def lerArquivoTxt(self, dictCovid: dict[Estado, list[Cidade]]) -> dict[Estado, list[Cidade]]:
      """Le o arquivo caso exista"""

      if len(dictCovid) <= 0 and self.verificaArquivo(): #Executar no terminal não escontra o arquivo devido a permissão de acesso, mas no interactive window sim.
         arquivo = open("dados.txt", "r")

         for linha in arquivo.readlines():
               if "Estado:" in linha:
                  estadoNome, estadoUf = (linha.replace("Estado:" or " ", "").strip().split("/"))
                  estado = Estado(estadoNome, estadoUf)
                  dictCovid.setdefault(estado, [])

               elif "Cidades:" in linha:
                  cidades = linha.replace("Cidades:" or " ", "").split(",")
                  for cidadeNome in cidades:
                     cidade = Cidade(cidadeNome.strip())
                     dictCovid[estado].append(cidade)

               elif "Casos:" in linha:
                  lstCasos = linha.replace("Casos:" or " ", "").strip().split(",")
                  for num, cidade in enumerate(dictCovid[estado]):
                     cidade.atualizaCasos(int(lstCasos[num]))

         arquivo.close()
         print("\nDados do arquivo inseridos no sistema!")
         return dictCovid
      return dictCovid


   def gravarArquivoTxt(self, dictCovid: dict[Estado, list[Cidade]]) -> None:
      """Escreve no arquivo e cria um caso não exista"""

      arquivo = open("dados.txt", "w+")
      print("Gravando novo Informativo...")
      progressBar()

      for estado, lstCidades in dictCovid.items():
         arquivo.write(f"Estado: {estado.nome}/{estado.uf}\n")
         arquivo.seek(0)

         if f"/{estado.uf}" in arquivo.read():
               arquivo.seek(arquivo.tell())

         for cidade in lstCidades:
               seek = arquivo.tell()
               if f"Cidades:" not in arquivo.read():
                  arquivo.write(f"Cidades: {cidade.nome}, ")
                  arquivo.seek(seek)
               else:
                  arquivo.write(f"{cidade.nome}, ")
         arquivo.seek(arquivo.tell()-2)
         arquivo.write("\n")

         for cidade in lstCidades:
               seek = arquivo.tell()
               if f"Casos:" not in arquivo.read():
                  arquivo.write(f"Casos: {cidade.casos}, ")
                  arquivo.seek(seek)
               else:
                  arquivo.write(f"{cidade.casos}, ")
         arquivo.seek(arquivo.tell()-2)
         arquivo.write("\n")
         arquivo.write("---\n")

      arquivo.close()
      print(" Arquivo salvo!")


   def verificaArquivo(self) -> bool:
      print("Verificando se existe Informativo salvo... ")
      progressBar()
      
      if os.path.exists('dados.txt'): #Coloquei o os.path.exists() como condição pra não quebrar a execução ao tentar abrir um arquivo inexistente ou não encontrado.
         return True
      else:
         print("\nNão existe Informativo salvo! Um arquivo com as entradas atuais será gerado após termino do programa.")
         return False


# MENU ## ----------------------------------------------------------------
def printMenu() -> None:
   print("""
MENU
1- Cadastrar Estados
2- Cadastrar Cidades
3- Relatório de Estados
4- Relatório de Cidades
5- Atualizar números de casos nas Cidades
0- Finalizar o Programa
   """)


def progressBar() -> None:
   progresso = "#"
   for num in range(11):
      progresso += "#"*num
      print(f"\r{progresso}", end="")
      sleep(0.05)


# AUX ## ----------------------------------------------------------------
def isChar(entrada: str, dictCovid) -> str:
   entrada = entrada.upper()
   if entrada.replace(" ", "").isalpha():
      if len(entrada) == 2:
         if not duplicado(entrada, dictCovid):
            return entrada
         else:
            new = novaEntrada()
            return isChar(new, dictCovid)

      if not duplicado(entrada, dictCovid):
         return entrada
      else:
         new = novaEntrada()
         return isChar(new, dictCovid)
   else:
      print("nova entrada")
      new = novaEntrada()
      return isChar(new, dictCovid)


def isNum(entrada: str) -> int:
   if entrada.isdigit() and int(entrada) >= 0:
      return int(entrada)
   else:
      new = novaEntrada()
      return isNum(new)


def isNAO(entrada: str) -> bool:
   if entrada in "NAOÃUMÑPE":
      return True


def duplicado(entrada: str, dictCovid: dict[Estado, list[Cidade]]) -> bool:
   for estado, lstCidades in dictCovid.items():
      if entrada == estado.nome or entrada == estado.uf:
         return True
      for cidade in lstCidades:
         if entrada == cidade.nome:
               return True
   return False


def novaEntrada() -> str:
   print("Entrada inválida.")
   return input("Digite novamente: ")
