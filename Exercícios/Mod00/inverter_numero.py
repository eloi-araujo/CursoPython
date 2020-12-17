def inverter_numero(x):  # Imagine que x = 23456 (x é um número inteiro).
    s = str(x)          # Criamos a variável s, com valor "23456" (uma string);
    s = s[::-1]        # Agora, s recebe "65432";
    x = int(s)        # Finalmente, x recebe s transformada em inteiro: 65432!
    return x         # Retornamos 65432, o "inverso" de 23456 :>

print(inverter_numero(23456))