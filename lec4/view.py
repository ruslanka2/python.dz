
from fractions import Fraction
from cmath import *
from sys import *




def get_value():
    value = input('Введите число: ')
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value

def get_operation():
    op=input('Введите необходимую операцию ')
    return op

def get_resultat(res):
    print(f'Резултат вычисления: {res}')

