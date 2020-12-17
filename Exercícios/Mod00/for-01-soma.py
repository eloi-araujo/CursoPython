N = 100
print("Soma dos ímpares menores que {}:".format(N))

soma = 0
for k in range(1, N, 2):
	soma += k
print(soma)

formulinha = (N // 2)**2  # (Calculando de duas maneiras distintas)
print(soma == formulinha)