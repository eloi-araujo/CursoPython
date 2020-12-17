from random import choice    # Dada uma lista, choice escolhe um elemento ao acaso

# Elemento novo [lista?]
uma_lista = [2, 3, 5, 7, 11, 12, 13, 14, 15, 16, 17]

escolha = choice(uma_lista)    # escolha aleatória entre os elementos da lista

print("Escolhemos ao acaso o número {}".format(escolha))

if escolha <= 11 or escolha == 13 or escolha == 17:
    print("    # {} é um número primo!".format(escolha))
	
elif escolha < 15:
    print("    # {} é composto menor que 15.".format(escolha))
		
else:
    print("    # {} é composto maior ou igual a 15.".format(escolha))