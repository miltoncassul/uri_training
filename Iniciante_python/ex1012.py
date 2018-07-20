'''entrada = input()
numerosComoString = entrada.split()
numeros = [float(numero) for numero in numerosComoString]

a, b, c = numeros'''

a,b,c = input()

pi=3.14159

triangulo = (a*c)/2 	#Calculo da area do triangulo
circulo = (pi * c ** 2)	#Calculo da area do circulo
trapezio = ((a+b)*c)/2 	#Calculo da area do trapezio
quadrado = b*b 			#Calculo da area do quadrado
retangulo = a*b 		#Calculo da area do retangulo

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))