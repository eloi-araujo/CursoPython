from time import time

def euler_6(N):
	"""
	Esta função calcula a diferença entre o quadrado da soma e a soma dos quadrados dos números naturais de 1 a N (incluindo N).
	"""
	
	print("\n... Iniciando a função euler_6")
	
	# Iniciando variáveis
	soma = 0
	somaq = 0
	
	# Fazendo os somatórios
	for i in range(1,N+1):
		soma += i
		somaq += (i**2)
		
	dif = (soma**2) - somaq
		
	return soma, somaq, dif

if __name__ == "__main__":
	# Entrada de dados:
	N = int(input("\nVamos calcular a diferença entre o quadrado da soma e a soma dos quadrados dos números naturais menores ou iguais a:\n    "))
		
	# Chamada da função
	ti = time()
	soma, somaq, dif = euler_6(N)
	tf = time()
	tp = tf - ti
	
	# Apresentação do resultado
	print("\nA diferença entre o quadrado da soma e a soma dos quadrados dos números naturais até (e incluindo) {} é:\n    {}**2 - {} =".format(N, soma, somaq))
	print("    {} - {} = {}".format(soma**2, somaq, dif))
	print("Tempo de processamento:\n    {:.6f}s".format(tp))