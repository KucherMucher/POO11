def NegNCheck(x): #erro se o número é negativo
    if x<0: raise Exception

exercicio = int(input("Escolhe o exercicio: "))

match exercicio:
    case 1:
        while True:
            try:
                n = int(input("Introduza um número inteiro: "))
                if n%2==0:
                    print(f"O número {n} é par")
                else:
                    print(f"O número {n} é ímpar")
                
                break
            except Exception:
                print("Não era introduzido um número inteiro. Try Again.")

    case 2:
        while True:
            try:
                n1=int(input("Introduza o primeiro número: "))
                n2=int(input("Introudza o segundo número: "))

                if n1>n2:
                    print("O primeiro número é maior que o segundo.")
                elif n1<n2:
                    print("O segundo número é maior que o primeiro.")
                else:
                    print("Os dois números são iguais")
                
                break
            except Exception:
                print("Não era introduzido um número inteiro. Try Again.")

    case 3:
        while True:
            try:
                n=int(input("Introduza a nota do aluno: "))
                NegNCheck(n)

                if n>=10: print("O aluno está aprovado")
                else: print("O aluno está reprovado")

                break
            except Exception:
                print("Não era introduzido um valor numérico ou foi introduzido um número negativo Try Again.")

    case 4:
        while True:
            try:
                id=int(input("Introduza a sua idade: "))
                NegNCheck(id)

                if 0<=id<=12:
                    print("Vocé é uma criança")
                elif 13<=id<=17:
                    print("Vocé é um adolescente")
                elif 18<=id<=64:
                    print("Vocé é um adulto")
                else:
                    print("Vocé é um sénior")
                
                break
            except Exception:
                print("Não era introduzido um valor numérico ou foi introduzido um número negativo Try Again.")
    
    case 5:
        while True:
            try:
                
                l1=float(input("Introduza o comprimento do primeiro lado: "))
                NegNCheck(l1)
                l2=float(input("Introduza o comprimento do segundo lado: "))
                NegNCheck(l2)
                l3=float(input("Introduza o comprimento do trceiro lado lado: "))
                NegNCheck(l3)

                if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
                    print("Os comprimentos formam um triângulo válido")
                else:
                    print("Os comprimentos não formam um triângulo válido")

                break
            except Exception:
                print("Não era introduzido um valor numérico ou foi introduzido um número negativo Try Again.")

    case 6:
        while True:
            try:
                ano=int(input("Introduza um ano: "))
                NegNCheck(ano)

                if (ano%4==0 and ano%100!=0) or ano%400==0: print(f"O ano {ano} é bissexto")
                else: print(f"O ano {ano} não é bissexto")
                break
            except Exception:
                print("Não era introduzido um número inteiro ou o número é negativo. Try Again.")

    case 7:
        while True:
            try:
                #peso/altura2
                peso=float(input("Introduza o seu peso (kg): "))
                NegNCheck(peso)
                altura=float(input("Introduza a sua altura (m): "))
                NegNCheck(altura)
                print("Fórmula de IMC = peso/altura^2")

                imc=peso/(altura**2)
                print(f"O seu IMC é: {round(imc,1)}")

                if imc<18.5:
                    print("Classificação: Abaixo do peso")
                elif 18.5<=imc<25:
                    print("Classificação: Peso Normal")
                elif 25<=imc<30:
                    print("Classificação: Sobrepeso")
                else:
                    print("Classificação: Obesidade")
                
                break
            except Exception:
                print("Não era introduzido um valor numérico ou o número é negativo. Try Again.")
        
    case 8:
        while True:
            try:
                n1=int(input("Introduza o primeiro número: "))
                n2=int(input("Introduza o segundo número: "))

                if n1>=0 and n2>=0:
                    print("Ambos os números são positivos.")
                elif n1<0 and n2<0:
                    print("Ambos os números são negativos.")
                else:
                    print("Pelo menos um dos números é positivo.")
                break
            except Exception:
                print("Não era introduzido um número inteiro. Try Again.")

    case 9:
        import math
        #fórmula = (-b+-root(b^2-4ac))/2a
        #precisamos b^2-4ac
        while True:
            try:
                a=float(input("Introduza o coeficiente a: "))
                b=float(input("Introduza o coeficiente b: "))
                c=float(input("Introduza o coeficiente c: "))

                if math.sqrt((b**2)-(4*a*c))<0: print("A função não intersseta a ordenada do 0 (y=0)")
                elif math.sqrt((b**2)-(4*a*c))==0:
                    print("A função intersseta a ordenada do 0 (y=0) uma vez,")
                    x=-(b)/(2*a)
                    print(f"com x={x}")
                else:
                    print("A função intersseta a ordenada do 0 (y=0) duas vezes,")
                    x1=(-(b)+math.sqrt(b**2-(4*a*c)))/2*a
                    x2=(-(b)-math.sqrt(b**2-(4*a*c)))/2*a
                    print(f"com x={round(x1,1)} e x={round(x2,1)}")
                
                break
            except Exception:
                print("Não era introduzido um número inteiro. Try Again.")

    case 10:
        while True:
            try:
                nota=float(input("Introduza a nota do aluno: "))
                NegNCheck(nota)

                if nota>=18:
                    print("Conceito: Aprovado com Distinção")
                elif 16<=nota<18:
                    print("Conceito: Muito Bom")
                elif 14 <= nota < 16:
                    print("Conceito: Bom")
                elif 10 <= nota < 14:
                    print("Conceito: Suficiente")
                elif nota < 10:
                    print("Conceito: Insuficiente")
                break
            except Exception:
                print("Não era introduzido um valor numérico ou foi introduzido um número negativo. Try Again.")

    case 11:
        while True: #CFC = 0.22*FG + 0.22*FC + 0.22*FT + 0.11*FCT + 0.23*PAP
            try:
                print("Bom dia, isto é cálculo da nota final do curso.")
                print("Primeiro vais introduzir notas para calcular FG, depois FC, depois FT, no final, introduzas notas de FCT e PAP.")

                print("--- FG: ---")
                pt=float(input("Portugês: "))
                NegNCheck(pt)
                li=float(input("Inglês: "))
                NegNCheck(li)
                fil=float(input("Filosofía: "))
                NegNCheck(fil)
                ef=float(input("Educação Física: "))
                NegNCheck(ef)

                fg=round((pt+li+fil+ef)/4, 1)
                print(f"FG = {fg}")

                print("--- FC: ---")
                mat=float(input("Matemática A: "))
                NegNCheck(mat)
                fq=float(input("Física e Química A: "))
                NegNCheck(fq)

                fc=round((mat+fq)/2, 1)
                print(f"FC = {fc}")

                print("--- FT: ---")
                edp=float(input("Ética e Deontologia Profisional: "))
                NegNCheck(edp)
                acso=float(input("Arquitetura de Computadores e Sistemas Operativos: "))
                NegNCheck(acso)
                rc=float(input("Redes e Comunicação: "))
                NegNCheck(rc)
                fpr=float(input("Fundamentos de Programção: "))
                NegNCheck(fpr)
                api=float(input("Aplicaçãoes Informáticas: "))
                NegNCheck(api)
                poo=float(input("Programação Orientada a Objetos: "))
                NegNCheck(poo)
                cpw=float(input("Construção de Páginas Web: "))
                NegNCheck(cpw)
                auro=float(input("Automação Robótica: "))
                NegNCheck(auro)
                pwam=float(input("Programação Web ou Aplicações Multimédia: "))
                NegNCheck(pwam)
                
                ft=round((edp+acso+rc+fpr+api+poo+cpw+auro+pwam)/9, 1)
                print(f"FT = {ft}")

                fct=float(input("FCT: "))
                NegNCheck(fct)
                pap=float(input("PAP: "))
                NegNCheck(pap)

                cfc = 0.22*fg + 0.22*fc + 0.22*ft + 0.11*fct + 0.23*pap

                print(f"A tua nota do curso (CFC) é {round(cfc,0)}")
                

                break
            except Exception:
                print("Não era introduzido um valor numérico ou foi introduzido um número negativo. Try Again.")