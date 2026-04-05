class Trotinete():
    def __init__(self, designacao):
        self.designacao = designacao
        self.__velocidade = 0

    def __avisar_limite(self):
        print("Beep! Limite de segurança atingido!")

    def get_velocidade(self):
        return self.__velocidade
    
    def set_velocidade(self, v):
        if v > 25:
            self.__velocidade = 25
            self.__avisar_limite()
        elif v < 0:
            self.__velocidade = 0
        else:
            self.__velocidade = v

    def acelarar(self, v):
        velocidade = self.__velocidade + v
        self.set_velocidade(velocidade)

    def travar(self, v):
        velocidade = self.__velocidade - v
        self.set_velocidade(velocidade)

    

trot = Trotinete("SUPER TRORINETE 6000"); print(f"Veículo: {trot.designacao}")

#teste 1
trot.acelarar(24); print(f"Velocidade atual: {trot.get_velocidade()} km/h")
#teste 2
trot.acelarar(1000); print(f"Velocidade após tentativa de excesso: {trot.get_velocidade()} km/h")
#teste 3
trot.travar(15); print(f"Velocidade após travar: {trot.get_velocidade()} km/h")
#teste 4
trot.travar(10000); print(f"Velocidade final (parada): {trot.get_velocidade()} km/h")



        
