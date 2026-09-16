crianca = 0
adolescente = 0
adulto = 0
idoso = 0
pessoas = 0

while pessoas < 10:
    idade = int(input("Digite a idade: "))

    if idade <= 12:
        crianca = crianca + 1

    elif idade <= 17:
        adolescente = adolescente + 1

    elif idade <= 59:
        adulto = adulto + 1

    else:
        idoso = idoso + 1

    pessoas = pessoas + 1

print("Crianças:", crianca)
print("Adolescentes:", adolescente)
print("Adultos:", adulto)
print("Idosos:", idoso)
