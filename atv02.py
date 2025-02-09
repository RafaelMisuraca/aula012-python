class Veiculo:
    def __init__(self):
        self.modelo =  None
        self.cor = None

    def definir_modelo(self, modelo):
        self.modelo = modelo
        return self
    
    def definir_cor(self, cor):
        self.cor = cor
        return self
    
    def exibir_info(self):
        print(f'Veículo: {self.__class__.__name__}, Modelo: {self.modelo}, Cor: {self.cor}')

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.motor_ligado = False
    def ligar_motor(self):
        self.motor_ligado = True

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.tem_cestinha = False
    def adicionar_cestinha(self):
        self.tem_cestinha = True
        print(f'A bicicleta {self.modelo} agora tem uma cestinha')
        return self
    
carro1 = Carro().definir_modelo('Ferrari').definir_cor('Vermelho').ligar_motor()
carro1.exibir_info()
bike1 = Bicicleta().definir_modelo('Caloi').definir_cor('Azul').adicionar_cestinha
bike1.exibir_info()