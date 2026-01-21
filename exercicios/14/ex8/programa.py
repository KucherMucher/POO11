import conversoes as cf

escolha = input("Insire temperatura (em Celcius ou Farenheit): ")

valor = float((''.join(filter(lambda x: x.isdigit() or x == '.', escolha))).strip())


try:
    if escolha.upper().endswith('F'):
        valorf = cf.fahrenheit_para_celsius(valor)
    elif escolha.upper().endswith('C'):
        valorf = cf.celsius_para_fahrenheit(valor)

    print(round(valorf, 2))
except Exception:
    print("Não foi introduzida a escala")