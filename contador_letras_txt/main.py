
def contador_letras():
    with open("texto.txt", "r") as arquivo:
        conteudo = arquivo.read()

    contador = 0
    for caractere in conteudo:
        if caractere.isalpha():
            contador += 1
    return contador

total_letras = contador_letras()
print(f"O total de letras no arquivo é: {total_letras}")