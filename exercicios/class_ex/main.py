exercicio = int(input("Escolhe o exercicio (1-5): "))

match exercicio:    
    case 1:
        class Filme():
            def __init__(self, titulo, genero, duracao):
                self.titulo = titulo
                self.genero = genero
                self.duracao = duracao

            def mostrar_filme(self):
                print(f"Título do Filme  - {self.titulo}",
                    f"\nGénero do Filme  - {self.genero}",
                    f"\nDuração do Filme - {self.duracao}")
                

        f1 = Filme(titulo="Despicable Me", genero="Comedy", duracao="1h35m")
        f2 = Filme(titulo="Cars 2", genero="Action", duracao="1h46m")

        print("Filme 1: ")
        f1.mostrar_filme()
        print("\nFilme 2: ")
        f2.mostrar_filme()
    case 2:
        class Produto():
            def __init__(self, nome, preco, quantidade):
                self.nome = nome
                self.preco = preco
                self.quantidade = quantidade

            def mostrar_produto(self):
                print(f"Nome do produto - {self.nome}",
                      f"\nPreço do produto - {self.preco}")
                
            def valor_stock(self):
                return self.quantidade
            
        p1 = Produto(nome="M&Ms", preco="3.89€", quantidade="137")
        p2 = Produto(nome="Dr. Pepper", preco="1.49€", quantidade="369")

        print("Produto 1:\n")
        p1.mostrar_produto()
        print(f"Stock: {p1.valor_stock()}")

        print("\nProduto 2:\n")
        p2.mostrar_produto()
        print(f"Stock: {p2.valor_stock()}")

    case 3:
        class Telemovel():
            def __init__(self, marca, modelo, bateria=20):
                self.marca = marca
                self.modelo = modelo
                self.bateria = bateria 

            def carregar(self, valor):
                if self.bateria + valor <=100:
                    self.bateria += valor
                    print(f"Carregou {valor}%.")
                else:
                    self.bateria = 100

            def usar(self, valor):
                if self.bateria - valor >= 0:
                    self.bateria -= valor
                    print(f"Usou {valor}%.")
                else:
                    self.bateria = 0

            def mostrar_bateria(self):
                print(f"Bateria - {self.bateria}%.")

        telemovel = Telemovel(marca="iPhone", modelo="XR")

        telemovel.carregar(69)
        telemovel.usar(31)
        telemovel.mostrar_bateria()

    case 4:
        class Videojogo():
            def __init__(self, nome, categoria, pontuacao=0):
                self.nome = nome
                self.categoria = categoria
                self.pontuacao = pontuacao

            def aumentar_pontuacao(self, valor):
                self.pontuacao += valor
            
            def mostrar_dados(self):
                print(f"Nome - {self.nome}",
                      f"\nCategoria - {self.categoria}",
                      f"\nPontuação - {self.pontuacao}")
                
        v = Videojogo(nome="Jogo", categoria="Ação")

        v.aumentar_pontuacao(1)
        v.aumentar_pontuacao(2)
        v.aumentar_pontuacao(3)

        v.mostrar_dados()

