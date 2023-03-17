
from itertools import repeat, product
from random import choice
from typing import Self
from juego import HORIZONTAL, LONGITUDES_BARCOS, VERTICAL, ORIENTACIONES, Barco, Case, Conventions
from decimal import Decimal, getcontext, ConversionSyntax, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_HALF_DOWN, ROUND_UP, ROUND_DOWN, ROUND_CEILING, ROUND_FLOOR, ROUND_05UP

instances = []
casillas_ocupadas = set()

# performance / legibilidad:
num_lineas = Conventions.tablero_num_lineas
num_columnas = Conventions.tablero_num_columnas
num2l = Conventions.generar_num_linea
num2c = Conventions.generar_num_columna

def __init__(self, longitud, orientacion, tocado, hundido):
        self.longitud = longitud
        self.orientacion = choice(ORIENTACIONES)
        self.tocado = False
        self.hundido = False

def horizontal(self):  
            if self.orientacion == HORIZONTAL:
                rang = choice(range(num_lineas))
                primero = choice(range(num_columnas + 1 - LONGITUDES_BARCOS))
                letra = num2l(rang)
                cifras = [num2c(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
                self.casillas = {Case.instances[l + c]
                              for l, c in product(repeat(letra, LONGITUDES_BARCOS), cifras)}
                
            else:
                rang = choice(range(num_columnas))
                primero = choice(range(num_lineas + 1 - LONGITUDES_BARCOS))
                cifra = num2c(rang)
                letras = [num2l(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
                # Crear el barco
                self.casillas = {Case.instances[l + c]
                              for l, c in product(letras, repeat(cifra, LONGITUDES_BARCOS))}
            return self.casillas

def instanciar(self):
    for existente in instances:
        if self.casillas.intersection(existente.casillas):
            break  # break relativo al "for existente in barcos:"
        else:
            # Agregar el barco en el contenedor de barcos
            instances.append(self)
            # Informar la casilla que contiene un barco.
            for casillas in self.casillas:
                casillas.contiene_barco = True
            # Agregar estas casillas a las casillas ocupadas :
            casillas_ocupadas.update(self.casillas)
                
@classmethod
def generar_barcos(cls):
        for longitud in Conventions.barcos_longitud:
            cls(longitud, choice(ORIENTACIONES), False, False)
