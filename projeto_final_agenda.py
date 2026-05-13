import getpass 

def configurar_login():
    print("\n--- Configurações de Login ---")
    nova_senha = getpass.getpass('Digite a nova senha (os caracteres não aparecerão): ')
    confirmacao_senha = getpass.getpass('Confirme a nova senha: ')

    if nova_senha == confirmacao_senha:
        print('\n[SUCESSO] Senha alterada com sucesso!')
        return nova_senha
    else:
        print('\n[ERRO] As senhas não coincidem! A senha não foi alterada.')
        return None

def realizar_login_com_tentativas():

    senha_padrao = "123456"
    tentativas_restantes = 5
    login_sucesso = False
    
    
    print('\n--- Sistema de Login ---')
    nome_usuario = input('Digite seu login: ')
    
    while tentativas_restantes > 0 and not login_sucesso:
        print(f'\nTentativas restantes: {tentativas_restantes}')
        senha_digitada = getpass.getpass('Digite sua senha (os caracteres não aparecerão): ')

        if senha_digitada == senha_padrao:
            print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
            login_sucesso = True

        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print('\n[ERRO] Senha incorreta! Tente novamente.')
            else:
                print('\n[BLOQUEADO] número de tentativas excedido!')

realizar_login_com_tentativas()

def opcoes_menu():

    print("\n--- Menu Principal ---")
    print("1. configurações")
    print("2. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha
    if escolha == "1":
        
opcoes_menu()