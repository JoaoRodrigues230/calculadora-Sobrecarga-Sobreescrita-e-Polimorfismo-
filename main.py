from calculadora import *

if __name__ == '__main__':
    a1 = Adicao(4)
    s1 = Subtracao(1)
    
    calc = Calculadora()
    calc.add_operacoes(a1)
    calc.add_operacoes(s1)
    calc.calculadora_total()
    
    print(calc.resultado)