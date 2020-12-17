# Vamos definir uma função chamada wat(), para chamá-la adiante,
# tal como fizemos com as funções print, randint, choice, etc.
def wat():
    # Em tempo de execução, vamos pedir para o usuário informar um número:
    N = int(input('Escolha um número de 0 a 7: '))
    print('    # Intervalo inicial [0 <= N <= 7].')
    
    if N <= 3:
        print('    # Descobrimos que [0 <= N <= 3]...')
        
        if N <= 1:
            print('    # Descobrimos que [0 <= N <= 1]...')
            
            if N <= 0:
                print('# Achamos N = 0!')
                
            else:
                print('# Achamos N = 1!')
                
        else:
            print('    # Descobrimos que [2 <= N <= 3]...')
            
            if N <= 2:
                print('# Achamos N = 2!')
                
            else:
                print('# Achamos N = 3!')
                
    else:
        print('    # Descobrimos que [4 <= N <= 7]...')
        
        if N <= 5:
            print('    # Descobrimos que [4 <= N <= 5]...')
            
            if N <= 4:
                print('# Achamos N = 4!')
                
            else:
                print('# Achamos N = 5!')
                
        else:
            print('    # Descobrimos que [6 <= N <= 7]...')
            
            if N <= 6:
                print('# Achamos N = 6!')
                
            else:
                print('# Achamos N = 7!')
                
#  O if a seguir representa algo como "Se estiver rodando este arquivo diretamente":
if __name__ == "__main__":
    wat()    # Chamada da função wat(), definida acima
# Um else desse if representaria algo como "Se estiver sendo importado por outro script"