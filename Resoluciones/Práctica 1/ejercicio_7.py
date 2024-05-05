#  Escribe un programa que tome una lista de números enteros como entrada 
# del usuario. Luego, convierte cada número en la lista a string y únelos 
# en una sola cadena, separados por guiones ('-'). Sin embargo, excluye 
# cualquier número que sea múltiplo de 3 de la cadena final.

numeros = []

while True:
    num = int(input('Ingrese un número (0 para terminar la carga): )'))
    if num == 0:
        break
    else:
        numeros.append(num)

cadena = ''
for num in numeros:
    if num % 3 != 0:
        num = str(num)
        cadena += num + ' - '

cadena = cadena[0:len(cadena) - 2]
print(cadena)
