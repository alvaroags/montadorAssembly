#quero fazer um algoritmo simples para teste do python

#definindo a função
def soma(a,b):
    return a+b

#definindo a função
def subtracao(a,b):
    return a-b

#definindo a função
def multiplicacao(a,b):
    return a*b

#definindo a função
def divisao(a,b):
    return a/b

#aqui começa o programa
print("Escolha uma das opções abaixo:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#recebendo a opção do usuário
opcao = int(input("Digite a opção desejada: "))
#recebendo os valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
#verificando a opção
if opcao == 1:
    print("O resultado da soma é: ", soma(valor1, valor2))
elif opcao == 2:
    print("O resultado da subtração é: ", subtracao(valor1, valor2))
elif opcao == 3:
    print("O resultado da multiplicação é: ", multiplicacao(valor1, valor2))
elif opcao == 4:
    print("O resultado da divisão é: ", divisao(valor1, valor2))
else:
    print("Opção inválida")

#fim do programa