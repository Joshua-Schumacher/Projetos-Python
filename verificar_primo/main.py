numero = int(input("Digite um número: "))

def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True    
    
if verificar_primo(numero):
    print("É primo!")
else:
    print("Não é primo!")