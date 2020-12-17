L = []  # L começa como uma lista vazia;

for i in range(20, 2, -3):
    print(i)
    # Vamos inserir em L os números pares em range(20, 2, -3):
    if not i % 2:   # => Como 0 é falso em python, poderíamos usar not i % 2
        L.append(i)  # (método append acrescenta um elemento à lista)

print("No final, L =", L)