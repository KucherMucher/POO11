import matematica as mat
import textos as txt

def doubleIntInput(text):
    return map(int, input(text).split())

inpt = 'c'
running = True
while running:
    if inpt == 'c':
        print("\n1--------------------1") # 20
        print("1-Escolhe o módulo:--1")
        print("1-(a)-matematica.py--1")
        print("1-(b)-textos---------1")
        print("1-(s)-sair-----------1")
        print("1--------------------1")
        inpt = input("")
    elif inpt == 'a':
        print("\n1--------------------1") # 20
        print("1-Escolhe a função:--1")
        print("1-(1)-soma-----------1")
        print("1-(2)-subtração------1")
        print("1-(3)-é_primo?-------1")
        print("1-(4)-sair-----------1")
        print("1--------------------1")
        inpt2 = int(input(""))
        match inpt2:
            case 1:
                a, b = doubleIntInput("Insira dois números (com espaço): ")
                print(f"A soma dos números é {mat.soma(a, b)}")
            case 2:
                a, b = doubleIntInput("Insira dois números (com espaço): ")
                print(f"A subtração dos números é {mat.subtracao(a, b)}")
            case 3:
                a = int(input("Insira qualquer número natural: "))
                print("O número é primo") if mat.eh_primo(a) else print("O número não é primo")
            case 4:
                inpt = 'c'
    elif inpt == 'b':
        print("\n1--------------------1") # 20
        print("1-Escolhe a função:--1")
        print("1-(1)-inverso--------1")
        print("1-(2)-capitalizar----1")
        print("1-(3)-decapitalizar--1")
        print("1-(4)-sair-----------1")
        print("1--------------------1")
        inpt2 = int(input(""))
        match inpt2:
            case 1:
                string = input("Insira uma palavra: ")
                print(f"O inverso da palavra é {txt.inverso(string)}")
            case 2:
                string = input("Insira uma palavra: ")
                print(f"A capitalização da palavra é {txt.capitalizar(string)}")
            case 3:
                string = input("Insira uma palavra: ")
                print(f"A decapitalização da palavra é {txt.decapitalizar(string)}")
            case 4:
                inpt = 'c'
    elif inpt == 's':
        running = False
print("Obrigado por usar a programa.")