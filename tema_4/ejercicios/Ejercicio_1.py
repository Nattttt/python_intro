# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 1
# Funciones lambda


def suma_cuadrados(a, b):
    return sum(map(lambda x: x ** 2, range(a, b + 1)))


def main():
    print(suma_cuadrados(11, 16))

if __name__ == '__main__':
    main()
