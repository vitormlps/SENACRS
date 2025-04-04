from desktop import Desktop
from notebook import Notebook

def main():
    pc = Desktop()
    note = Notebook()

    pc.cadastrar("Alien Ware", "Preto", 10000.0, "600w")
    print("PC cadastrado!")
    note.cadastrar("MacBook", "Branco", 25000.0, 21)
    print("Note cadastrado!")

    pcInfo = pc.getInformacoes()
    print(f"Este PC é um {pcInfo[0]} de cor {pcInfo[1]}. Custa R${pcInfo[2]} e tem potência de {pcInfo[3]}.")

    noteInfo = note.getInformacoes()
    print(f"Este note é um {noteInfo[0]} de cor {noteInfo[1]}. Custa R${noteInfo[2]} e a bateria dura {noteInfo[3]} horas.")

if "__main__" == __name__:
    main()