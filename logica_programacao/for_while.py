# numeros = [1, 2, 3, 4, 5]
# soma = 0
# for numero in numeros:
#     soma = soma + numero
#     #soma+= numero
# print(soma)

# senha_correta = input("Digite a senha correta: ")
# senha = input("Digite a senha:")

# while senha != senha_correta:
#     print("Senha incorreta. Tente novamente.")
#     senha = input("Digite a seha: ")

# print("Seja bem-vindo!")

# soma = 0
# while True:
#     numero = int(input("Digite um numero "))
#     soma += numero
#     if numero == 0:
#         break
# print(soma)

numero_maior = 1
numero_menor = 1
numero = int(input("Digite um número: "))
controle = 0

while controle <10:
    numero = int(input("Digite um número: "))
    if numero > numero_maior:
        numero_maior = numero
    elif numero < numero_menor:
        numero_menor = numero
    controle += 1
print(f"O número menor foi: {numero_menor}")
print(f"O número maior foi: {numero_maior}")
    
