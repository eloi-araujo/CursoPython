def euler_4(a, b):
	"""
	Esta função calcula o maior produto palindrômico de números naturais entre "a" e "b".
	"""
	
	print("\n... Iniciando a função euler_4")
	
	# Se os valores digitados são iguais, checa se o produto é um palíndromo
	if a == b:
		prod = a * b
		if str(prod) == str(prod)[::-1]:
			result = "Os limites do intervalo são iguais e seu produto é o palíndromo:\n    {} * {} = {}".format(a,b,prod)
		else:
			result = "Os limites do intervalo são iguais e seu produto não é um palíndromo."
		return(result)
		
	# Caso não sejam iguais, o programa roda este código:
	else:
	
	# Ajustando os limites superior e inferior
		if a < b:
			linf = a
			lsup = b + 1 # Somando 1 para incluir o limite superior no cálculo
		
		else:
			linf = b
			lsup = a + 1 # Somando 1 para incluir o limite superior no cálculo

	# Iniciando variáveis
		indpalind = 0 # variável indicadora: vale 0 se nenhum palíndromo foi encontrado
		prodmax = 0
		
		for p1 in range(linf,lsup):
			for p2 in range(p1,lsup):
				prod = p1 * p2
			
				if str(prod) == str(prod)[::-1] and prod > prodmax:
					indpalind = 1
					prodmax = prod
					pmax1 = p1
					pmax2 = p2
	
		if indpalind == 0:
			result = "Não foram encontrados produtos palindrômicos de números inteiros entre {} e {}.".format(linf,lsup-1)
		else:
			result = "O maior produto palindrômico de números inteiros entre {} e {} é:\n    {} * {} = {}.".format(linf,lsup-1,pmax1,pmax2,prodmax)
			
		return(result)

from time import time

if __name__ == "__main__":
	# Entrada de dados:
	a = int(input("\nVamos calcular o maior produto palindrômico de números inteiros entre:\n    "))
	b = int(input("e:\n    "))
		
	# Chamada da função
	ti = time()
	result = euler_4(a, b)
	tf = time()
	tp = tf - ti
	
	# Resultado
	print("\n{}".format(result))
	print("Tempo de processamento:\n    {:.6f}s".format(tp))