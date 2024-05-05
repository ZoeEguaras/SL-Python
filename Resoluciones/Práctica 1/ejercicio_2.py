# Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius 
# y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

grados_celsius = float(input('Ingrese una temperatura (Celsius): '))

print(f'Esa temperatura equivale a {((grados_celsius * 9) / 5) + 32} grados Fahrenheit.')