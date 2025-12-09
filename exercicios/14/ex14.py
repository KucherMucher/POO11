import math

def vindas(nome):
    return print(f"Bem-vindo, {nome}!")

def maior(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return '='
    
def fatorial(n):
    fat = n
    for i in range(1, n):
        fat *= (n-i)
    return fat

def el_primo(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    
    

s = int(input("Escolhe o exercício: "))



match s:
    case 1:
        nome = input("Qual é o teu nome?: ")
        vindas()
    case 2:
        a, b = map(int, input("Insire dois números separados por espaço: ").split())
        maiorn = maior(a, b)
        print(f"O número maior é {maiorn}")
    case 3:
        n = int(input("Insire um número: "))
        n1 = fatorial(n)
        print(f"{n}! = {n1}")
    case 4: