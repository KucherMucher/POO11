ex=int(input("Escolhe o exercício: "))

match ex:
    case 1:
        for i in range(1,11):
            print(i)

    case 2:
        n=int(input("Introduz um número: "))

        for i in range(1,51):
            if i%n==0:
                print(i)

    case 3:
        soma = 0
        for i in range(1, 101):
            soma+=i

        print(soma)

    case 4:
        list = [3, 6, 9, 36, 69, 369] #6 números
        soma = 0
        for i in list:
            soma+=i

        print(soma)

    case 5:
        idades = [15, 17, 18, 19, 14, 16, 20, 18]
        n = 0

        for i in idades:
            if i >= 18:
                n+=1

        print(n)

    case 6:
        string = input("Insira uma palavra: ")
        n=0

        for i in string:
            if i.lower() == 'a':
                n+=1

        state = "letra" if n == 1 else "letras"
        print(f"A palavra {string} inclui {n} {state} de 'a'")

    case 7:
        n = int(input("Insira uma número para tabuada: "))
        print(f"Entrada -> {n}")
        print("Saída ->")

        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")

    case 8:
        for i in range(1, 11):
            print(f"{i} -> {i**2}")