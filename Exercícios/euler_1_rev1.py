from time import time

def euler_1(a, b, N):
	"""
	Esta função calcula o somatório dos números naturais múltiplos de "a" ou "b" menores que "N".
	"""
	
	print("\n... Iniciando a função euler_1")
	soma = 0
	
	# Soma dos múltiplos de a
	for i in range(a,N,a):
		soma += i
	
	# Soma dos múltiplos de b...
	for j in range(b,N,b):
		# ... que não são múltiplos de a (já foram somados no outro laço)
		if j % a != 0:
			soma += j
			
	return soma

if __name__ == "__main__":
	# Entrada de dados:
	N = int(input("\nVamos calcular o somatório de números naturais menores que:\n    "))
	a = int(input("que sejam múltiplos de:\n    "))
	b = int(input("ou múltiplos de:\n    "))
	
	# Chamada da função
	ti = time()
	soma = euler_1(a, b, N)
	tf = time()
	tp = tf - ti
	
	# Resultado
	print("\nA soma dos números naturais múltiplos de {} ou {} menores que {} é:\n    {}".format(a, b, N, soma))
	print("Tempo de processamento:\n    {:.6f}s".format(tp))