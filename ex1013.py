'''entrada = input()
numerosComoString = entrada.split()
numeros = [int(numero) for numero in numerosComoString]

a, b, c = numeros'''

entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorAB = (a + b + abs(a - b)) / 2
maiorAB = (maiorAB + c + abs(maiorAB - c)) / 2

print(round(maiorAB), "eh o maior")