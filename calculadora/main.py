print("Bem-vindo a calculadora!")

num1 = 0
num2 = 0
operacoes = ""

print("-"*55)


while operacoes != "5":
    print("Informe dois números que queira calcular")

    print("-"*55)

    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))

    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    
    print("-"*55)

    operacoes = input("Selecione uma operação matemática: \n 1-Soma \n 2-Subtração \n 3-Mutiplicação \n 4-Divisão \n 5-Sair \n")

    print("-"*55)
    
    match operacoes:
        case "1":
            print("A soma é: ", adicao)
        case "2":
            print("A subtração é: ", subtracao)
        case "3":
            print("A multiplicação é: ", multiplicacao)
        case "4":
            print("A divisão é: ", divisao)
        case "5":
            print("Sistema encerrado")
