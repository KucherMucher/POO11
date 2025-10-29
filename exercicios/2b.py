import math

#e de escolha
e = int(input("Exercício: ")) 

match e:
    case 1:
        print("\nexercicio1\n")

        try:
            raio=float(input("Introduza o raio do círculo: "))
            print(f"A área do círculo é: {round(((math.pi)*raio**2), 1)}") #considero que desta maneira é mais fixe
        except Exception:
            print("Não foi introduzido um número!!!")

    case 2:
        print("\nexercicio2\n")

        try:
            celcius=float(input("Introduza a temperatura em Celsius: "))
            print(f"A temperatura em Fahrenheit é: {round((celcius*(9/5)+32), 1)}")
        except Exception:
            print("Não foi introduzido um número!!!")

    case 3:
        print("\nexercicio3\n")

        try:
            nota1=float(input("Introduza a primeira nota: "))
            nota2=float(input("Introduza a segunda nota: "))
            nota3=float(input("Introduza a terceira nota: "))

            print(f"A média das notas é: {round((nota1+nota2+nota3)/3, 2)}")
        except Exception:
            print("Não foi introduzido um número!!!")
    case 4:
        print("\nexercicio4\n")

        try:
            largura=float(input("Introduza a largura do retângulo: "))
            altura=float(input("Introduza a altura do retângulo: "))
            print(f"O perímetro é: {(largura*2)+(altura*2)} u.")
            print(f"A área é: {largura*altura} u.a.")

        except Exception:
            print("Não foi introduzido um número!!!")

        
    case 5:
        print("\nexercicio5\n")

        try:
            hora=int(input("Introduza as horas: "))
            minuto=int(input("Introduza os minutos: "))
            segundo=int(input("Introduza os segundos: "))

            print(f"O tempo total em segundos é: {((hora*60)+minuto)*60+segundo}")
        except Exception:
            print("Não foi introduzido um número!!!")