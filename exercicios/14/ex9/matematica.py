def soma(a, b):
    sum = a + b
    return sum
def subtracao(a, b):
    sum = a - b
    return sum

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
