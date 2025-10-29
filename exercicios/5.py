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