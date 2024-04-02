# Cree un programa que dada una lista de números imprima sólo los que son pares.
# Nota: utilice la sentencia continue donde haga falta.

numeros = [10, 34, 54, 236, 21, 67.3, 98, 3.2, 56, 678, 343, 4.6]

for num in numeros:
    if num % 2 != 0:
        continue
    else:
        print(num)