resposta = "sim"

while resposta != "não":

    numero = int(input("Digite um número: "))

    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

    resposta = input("Deseja consultar outra tabuada? (sim/não): ")

    if resposta == "sim":
        print("Vamos continuar!")

    elif resposta == "não":
        print("Programa encerrado.")

    else:
        print("Resposta inválida.")
