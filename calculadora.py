from abc import ABC, abstractmethod
from typing import List

class Operacao(ABC):
    operador : float

    def __init__(self, op : float):
        self.operador = op

    @abstractmethod
    def calcular (self, n : float):
        pass

    @abstractmethod
    def calcular_inverso(self, n: float):
        pass

class Adicao(Operacao):
    def calcular(self, n: float):
        return n + self.operador
    
    def calcular_inverso(self, n: float):
        return n - self.operador

class Subtracao(Operacao):
    def calcular(self, n: float):
        return n - self.operador
    
    def calcular_inverso(self, n: float):
        return n + self.operador

class Calculadora:
    resultado : float
    operacoes : List[Operacao]

    def __init__(self):
        self.resultado = 0.0
        self.operacoes = []

    def add_operacoes(self, op : Operacao):
        self.operacoes.append(op)
    
    def calculadora_total(self):
        calculo = 0
        for op in self.operacoes:
            calculo = op.calcular(calculo)
        self.resultado = calculo

    def desfazer_ultima(self):
        op = self.operacoes.pop()
        self.resultado = op.calcular_inverso(self.resultado)