import tlib
import random

#main script

pontos = [0, 15, 30, 40, 100]

print("Durante a contagem vais ter different controlos:\n" \
"0 - anular o ultimo ponto\n" \
"1 - escolher jogador A nos pontos\n" \
"2 - escolher jogador B nos pontos\n" \
"p - mostrar a história dos pontos\n" \
"j - mostrar a histótia dos jogos\n" \
"s - mostrar a histótia dos sets\n")





playerA = input("Nome do jogador A: ")
playerB = input("Nome do jogador B: ")

print("\n")

while True:
    try:
        bestof = int(input("Escolhe o formato de encontro (3/5): "))
        tlib.valueCheck(bestof, 3, 5, None)
        break
    except Exception:
        print("O número foi mal introduzido")

if bestof==3: winSetNum=2
elif bestof==5: winSetNum=3

setA=0
setB=0

setLog = ["-", f"{playerA} 0 : {playerB} 0"]
jogoLog = ["-"]
pointLog = []
ip=0
iss=0
ij=0

service1=random.choice([True, False])
while True: #set loop
    print("\nComeça o set!")
    iss+=1
    jogoA=0; jogoB=0
    jogoLog.append(f"{playerA} 0 - {playerB} 0")
    if iss>1: ij+=1
    while True: #game loop
        print("\nComeça o jogo!\n")

        if service1: print(f"{playerA} está a servir!")
        else: print(f"{playerB} está a servir!")

        ij+=1
        pointA=0; pointB=0
        
        pointTimeMachine = []
        pointLog.append(f"{playerA} 0 | {playerB} 0")
        if ij>1: ip+=1
        
        while True: #point loop
            ip+=1 # para timemachine dos pontos e para database
            while True:
                try:
                    pointScore = input(f"\nQuem acertou o ponto, {playerA} ou {playerB} ? (input 1 ou 2 e 0 para anular o último ponto): ")
                    if pointScore.isnumeric():
                        pointScore = int(pointScore)
                        tlib.valueCheck(pointScore, 1, 2, 0)
                        break
                    elif pointScore=="p":
                        tlib.showList(pointLog)
                    elif pointScore=="j":
                        tlib.showList(jogoLog)
                    elif pointScore=="s":
                        tlib.showList(setLog)
                    else:
                        raise Exception
                
                except Exception:
                    
                    print("Foi introduzido um número errado, try again")

            
            if int(pointScore) == 1:
                pointA+=1
                pointTimeMachine.append(pointScore)

            elif int(pointScore) == 2:
                pointB+=1
                pointTimeMachine.append(pointScore)

            elif int(pointScore) == 0:
                try:
                    lastPoint = pointTimeMachine.pop() #for future: the problem was resolved using .pop(): it removes last element also returning it to a variable. No need for counters, as they are hard to manage (in this case)
                    if lastPoint == 1:
                        pointA-=1

                    elif lastPoint == 2:
                        pointB-=1
                except Exception: print("Eliminaram todos pontos")


            pointLog.append(f"{playerA} {pontos[pointA]} | {playerB} {pontos[pointB]}")
            print(pointLog[ip])
            print(jogoLog[ij])
            print(setLog[iss])

            if (pointA>3 and pointB<3):
                 winJogo = playerA
                 break
            elif (pointA<3 and pointB>3):
                winJogo = playerB
                break
            elif pointA == 3 and pointB == 3:
                winJogo, deuceLog, idd = tlib.deuceBreak(playerA, playerB, service1)
                pointLog.extend(deuceLog)
                ip+=idd
                break
            
        
        print(f"\n{winJogo} ganhou o jogo!\n")

        if winJogo == playerA:
            jogoA+=1
        elif winJogo == playerB:
            jogoB+=1
        service1 = not service1
        jogoLog.append(f"{playerA} {jogoA} - {playerB} {jogoB}")
        print(jogoLog[ij+1])
        print(setLog[iss])

        match jogoA:
            case 0 | 1 | 2 | 3 | 4:
                if jogoB==6:
                    winSet=playerB
                    break
            case 5:
                if jogoB==7:
                    winSet=playerB
                    break
            case 6:
                if jogoB <= 4:
                    winSet=playerA
                    break
                elif jogoB == 6:
                    winSet=tlib.tieBreak(playerA, playerB)
                    ij+=1
                    if winSet==playerA:
                        jogoLog.append(f"{playerA} 7 - {playerB} 6")
                        print(f"{jogoLog[ij+1]}")
                    elif winSet==playerB:
                        jogoLog.append(f"{playerA} 6 - {playerB} 7")
                        print(f"{jogoLog[ij+1]}")
                    
                    break
            case 7:
                winSet=playerA
                break

    print(f"\n{winSet} ganhou um set!\n")

    if winSet == playerA:
        setA+=1
    elif winSet == playerB:
        setB+=1

    setLog.append(f"{playerA} {setA} : {playerB} {setB}")
    print(setLog[iss+1])

    if setA==winSetNum:
        winTennis = playerA
        break
        
    elif setB==winSetNum:
        winTennis = playerB
        break

print(f"\n{winTennis} ganhou o encontro!")