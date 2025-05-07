import random
import string

letras = string.ascii_lowercase
numeros = string.digits

elementos_senha = letras + numeros

senha = int(input("Informe o tamanho da senha "))

print(*random.sample(elementos_senha, senha))


