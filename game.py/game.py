print(25*"#")
print("Descubra o numero secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o numero secreto?")
print(43*"#")

import random


tentativas = 0
pontuacao = 100

secreto_num = random.randint(10,100)
    

dificuldade = input("Selecione um nível de dificuldade: \n 1-Fácil \n 2-médio \n 3-difícil \n")
match dificuldade:
    case "1":
        perda = 10
        tentativas = 30
        print("Você selecionou a dificuldade fácil")
    case "2":
        perda = 20
        tentativas = 15
        print("Você selecionou a dificuldade média")
    case "3":
        perda = 50
        tentativas = 5
        print("Você selecionou a dificuldade difícil")

print(43*"#")

chance = 1

while chance <= tentativas:
    if pontuacao == 0:
            print("Seus pontos acabaram. Fim de jogo")
            break
    
    print(f"Tentativa {chance} de {tentativas}")
    palpite = int(input("Informe seu palpite(entre 10 e 100): "))
    
    if palpite < 10 or palpite > 100:
        print("Valor inválido")
        continue       

    print("Seu palpite é: {}".format(palpite))
   
    if (secreto_num == palpite):
        print("Você acertou miseravi")
        break    
    elif palpite < secreto_num:
        
        print("O palpite é menor que o número secreto")
        pontuacao -= perda
        print(f"Você errou miseravi. Perdeu {perda} pontos, você ainda tem {pontuacao} pontos.")  

    elif palpite > secreto_num:
        
        print("O palpite é maior que o número secreto")
        pontuacao -= perda
        print(f"Você errou miseravi. Perdeu {perda} pontos, você ainda tem {pontuacao} pontos.")  

    else:
        print("Valor inválido.")
    
    chance += 1
     

