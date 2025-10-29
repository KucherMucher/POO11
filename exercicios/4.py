ex=int(input("Escolhe o exercício: "))

match ex:
    case 1:
        n=int(input("Introduza um número: "))
        i=1
        while i<=n:
            print(i)
            i=i+1

    case 2:
        palavra=input("Introduza uma palavra: ")
        n=int(input("introduza um número: "))

        i=1
        while i<=n:
            print(palavra)
            i=i+1


    case 3:
        print("introduzir números até escrever 0")

        soma=0
        while True:
            n=int(input("Introduza um número: "))
            soma=soma+n
            if n==0:
                break

        print(f"A soma é {soma}")

    case 4:
        import random
        i=random.randint(1,10)
        print("Advinha um número! (1-10)")
        while True:
            n=int(input("Número: "))
            if n==i:
                break
            else:
                print("Errado. Tenta outravez")
        print(f"Acertaste! O número é {i}")

    case 5:
        senha="python123"
        while True:
            st=input("Introduza a senha: ")
            if st==senha:
                print("Acesso Permitido")
                break
            else:
                print("senha incorreta")
            

    case 6:
        soma = 0
        i = 0
        while True:
            n=int(input("Introduza uma nota: "))
            if n == -1:
                break
            else:
                soma=soma+n
                i=i+1
        print(f"A média é {round(soma/i, 1)}")