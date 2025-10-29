print("exercicio:\n")
escolha = input()

if escolha == "1":
    nome = "Ana"
    idade = 15
    altura = 1.65

    print(nome)
    print(idade)
    print(altura)
if escolha == "2":
    nome_aluno = "João"
    nota1 = 8.5
    nota2 = 7.0
    nota3 = 9.2

    print(f"O aluno {nome_aluno} obteve as notas: {nota1}, {nota2} e {nota3}.")

    media = (nota1 + nota2 + nota3)/3

    media = round(media, 2)

    print(f"A média do aluno {nome_aluno} é: {media}.")

if escolha == "3":
    nome_professor = "Maria"
    quantidade_alunos = 30
    duracao_aula = 1.5

    print(f"A professora {nome_professor} dará uma aula para {quantidade_alunos} alunos que durará {duracao_aula} horas.")


if escolha == "4":
    print("Insira vossos dados.\n")

    print("Nome: ")
    nome=input()

    print("\nIdade: ")
    idade=input()

    print("\nCidade em que vive: ")
    cidade=input()

    print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")





