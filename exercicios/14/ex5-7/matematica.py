import math

def soma(a, b):
    sum = a + b
    return sum
def subtracao(a, b):
    sum = a - b
    return sum

def area_circulo(r):
    area = round(math.pi*(r**2), 1)
    return area
    
def eh_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2): #3 porque o mínimo é 3, quilo porque verificar até raiz do número, e pulamos números pares
        if n % i == 0:
            return False
        
    return True

def maior(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return '='
    
def doubleIntInput(text):
    return map(int, input(text).split())