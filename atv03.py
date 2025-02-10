class Calculadora:
    def somar(self, a, b):
        if isinstance(a, int) and isinstance(b, int):  
            return a + b  
        elif isinstance(a, str) and isinstance(b, str):  
            return a + b  
        else:
            raise TypeError("Tipos de entrada não suportados. Use dois inteiros ou duas strings.")


calculadora = Calculadora()


resultado_inteiros = calculadora.somar(5, 10)
print(f"Soma de inteiros: {resultado_inteiros}") 


resultado_strings = calculadora.somar("Olá, ", "mundo!")
print(f"Concatenação de strings: {resultado_strings}")  


try:
    calculadora.somar(5, "texto")
except TypeError as e:
    print(e)  