## IMPORTS ## ----------------------------------------------------------------

## CLASSES ## ----------------------------------------------------------------
class Aluno:
    def __init__(self, nome, curso):
        self.__nome = nome
        self.__curso = curso

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
    def getCurso(self):
        return self.__curso

    def setCurso(self, curso):
        self.__curso = curso

    nome = property(getNome, setNome)
    curso = property(getCurso, setCurso)