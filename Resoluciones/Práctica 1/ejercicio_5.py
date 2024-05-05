# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta.

numeros = []

while True:
    num = int(input('Ingrese un número (0 para terminar la carga): '))
    if num != 0:
        numeros.append(num)
    else:
        break

for num in numeros:
    if num > 0:
        print(num)
    else:
        break