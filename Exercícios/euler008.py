from time import time

def ler_arquivo(fname):
	"""Recebe o nome do arquivo e retorna uma lista com seus dígitos."""
	with open(fname, "r") as arquivo:
		# Abrimos o arquivo em modo de leitura ("r" de "read"), pois só queremos ler o conteúdo.
		# Vamos obter uma grande string com todo o conteúdo do arquivo:
		texto = arquivo.read()
		# Outro método disponível é o arquivo.readlines(), que cria uma lista de strings!

	# Vamos substituir as quebras de linha por nada, só sobrando dígitos:
	texto = texto.replace("\n", "")

	# E agora vamos pegar cada caractere, transformar em inteiro e adicionar a uma lista.
	L = []
	for caractere in texto:  # Strings são iteráveis! Esse for vai passar por cada caractere.
		L.append(int(caractere))
	# (Quem souber e quiser fazer uma versão mais eficiente dessa função, fique à vontade!)
	return L

def euler_8(ndigits,list):
	"""
	Calcula o maior produto possível entre 'ndigits' adjacentes na sequência numérica 'list'.
	Retorna os dígitos, o produto e a localização do primeiro entre eles.
	"""
	
	# Iniciando as variáveis
	prodmax = 0 # Produto máximo
	loc1max = 0 # Localização do primeiro elemento do produto máximo
	
	# Índice loc1 varre a lista da posição inicial até a 'ndigits' antes da final
	for loc1 in range(0,(len(list)-ndigits)):
		# Produtório de 'ndigits' elementos, iniciando pelo elemento neutro da multiplicação (1)
		prod = 1
		for i in range(ndigits):
			# Vai de loc1 até loc1 + 'ndigits'
			prod *= list[loc1+i]
		
		# Após o laço do produtório, verifica se prod encontrado é maior que o máximo armazenado
		if prod > prodmax:
			prodmax = prod
			loc1max = loc1
			
	return prodmax, loc1max

if __name__ == "__main__":
	# Entrada de dados:
	fname = "euler008-digits.txt" # Arquivo com a sequência numérica
	print("O arquivo com a sequência numérica é: {}".format(fname))
	digitos = ler_arquivo(fname)
#	print(digitos)
	ndigits = int(input("\nVamos calcular o maior produto possível entre os X números adjacentes de uma sequência numérica, sendo X:\n    "))
		
	# Chamada da função principal
	ti = time()
	prodmax, loc1max = euler_8(ndigits,digitos)
	tf = time()
	tp = tf - ti
	
	# Apresentação do resultado
	print("\nO maior produto entre {} dígitos adjacentes da sequência é:\n     {}".format(ndigits, prodmax))
	print("Entre os dígitos:\n    {}".format(digitos[loc1max:(loc1max+ndigits)]))
	print("\nO primeiro número encontra-se na posição {} da sequência original.".format(loc1max))
	print("Isto é: {} é o {}o. número da sequência, que é contada a partir da posição 0.".format(digitos[loc1max],(loc1max+1)))
	print("Tempo de processamento:\n    {:.6f}s".format(tp))