#additional script

def valueCheck(num, num1, num2=None, num3=None):
        if num2==None:
                if num != num1:
                    raise Exception
        elif num3 == None:
            if num != num1 and num != num2:
                raise Exception
        else:
            if num != num1 and num != num2 and num!=num3:
                raise Exception


   
        
def deuceBreak(playerA, playerB, service1):
    print("Deuce break!")
    deuceLog = []
    pointA=0; pointB=0
    idd=0
    while True: #point loop
            if service1: print(f"{playerA} está a servir!")
            else: print(f"{playerB} está a servir!")

            idd+=1
            while True:
                try:
                    pointScore = int(input(f"\nQuem acertou o ponto, {playerA} ou {playerB} ? (input 1 ou 2): "))
                    valueCheck(pointScore, 1, 2)
                    break
                except Exception:
                    print("Foi introduzido um número errado, try again")
            
            if pointScore == 1:
                pointA+=1
                adv=playerA
                if pointA > pointB:
                    deuceLog.append(f"ADV {playerA}")
                

            if pointScore == 2:
                pointB+=1
                adv=playerB
                if pointB > pointA:
                    deuceLog.append(f"ADV {playerB}")
            
            print(f"{adv} está em Advantage!\n")

            if pointA==1 and pointB==1:
                print("Deuce!")
                pointA=0
                pointB=0
                deuceLog.append("DEUCE")

            if pointA==2:
                winJogo = playerA
                break
            elif pointB==2:
                winJogo = playerB
                break
    return winJogo, deuceLog, idd

def tieBreak(playerA, playerB):
    pointTimeMachine = []
    pointA=0; pointB=0
    print("Tie Break!!!")
    while True: #point loop
            while True:
                try:
                    pointScore = int(input(f"Quem acertou o ponto, {playerA} ou {playerB} ? (input 1 ou 2 e 0 para anular o último ponto): "))
                    valueCheck(pointScore, 1, 2, 0)
                    break
                except Exception:
                    print("Foi introduzido um número errado, try again")

            if pointScore == 1:
                pointA+=1
                pointTimeMachine.append(pointScore)

            elif pointScore == 2:
                pointB+=1
                pointTimeMachine.append(pointScore)

            elif pointScore == 0:
                try:
                    lastPoint = pointTimeMachine.pop() #for future: the problem was resolved using .pop(): it removes last element also returning it to a variable. No need for counters, as they are hard to manage (in this case)
                    if lastPoint == 1:
                        pointA-=1

                    elif lastPoint == 2:
                        pointB-=1
                except Exception: print("Eliminaram todos pontos")

            print(f"{pointA}!{pointB}")

            if pointA>=7 and pointA>= pointB +2:
                 winJogo = playerA
                 break
            elif pointB>=7 and pointB>= pointA + 2:
                winJogo = playerB
                break

    return winJogo


def showList(lista):
    if lista is None:
        print("None")
    else:
        for i in lista:
            print(f"{i}")
