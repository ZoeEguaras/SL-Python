# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas 
# listas, una con los número pares y otras con los que son impares. 
# Imprima las listas al terminar de procesarlas.

numeros = [10, 34, 54, 236, 21, 67.3, 98, 3.2, 56, 678, 343, 4.6]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('NUMEROS PARES: ')
for num in pares:
    print(num)

print('NUMEROS IMPARES: ')
for num in impares:
    print(num)
