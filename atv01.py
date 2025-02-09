import math as math
class Forma:
    def __init__(self, base, altura, raio):
        self.base = base
        self.altura = altura
        self.raio = raio
    def area(self):
        pass
    def perimetro(self):
        pass

class Circulo(Forma):
    def area(self):
        resultado_c = self.raio**2 * math.pi
        print(f'A área do círculo é {resultado_c:.2f}')
    def perimetro(self):
        resultado2_c = self.raio * math.pi* 2
        print(f'O perímetro do círculo é {resultado2_c:.2f}')

class Retangulo(Forma):
    def area(self):
        resultado_r = self.base * self.altura
        print(f'A área do retângulo é {resultado_r:.2f}')
    def perimetro(self):
        resultado2_r = 2*self.base + 2*self.altura
        print(f'O perímetro do retângulo é {resultado2_r}')

circulo = Circulo(None, None, 5)
retangulo = Retangulo(5, 8, None)

circulo.area()
circulo.perimetro()

retangulo.area()
retangulo.perimetro()