import os.path
from cidade import Cidade
from estado import Estado
from menu import progressBar


class ManipuladorTxt:
    """Manipula o arquivo 'dados.txt'"""

    def lerArquivoTxt(
        self, dictCovid: dict[Estado, list[Cidade]]
    ) -> dict[Estado, list[Cidade]]:
        """Le o arquivo caso exista"""

        if len(dictCovid) <= 0 and self.verificaArquivo():
            arquivo = open("dados.txt", "r")

            for linha in arquivo.readlines():
                if "Estado:" in linha:
                    estadoNome, estadoUf = (
                        linha.replace("Estado:" or " ", "").strip().split("/")
                    )
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
                if "Cidades:" not in arquivo.read():
                    arquivo.write(f"Cidades: {cidade.nome}, ")
                    arquivo.seek(seek)
                else:
                    arquivo.write(f"{cidade.nome}, ")
            arquivo.seek(arquivo.tell() - 2)
            arquivo.write("\n")

            for cidade in lstCidades:
                seek = arquivo.tell()
                if "Casos:" not in arquivo.read():
                    arquivo.write(f"Casos: {cidade.casos}, ")
                    arquivo.seek(seek)
                else:
                    arquivo.write(f"{cidade.casos}, ")
            arquivo.seek(arquivo.tell() - 2)
            arquivo.write("\n")
            arquivo.write("---\n")

        arquivo.close()
        print(" Arquivo salvo!")

    def verificaArquivo(self) -> bool:
        print("Verificando se existe Informativo salvo... ")
        progressBar()

        if os.path.exists("dados.txt"):
            return True
        print(
            "\nNão existe Informativo salvo! Um arquivo com as entradas atuais será gerado após termino do programa."
        )
        return False
