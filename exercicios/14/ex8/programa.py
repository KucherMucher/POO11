import conversoes as cf

escolha = input("Insire temperatura (em Celcius ou Farenheit): ")

valorf = 0
valor = float((''.join(filter(lambda x: x.isdigit() or x == '.', escolha))).strip())


print(escolha, valor)

if escolha.endswith('F'):
    valorf = cf.fahrenheit_para_celsius(valor)
elif escolha.endswith('C'):
    valorf = cf.celsius_para_fahrenheit(valor)

print(round(valorf, 2))