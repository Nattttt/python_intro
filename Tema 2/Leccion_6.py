# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 6
# Listas

fibonacci = [2, 34, 5, 1, 21, 3, 8, 13, 4]
len(fibonacci)

fibonacci.sort()
print(fibonacci)

fibonacci.reverse()
print(fibonacci)

fibonacci.remove(4)
print(fibonacci)

fibonacci.append(55)
print(fibonacci)

fibonacci.sort()
fibonacci.insert(0, 1)
print(fibonacci)

fibonacci.index(21)
fibonacci.count(1)

fibonacci.pop()
print(fibonacci)

# Lista vacia
vacia = []
len(vacia)