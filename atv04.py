class Veiculo:
    def __init__(self):
        self.motor_ligado = False
        self.acelerado = False
        self.frear = False

    def ligar_motor(self):
        if self.motor_ligado:
            print('Você não pode ligar o motor duas vezes.')
        else:
            self.motor_ligado = True
            print('Motor ligado com sucesso!')

    def acelerar(self):
        raise NotImplementedError("Método 'acelerar' deve ser implementado pela subclasse.")

    def frear(self):
        raise NotImplementedError("Método 'frear' deve ser implementado pela subclasse.")


class Carro(Veiculo):
    def acelerar(self):
        if not self.motor_ligado:
            print('Ligue o motor antes de acelerar.')
        elif self.acelerado:
            print('O carro já está acelerado.')
        else:
            self.acelerado = True
            print('Carro acelerando...')

    def frear(self):
        if not self.frear:
            self.acelerado = False
            self.frear = True
            print('Carro freando...')
        else:
            print('O carro já está freando.')


class Bicicleta(Veiculo):
    def ligar_motor(self):
        print('Bicicletas não têm motor!')

    def acelerar(self):
        if self.acelerado:
            print('A bicicleta já está em movimento.')
        else:
            self.acelerado = True
            print('Bicicleta acelerando...')

    def frear(self):
        if not self.frear:
            self.acelerado = False
            self.frear = True
            print('Bicicleta freando...')
        else:
            print('A bicicleta já está freando.')



print("--- Carro ---")
carro = Carro()
carro.ligar_motor()  
carro.acelerar()     
carro.frear()      

print("\n--- Bicicleta ---")
bicicleta = Bicicleta()
bicicleta.ligar_motor()  
bicicleta.acelerar()    
bicicleta.frear()        