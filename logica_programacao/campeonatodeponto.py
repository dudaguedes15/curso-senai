usuario_correto = "admin"
senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break
    elif usuario != usuario_correto:
        print("Usuário incorreto.")
    else:
        print("Senha incorreta.")
    tentativas += 1
else:
    print("Usuário bloqueado por excesso de tentativas.")
