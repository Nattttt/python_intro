# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 10
# SciPy: Integración numérica

from scipy.integrate import quad, romberg
from scipy import sin, exp, pi


def f(t):
    return exp(-t) * sin(t)


def main():
    print(quad(f, 0, pi))
    print(romberg(f, 0, pi))

    print(quad(f, 0, float('inf')))

if __name__ == '__main__':
    main()
