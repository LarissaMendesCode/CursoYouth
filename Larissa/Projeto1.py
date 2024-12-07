class Carro:
    def __init__ (self,cor,modelo,ano,marca):
        self.cor= cor 
        self.modelo= modelo
        self.ano= ano
        self.marca= marca  
        self.capacidade=50
        self.ligado= False
        self.tanque=0

    def ligar(self):
            self.ligado= True

    def abastecer(self,qtd):
            if (self.tanque + qtd<=self.capacidade):
                self.tanque+=qtd
            else:
                print("Não foi possível abastecer")



meu_carro= Carro("preto", "supra MK4", 2018, "TOYOTA")
print(meu_carro.ano)
print(meu_carro.ligado)

meu_carro.ligar()
print(meu_carro.tanque)
meu_carro.abastecer(20)
print(meu_carro.tanque)
meu_carro.abastecer(25)
print(meu_carro.tanque)
meu_carro.abastecer(40)
print(meu_carro.tanque)

        