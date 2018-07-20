'''
Dois carros (X e Y) partem em uma mesma direção. O carro X sai com
velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90
Km/h. Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o
carro Y tomar essa distância do outro carro.

Entrada
O arquivo de entrada contém um número inteiro.

Saída
Imprima o tempo necessário seguido da mensagem " minutos".
'''

import math

distancia = int (input())

	#S = s0 + vt
	#s1 + v1t = s2 + v2t
	#t = (s1 - s2)/(v2-v1)

t = abs(- distancia / (90 - 60)) * 60

print(round(t), "minutos")