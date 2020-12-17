from random import randint   # importamos uma função da biblioteca random

x = randint(4, 9)  # Número inteiro aleatório no intervalo [4,9]
print("Número aleatório:", x)

if x < 7:
	print("   # Entramos no bloco do if porque", x, "< 7;")
	
else:
	print("   # Entramos no bloco do else porque", x, ">= 7;")
	quadrado = x**2
	print("   # O quadrado de {} é {}!".format(x, quadrado))