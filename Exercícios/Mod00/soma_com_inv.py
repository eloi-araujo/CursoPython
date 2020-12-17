def inverter_numero(x):  # Imagine que x = 23456 (x é um número inteiro).
    s = str(x)          # Criamos a variável s, com valor "23456" (uma string);
    s = s[::-1]        # Agora, s recebe "65432";
    x = int(s)        # Finalmente, x recebe s transformada em inteiro: 65432!
    return x         # Retornamos 65432, o "inverso" de 23456 :>

def soma_com_inv(a):
    return a + inverter_numero(a)

x = 1234567
soma = soma_com_inv(x)

print(soma)
print(soma == 1234567 + 7654321)  # teste simples