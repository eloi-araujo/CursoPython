from time import time

def euler_4(a, b):
	"""
	Esta função calcula o maior produto palindrômico de números naturais entre "a" e "b".
	"""
	
	print("\n... Iniciando a função euler_4")
	
	# Garantindo os limites inferior (a) e superior (b)
	if a > b:
		a, b = b, a
	
	# Iniciando variáveis
	indpalind = 0 # variável indicadora: vale 0 se nenhum palíndromo foi encontrado
	prodmax = 0
	pmax1 = 0
	pmax2 = 0
	
	# Fazendo as multiplicações variando os fatores em ordem decrescente
	for p1 in range(b, a-1, -1):
		
		# Como p1 * p2 = p2 * p1, não é necessário começar o segundo laço do limite original b
		for p2 in range(p1, a-1, -1):
			prod = p1 * p2

			# Só verifica se é palíndromo se p1 x p2 > máximo já guardado
			if prod > prodmax:
				if euler_4_ispalindrome(prod):
					indpalind = 1
					prodmax = prod
					pmax1 = p1
					pmax2 = p2
			
			# Se p1 x p2 < máximo, já é possível testar o próximo p1 / sair do laço
			else:
				break
	
	return indpalind, pmax1, pmax2, prodmax

def euler_4_ispalindrome(a):
	"""
	Esta função checa se um valor é um palíndromo
	"""
	
	s = str(a)
	
	if s == s[::-1]:
		return True
		
	else:
		return False
		
if __name__ == "__main__":
	# Entrada de dados:
	a = int(input("\nVamos calcular o maior produto palindrômico de números inteiros entre:\n    "))
	b = int(input("e:\n    "))
		
	# Chamada da função
	ti = time()
	indpalind, pmax1, pmax2, prodmax = euler_4(a, b)
	tf = time()
	tp = tf - ti
	
	# Apresentação do resultado
	if indpalind == 0:
		if a == b:
			print("\nOs limites do intervalo são iguais ({}) e seu quadrado não é um palíndromo.".format(a))
		elif a < b:
			print("\nNão foram encontrados produtos palindrômicos de números inteiros entre {} e {}.".format(a,b))
		else:
			print("\nNão foram encontrados produtos palindrômicos de números inteiros entre {} e {}.".format(b,a))
	else:
		if a == b:
			print("\nOs limites do intervalo são iguais ({}) e seu quadrado é o palíndromo:\n    {} * {} = {}".format(a,pmax1,pmax2,prodmax))
		elif a < b:
			print("\nO maior produto palindrômico de números inteiros entre {} e {} é:\n    {} * {} = {}".format(a,b,pmax1,pmax2,prodmax))
		else:
			print("\nO maior produto palindrômico de números inteiros entre {} e {} é:\n    {} * {} = {}".format(b,a,pmax1,pmax2,prodmax))
	print("Tempo de processamento:\n    {:.6f}s".format(tp))