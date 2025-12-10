from matematica import soma, doubleIntInput

try:
    a, b = doubleIntInput("Insira dois números (com espaço): ")
except Exception:
    print("Não insirou o espaço")
    quit

print(f"A soma dos números é {soma(a, b)}")