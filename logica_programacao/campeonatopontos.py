maior_pontuacao = -1
jogador_melhor = ""

iniciantes = 0
intermediarios = 0
avancados = 0

contador = 1

while contador <= 6:
    nome = input("Digite o nome do jogador: ")
    pontuacao = int(input("Digite a pontuação: "))

    if pontuacao <= 20:
        print(nome, "- Iniciante")
        iniciantes += 1
    elif pontuacao <= 50:
        print(nome, "- Intermediário")
        intermediarios += 1
    else:
        print(nome, "- Avançado")
        avancados += 1

    if pontuacao > maior_pontuacao:
        maior_pontuacao = pontuacao
        jogador_melhor = nome

    contador += 1

print("\n--- Resultado Final ---")
print("Maior pontuação:", jogador_melhor, "-", maior_pontuacao, "pontos")
print("Iniciantes:", iniciantes)
print("Intermediários:", intermediarios)
print("Avançados:", avancados)
