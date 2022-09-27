from cidade import Cidade
from estado import Estado


def enter():
    input("ENTER para retornar ao menu.")


def isChar(entrada: str, dictCovid) -> str:
    entrada = entrada.upper()
    if entrada.replace(" ", "").isalpha() or len(entrada) == 2:
        return (
            entrada
            if not duplicado(entrada, dictCovid)
            else isChar(escreverNovaEntrada(), dictCovid)
        )

    return isChar(escreverNovaEntrada(), dictCovid)


def isNum(entrada: str) -> int:
    return (
        int(entrada)
        if entrada.isdigit() and int(entrada) >= 0
        else isNum(escreverNovaEntrada())
    )


def isNAO(entrada: str) -> bool:
    return True if entrada in "NAOÃUMÑPE" else False


def duplicado(entrada: str, dictCovid: dict[Estado, list[Cidade]]) -> bool:
    for estado, lstCidades in dictCovid.items():
        if entrada == estado.nome or entrada == estado.uf:
            return True
        for cidade in lstCidades:
            if entrada == cidade.nome:
                return True
    return False


def escreverNovaEntrada() -> str:
    print("Entrada inválida.")
    return input("Digite novamente: ")
