a, b = 1, 1  # Fibonaccis iniciais (vamos sempre lembrar de um par consecutivo).

while b < 1000:
	lembrar = a   # Se começássemos com a = b, perderíamos o valor de a!
	a = b
	b += lembrar  # Daria pra fazer o while com uma linha só: "a, b = b, a+b"

# Só saímos do 'while' quando b >= 1000!
print("Último Fibonacci menor que 1000: {}".format(a))