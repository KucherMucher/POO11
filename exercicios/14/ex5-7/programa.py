#ver 1

import matematica

try:
    a, b = matematica.doubleIntInput("Insira dois números (com espaço): ")
except Exception:
    print("Não insirou o espaço")
    quit

print(f"A soma dos números é {matematica.soma(a, b)}")
print(f"A subtração dos números é {matematica.subtracao(a, b)}")
if matematica.eh_primo(a): print(f"O número {a} é primo")
elif matematica.eh_primo(b): print(f"O número {b} é primo")
else: print("Os números são compostos")
print(f"O número maior é {matematica.maior(a, b)}")

r = int(input("Insire um raio: "))
print(f"A área do círculo é {matematica.area_circulo(r)}")