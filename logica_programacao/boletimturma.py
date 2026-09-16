aprovados = 0
recuperacoes = 0
reprovados = 0

alunos = [1, 2, 3, 4, 5]

for aluno in alunos:
    nota1 = float(input(f"Digite a primeira nota do aluno {aluno}: "))
    nota2 = float(input(f"Digite a segunda nota do aluno {aluno}: "))

    media = (nota1 + nota2) / 2

    print(f"Média do aluno {aluno}: {media:.1f}")

    if media >= 6:
        print("Aprovado")
        aprovados += 1
    elif media >= 4:
        print("Recuperação")
        recuperacoes += 1
    else:
        print("Reprovado")
        reprovados += 1

print("\n--- Resultado da turma ---")
print(f"Aprovados: {aprovados}")
print(f"Recuperações: {recuperacoes}")
print(f"Reprovados: {reprovados}")
