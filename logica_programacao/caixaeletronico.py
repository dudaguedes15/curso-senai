saque = int(input("Digite o valor do saque: R$ "))

while saque / 10 != int(saque / 10):
    print("O valor deve ser múltiplo de 10.")
    saque = int(input("Digite outro valor: R$ "))

if saque <= 0:
    print("O valor deve ser positivo.")
elif saque > 0:
    notas = [100, 50, 20, 10]

    for nota in notas:
        quantidade = saque // nota
        print("Notas de R$", nota, ":", quantidade)
        saque = saque - (quantidade * nota)
else:
    print("Valor inválido.")
