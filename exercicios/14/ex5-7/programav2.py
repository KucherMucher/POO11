import matematica as m 

try:
    a, b = m.doubleIntInput("Insira dois números (com espaço): ")
except Exception:
    print("Não insirou o espaço")
    quit

print(f"A soma dos números é {m.soma(a, b)}")
print(f"A subtração dos números é {m.subtracao(a, b)}")
if m.eh_primo(a): print(f"O número {a} é primo")
elif m.eh_primo(b): print(f"O número {b} é primo")
else: print("Os números são compostos")
print(f"O número maior é {m.maior(a, b)}")

r = int(input("Insire um raio: "))
print(f"A área do círculo é {m.area_circulo(r)}")