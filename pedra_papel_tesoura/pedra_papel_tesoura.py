jogadas_maquina = ["pedra", "papel", "tesoura"]

num_jogadas = int(input("Quantas vezes quer jogar? "))
print(f"Você tem {num_jogadas} jogadas")

jogadas_player = ""


import random
match jogadas_player:
    case "pedra":
        print("Você jogou pedra")
    case "papel":
        print("Você jogou papel")
    case "tesoura":
        print("Você jogou tesoura")

for i in range(num_jogadas):  
    
   
    jogadas_player = input("Faça uma jogada de pedra, papel ou tesoura  ")
    
    maquina = random.choice(jogadas_maquina)
    print(f"A máquina jogou:  {maquina}")
    
    if maquina == jogadas_player:
        print("Deu empate!")
    elif maquina == "pedra" and jogadas_player == "papel":
        print("Parabêns você ganhou!")
    elif maquina == "pedra" and jogadas_player == "tesoura":
        print("A máquina ganhou!")
    elif maquina == "papel" and jogadas_player == "pedra":
        print("A máquina ganhou!")
    elif maquina == "papel" and jogadas_player == "tesoura":
        print("Parabêns você ganhou!")
    elif maquina == "tesoura" and jogadas_player == "pedra":
        print("Parabêns você ganhou!")
    elif maquina == "tesoura" and jogadas_player == "papel":
        print("A máquina ganhou!")
    else:
        print("fim")

    num_jogadas -= 1
    if num_jogadas != 0:
        print(f"Você ainda tem {num_jogadas} jogadas")
    else:
        print("Fim de jogo")
